import socket
import threading
import pickle
import time
import random

HOST = "0.0.0.0"
PORT = 5555
MAX_PLAYERS = 12

# Each player's data:
# players[player_id] = {
#   "pos": (x, y),
#   "element": (earth, electric, etc),
#   "gun": ()
#   "bullet": ()
#   "health": int,
#   "kills": int,
#   "is_dead": bool,
#   "respawn_time": float  (timestamp when they'll respawn),
# }

players = {}
bullets = []
next_player_id = 0

client_sockets = []
player_connections = {}

game_start_time = None
GAME_DURATION = 300
lavaY = 950

lock = threading.Lock()

def handle_client(conn, addr, player_id):
    """Receive data from the client and update global state accordingly."""
    print(f"[NEW CONNECTION] Player {player_id} connected from {addr}")
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            try:
                msg = pickle.loads(data)
            except:
                continue

            with lock:
                action = msg.get("action")
                pid = msg.get("player_id")

                if pid in players and players[pid]["is_dead"]:
                    continue

                if action == "move":
                    dx = msg.get("dx", 0)
                    dy = msg.get("dy", 0)
                    if pid in players:
                        px, py = players[pid]["pos"]
                        players[pid]["pos"] = (px + dx, py + dy)
                elif action == "jump":
                    if pid in players:
                        px, py = players[pid]["pos"]
                        players[pid]["pos"] = (px, py - 100)
                elif action == "shoot":
                    dx = msg.get("dx", 0)
                    dy = msg.get("dy", 0)
                    angle = msg.get("angle", 0)
                    if pid in players:
                        px, py = players[pid]["pos"]
                        bullet_speed_x = 4
                        bullet_speed_y = 6
                        bullets.append({
                            "x": px,
                            "y": py,
                            "dx": dx * bullet_speed_x,
                            "dy": dy * bullet_speed_y,
                            "owner_id": pid,
                            "type": "bullet",
                            "angle": angle
                        })
                elif action == "multibullet":
                    dx = msg.get("dx", 0)
                    dy = msg.get("dy", 0)
                    angle = msg.get("angle", 0)
                    if pid in players:
                        px, py = players[pid]["pos"]
                        multibullet_speed_x = 4
                        multibullet_speed_y = 6
                        bullets.append({
                            "x": px + 40,
                            "y": py,
                            "dx": dx * multibullet_speed_x,
                            "dy": dy * multibullet_speed_y,
                            "owner_id": pid,
                            "type": "multibullet",
                            "angle": angle
                        })
                        bullets.append({
                            "x": px,
                            "y": py,
                            "dx": dx * multibullet_speed_x,
                            "dy": dy * multibullet_speed_y,
                            "owner_id": pid,
                            "type": "multibullet",
                            "angle": angle
                        })
                        bullets.append({
                            "x": px - 40,
                            "y": py,
                            "dx": dx * multibullet_speed_x,
                            "dy": dy * multibullet_speed_y,
                            "owner_id": pid,
                            "type": "multibullet",
                            "angle": angle
                        })
                elif action == "nuke":
                    dx = msg.get("dx", 0)
                    dy = msg.get("dy", 0)
                    angle = msg.get("angle", 0)
                    if pid in players:
                        px, py = players[pid]["pos"]
                        nuke_speed_x = 4
                        nuke_speed_y = 6
                        bullets.append({
                            "x": px,
                            "y": py,
                            "dx": dx * nuke_speed_x,
                            "dy": dy * nuke_speed_y,
                            "owner_id": pid,
                            "type": "nuke",
                            "angle": angle
                        })
                elif action == "ancient_bullet":
                    dx = msg.get("dx", 0)
                    dy = msg.get("dy", 0)
                    angle = msg.get("angle", 0)
                    if pid in players:
                        px, py = players[pid]["pos"]
                        ancient_bullet_speed_x = 12
                        ancient_bullet_speed_y = 18
                        bullets.append({
                            "x": px,
                            "y": py,
                            "dx": dx * ancient_bullet_speed_x,
                            "dy": dy * ancient_bullet_speed_y,
                            "owner_id": pid,
                            "type": "ancient_bullet",
                            "angle": angle
                        })
                elif action == "element":
                    element = msg.get("element")
                    if pid in players:
                        players[pid]["element"] = element
                elif action == "shield":
                    if pid in players:
                        players[pid]["shield"] = not players[pid]["shield"]
    except Exception as e:
        print(f"[EXCEPTION] {e}")
    finally:
        with lock:
            if player_id in players:
                del players[player_id]
            if conn in client_sockets:
                client_sockets.remove(conn)
            if player_id in player_connections:
                del player_connections[player_id]

        conn.close()
        print(f"[DISCONNECT] Player {player_id} disconnected")

def broadcast_game_state():
    """
    Sends the entire game state (players, bullets) plus
    the countdown timer (time_left) to all clients.
    """
    global game_start_time, lavaY
    # Calculate time_left if we have at least 2 players and the timer started
    if game_start_time is not None:
        lavaY -= 0.01
        elapsed = time.time() - game_start_time
        time_left = max(0, GAME_DURATION - elapsed)
    else:
        time_left = GAME_DURATION
    game_state = {
        "players": players,   # includes positions, elements, health, kills, is_dead, etc.
        "bullets": bullets,
        "time_left": time_left,
        "lavaY": lavaY
    }
    data = pickle.dumps(game_state)

    for cs in client_sockets:
        try:
            cs.sendall(data)
        except:
            pass
def send_msg_to_player(pid, msg_dict):
    """
    Send a specific dictionary message to one player (if connected).
    """
    if pid in player_connections:
        try:
            player_connections[pid].sendall(pickle.dumps(msg_dict))
        except:
            pass
def check_bullet_collisions():
    """
    For each bullet, check if it collides with any *alive* player (besides its owner).
    If collision: reduce health by 5. If health <= 0 -> record a kill, set dead status, schedule respawn.
    Remove the bullet on collision (no piercing).
    """
    global bullets
    surviving_bullets = []
    for b in bullets:
        bx, by = b["x"], b["y"]
        owner_id = b["owner_id"]
        hit_something = False

        for pid, pdata in list(players.items()):
            if pid == owner_id or pdata["is_dead"]:
                continue

            bullet_left, bullet_right, bullet_top, bullet_bottom = 0, 0, 0, 0

            if b["type"] == "bullet" or b["type"] == "multibullet" or b["type"] == "ancient_bullet":
                bullet_left = bx + 22
                bullet_right = bx + 29
                bullet_top = by + 12.5
                bullet_bottom = by + 32.5
            if b["type"] == "nuke":
                bullet_left = bx + 18.5
                bullet_right = bx + 32.5
                bullet_top = by + 9.5
                bullet_bottom = by + 36

            px, py = pdata["pos"]
            player_left = px + 6.5
            player_right = px + 43.5
            player_top = py + 6.5
            player_bottom = py + 43.5

            if (bullet_right >= player_left and
                bullet_left <= player_right and
                bullet_bottom >= player_top and
                bullet_top <= player_bottom):
                if b["type"] == "bullet" or b["type"] == "multibullet" or b["type"] == "ancient_bullet":
                    pdata["health"] -= 5
                elif b["type"] == "nuke":
                    pdata["health"] -= 15
                hit_something = True

                if pdata["health"] <= 0:
                    if owner_id in players:
                        players[owner_id]["kills"] += 1
                        players[owner_id]["xp"] += 10
                    pdata["is_dead"] = True
                    pdata["health"] = 0

                break

        if not hit_something:
            surviving_bullets.append(b)
    bullets = surviving_bullets

def game_loop():
    """
    Continually update bullets, collisions, respawns, and broadcast updates.
    """
    global bullets
    while True:
        time.sleep(0.00694444)  # ~144 updates per second
        with lock:
            for b in bullets:
                b["x"] += b["dx"]
                b["y"] += b["dy"]
                b["dy"] += 0.1
            for pid, pdata in list(players.items()):
                px, py = pdata["pos"]
                if px >= 305 and px <= 1585 and py >= 877:
                    py = 877
                elif px >= 325 and px <= 450 and py >= 739 and py <= 744:
                    py = 739
                elif px >= 445 and px <= 570 and py >= 739 and py <= 744:
                    py = 739
                elif px >= 565 and px <= 690 and py >= 739 and py <= 744:
                    py = 739
                elif px >= 685 and px <= 810 and py >= 739 and py <= 744:
                    py = 739
                elif px >= 1080 and px <= 1205 and py >= 739 and py <= 744:
                    py = 739
                elif px >= 1200 and px <= 1325 and py >= 739 and py <= 744:
                    py = 739
                elif px >= 1320 and px <= 1445 and py >= 739 and py <= 744:
                    py = 739
                elif px >= 1440 and px <= 1565 and py >= 739 and py <= 744:
                    py = 739
                else:
                    py += 1
                pdata["pos"] = (px, py)

            bullets = [
                b for b in bullets
                if 0 <= b["x"] <= 1920 and 0 <= b["y"] <= 1080
            ]

            check_bullet_collisions()
            broadcast_game_state()

def main():
    global next_player_id, client_sockets, player_connections
    global game_start_time

    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    threading.Thread(target=game_loop, daemon=True).start()

    while True:
        conn, addr = server.accept()
        conn.setblocking(True)

        with lock:
            if len(players) >= MAX_PLAYERS:
                # Server is full
                msg = {"action": "server_full"}
                conn.sendall(pickle.dumps(msg))
                conn.close()
                continue

            # Assign new ID
            player_id = next_player_id
            next_player_id += 1

            color = (
                random.randint(50, 255),
                random.randint(50, 255),
                random.randint(50, 255)
            )
            element = "Earth"
            players[player_id] = {
                "pos": (400, 300), # random between  50 too 950 for x and 600 to 700 for y
                "element": element,
                "guntype": "DefaultGun",
                "health": 40,
                "kills": 0,
                "xp": 0,
                "is_dead": False,
                "shield": False
            }

            client_sockets.append(conn)
            player_connections[player_id] = conn

            # If we now have at least 2 players, and the timer hasn't started, start it
            if game_start_time is None and len(players) >= 2:
                game_start_time = time.time()
        handshake_msg = {
            "action": "handshake",
            "player_id": player_id,
            "max_players": MAX_PLAYERS
        }
        conn.sendall(pickle.dumps(handshake_msg))
        t = threading.Thread(target=handle_client, args=(conn, addr, player_id), daemon=True)
        t.start()

if __name__ == "__main__":
    main()