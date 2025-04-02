#change bullets, flaks, and shields
import pygame
import socket
import threading
import time
import math
import pickle
import sys
player_id = 1

players = {}
bullets = []

client_socket = None

def receive_data():
    global players, bullets, time_remaining, lavaY

    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break
            msg = pickle.loads(data)
            # Special messages (server_full, handshake, etc.)
            if "action" in msg:
                if msg["action"] == "server_full":
                    print("Server is full. Exiting.")
                    pygame.quit()
                    sys.exit()

            # Normal game state broadcast
            if "players" in msg and "bullets" in msg:
                with lock:
                    players = msg["players"]
                    bullets = msg["bullets"]
                    time_remaining = msg.get("time_left", 300)
                    lavaY = msg.get("lavaY")
        except:
            break

def send_to_server(message_dict):
    try:
        data = pickle.dumps(message_dict)
        client_socket.sendall(data)
    except:
        pass

def draw_leaderboard(screen):
    """
    Draw a simple leaderboard in the top-right corner,
    listing all players by kills descending, or by ID for a simpler approach.
    """
    # Sort players by kills descending
    sorted_players = sorted(players.items(), key=lambda p: p[1]["kills"], reverse=True)
    # Start from some top-right position
    x_start = 200
    y_start = 200
    line_height = 30

    label = font2.render("Leaderboard", True, (255,255,255))
    screen.blit(label, (x_start, y_start))
    y_offset = y_start + line_height

    for pid, pdata in sorted_players:
        kills = pdata["kills"]
        text_str = f"Player {pid}: {kills} kills"
        text_surf = font2.render(text_str, True, (255, 255, 255))
        screen.blit(text_surf, (x_start, y_offset))
        y_offset += line_height

lock = threading.Lock()
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("Lexend", 20)
font2 = pygame.font.SysFont("Lexend", 30)
font3 = pygame.font.SysFont("Lexend", 40)
font4 = pygame.font.SysFont("Lexend", 50)
font5 = pygame.font.SysFont("Lexend", 65)
font6 = pygame.font.SysFont("Lexend", 100)
display = pygame.display.set_mode((1920, 1080))
gamestatus = 0
customization = 0
playergravity = 25
bulletgravity = 4
bullet_shooting_time = time.time()
bullets_remaining = 100
speedX = 0
speedY = 0
speed1 = 1
positionX = 1000
positionY = 700
time_remaining = 300
lavaY = 950
active_bullets = []
bullet_speedX = 5
bullet_gravity = 0.2
bulletpositionX = -1000
bulletpositionY = -1000
health = 40
healthtype = 1
bullettype = 1
rapidfiretype = 1
shieldtype = 1
shieldtime = 0
shieldduration = 10
minetype = 1
nuketype = 1
homingtype = 1
ancientbullettype = 1
flaktype = 1
equipped_gun_type = 1
bulletactive = True
bulletkey = pygame.K_1
rapidfireactive = False
rapidfirekey = pygame.K_2
shieldactive = False
shieldkey = pygame.K_3
mineactive = False
minekey = pygame.K_4
nukeactive = False
nukekey = pygame.K_5
homingactive = False
homingkey = pygame.K_6
ancientbulletactive = False
ancientbulletkey = pygame.K_7
flakactive = False
flakkey = pygame.K_8
level_number = 1
level_number_positionX = 243
xp = 0
signed_in = False
damage_gun = 1
speed_gun = 1
signing_up = False
logging_in = False
username_text = ""
password_text = ""
password_text_hide = ""
username_typing = False 
password_typing = False
cash = 0
colors = {"Red": "#ff0000",
"Orange": "#ff9600",
"Yellow": "#fff000",
"Green": "#22ff00",
"Teal": "#00ffff",
"Blue": "#0030ff",
"Purple": "#8c00ff",
"Pink": "#fc00ff",
"Brown": "#884a00",
"White": "#eeeeee",
"Black": "#444444",
"Bronze": "#b55a00",
"Light Bronze": "#cd7f32",
"Silver": "#777777",
"Light Silver": "#c0c0c0",
"Gold": "#ffc300",
"Light Gold": "#ffe290",
"Diamond": "#99ebff",
"Light Diamond": "#b9f2ff",
}


# Define bullet colors and levels
colors_names = [
    "Red", "Orange", "Yellow", "Green", "Teal", "Blue", 
    "Purple", "Pink", "Brown", "White", "Black", 
    "Bronze", "Silver", "Gold", "Diamond"
]
# Define tank/material types
tank_types = ["Earth", "Electric", "Fire", "Grass", "Ice", "Plasma", "Water", "Wind"]

levels = ["One", "Two", "Three", "Four", "Five"]

# Dictionary to store ancient bullets
ancient_bullets = {}

# Load and scale ancient bullets
for t in tank_types:
    ancient_bullets[t] = {}
    for level in levels:
        filename = f"AncientBullets/{t}AncientBullets/{t}AncientBulletLevel{level}.png"
        ancient_bullet_image = pygame.image.load(filename)
        scaled_ancient_bullet = pygame.transform.scale(ancient_bullet_image, (200, 200))
        ancient_bullets[t][level] = scaled_ancient_bullet

# Dictionary to store bullets
bullets = {}

# Load and scale bullets
for color in colors_names:
    bullets[color] = {}
    for level in levels:
        filename = f"Bullets/{color}Bullets/{color}BulletLevel{level}.png"
        bullet_image = pygame.image.load(filename)
        scaled_bullet = pygame.transform.scale(bullet_image, (30, 30))
        bullets[color][level] = scaled_bullet

equippedbullet = bullets["Red"]["One"]

# Dictionary to store flaks
flaks = {}

# Load and scale flaks
for color in colors_names:
    flaks[color] = {}
    for level in levels:
        filename = f"Flaks/{color}Flaks/{color}FlakLevel{level}.png"
        flak_image = pygame.image.load(filename)
        scaled_flak = pygame.transform.scale(flak_image, (200, 200))
        flaks[color][level] = scaled_flak

# Example of equipping a specific flak
equipped_flak = flaks["Red"]["One"]

categories = [
    "DefaultGuns", "ShortGuns", "LongGuns", "SpikeGuns",
    "BladeGuns", "AncientGuns", "ModernGuns"
]

# Dictionary to store guns
guns = {}

# Load and scale guns
for category in categories:
    guns[category] = {}
    for color in colors_names:
        filename = f"Guns/{category}/{color}{category[:-4]}Gun.png"
        gun_image = pygame.image.load(filename)
        scaled_gun = pygame.transform.scale(gun_image, (200, 200))
        guns[category][color] = scaled_gun

# Example of equipping a gun
equipped_gun = guns["DefaultGuns"]["Red"]


health_bars = {
1: [],
2: [],
3: []
}
h = 40
for i in range(1, 4):
  for j in range(0, h + 1):
      health_bars[i].append(pygame.image.load("HealthBars/HealthBarsType" + str(i) + "/HealthBars" + str(i) + "-" + str(j) + ".png"))
  h += 10
  
# Dictionary to store homings
homings = {}

# Load and scale homings
for t in tank_types:
    homings[t] = {}
    for level in levels:
        filename = f"Homings/{t}Homings/{t}HomingLevel{level}.png"
        homing_image = pygame.image.load(filename)
        scaled_homing = pygame.transform.scale(homing_image, (200, 200))
        homings[t][level] = scaled_homing

levels_icons = {}
for i in range(0, 10):
  levels_icons[i] = pygame.image.load(f"LevelIcons/Levels{i * 10 + 1}-{i * 10 + 10}.png")
  levels_icons[i] = pygame.transform.scale(levels_icons[i], (100, 100))
levels_icons[10] = pygame.image.load("LevelIcons/Level100.png")
levels_icons[10] = pygame.transform.scale(levels_icons[10], (100, 100))

lobby_maps = {}

for i in range(1, 5):
  lobby_maps[i] = pygame.image.load(f"Maps/LobbyMaps/Lobby{i}.png")
  lobby_maps[i] = pygame.transform.scale(lobby_maps[i], (625, 625))

bottom_left_earth_map = pygame.image.load("Maps/EarthMaps/BottomLeftEarthMap.png")
bottom_left_earth_map = pygame.transform.scale(bottom_left_earth_map, (625, 625))
bottom_right_earth_map = pygame.image.load("Maps/EarthMaps/BottomRightEarthMap.png")
bottom_right_earth_map = pygame.transform.scale(bottom_right_earth_map, (625, 625))
top_left_earth_map = pygame.image.load("Maps/EarthMaps/TopLeftEarthMap.png")
top_left_earth_map = pygame.transform.scale(top_left_earth_map, (625, 625))
top_right_earth_map = pygame.image.load("Maps/EarthMaps/TopRightEarthMap.png")
top_right_earth_map = pygame.transform.scale(top_right_earth_map, (625, 625))

# Dictionary to store nukes
nukes = {}

# Load and scale nukes
for t in tank_types:
    nukes[t] = {}
    for level in levels:
        filename = f"Nukes/{t}Nukes/{t}NukeLevel{level}.png"
        nuke_image = pygame.image.load(filename)
        scaled_nuke = pygame.transform.scale(nuke_image, (200, 200))
        nukes[t][level] = scaled_nuke

# Dictionary to store rapidfires
rapidfires = {}

# Load and scale rapidfires
for t in tank_types:
    rapidfires[t] = {}
    for level in levels:
        filename = f"Rapidfires/{t}Rapidfires/{t}RapidfireLevel{level}.png"
        rapidfire_image = pygame.image.load(filename)
        scaled_rapidfire = pygame.transform.scale(rapidfire_image, (200, 200))
        rapidfires[t][level] = scaled_rapidfire

# Example of equipping a specific rapidfire
equipped_rapidfire = rapidfires["Earth"]["One"]

shields = {}

# Load and scale shields
for color in colors_names:
    shields[color] = {}
    for level in levels:
        filename = f"Shields/{color}Shields/{color}ShieldLevel{level}.png"
        shield_image = pygame.image.load(filename)
        scaled_shield = pygame.transform.scale(shield_image, (60, 60))
        shields[color][level] = scaled_shield

equippedshield = shields["Red"]["One"]

tanks = {}
for t in tank_types:
  tanks[t] = {}
  tanks[t][0] = pygame.image.load(f"Tanks/{t}Tank.png")
  tanks[t][0] = pygame.transform.scale(tanks[t][0], (40, 40))
  tanks[t][1] = pygame.image.load(f"Tanks/{t}Tank.png")
  tanks[t][1] = pygame.transform.scale(tanks[t][1], (150, 150))

equippedtank = tanks["Earth"][0]
equippedtankpreview = tanks["Earth"][1]

# Receive initial handshake
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5555))
client_socket.setblocking(True)

initial_data = client_socket.recv(4096)
handshake = pickle.loads(initial_data)

if handshake.get("action") == "server_full":
  print("Server is full. Exiting.")
  client_socket.close()
if handshake.get("action") == "handshake":
  my_id = handshake.get("player_id")
  print(f"[HANDSHAKE] My ID is {my_id}")
else:
  print("Did not receive a proper handshake. Exiting.")
  client_socket.close()

threading.Thread(target=receive_data, daemon=True).start()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            speedX = -speed1
          if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            speedX = speed1
          if event.key == bulletkey and time.time() - bullet_shooting_time >= 2 and bullets_remaining >= 1:
            # Shoot
            mouse_x, mouse_y = pygame.mouse.get_pos()
            with lock:
              if my_id in players:
                px, py = players[my_id]["pos"]
              else:
                px, py = (0, 0)
            dir_x = mouse_x - px
            dir_y = mouse_y - py
            length = math.hypot(dir_x, dir_y)
            if length != 0:
              dir_x /= length
              dir_y /= length
            send_to_server({
            "action": "shoot",
            "player_id": my_id,
            "dx": dir_x,
            "dy": dir_y
                    })
          if event.key == rapidfirekey:
            rapidfireactive = True
          if event.key == shieldkey and shieldactive == False:
            shieldactive = True
            shieldtime = time.time()
          if event.key == minekey:
            mineactive = True
          if event.key == nukekey:
            nukeactive = True
          if event.key == homingkey:
            homingactive = True
          if event.key == ancientbulletkey:
            ancientbulletactive = True
          if event.key == flakkey:
            flakactive = True
          if username_typing == True:
            if event.key == pygame.K_BACKSPACE:
              username_text = username_text[:-1]
            else:
              if len(username_text) < 15:
                username_text += event.unicode
          if password_typing == True:
            if event.key == pygame.K_BACKSPACE:
              password_text = password_text[:-1]
              password_text_hide = password_text_hide[:-1]
            else:
              if len(password_text) < 15:
                password_text += event.unicode
                password_text_hide += "*"
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            speedX = 0
          if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            speedX = 0
          if event.key == pygame.K_w:
            speedY = 0
          if event.key == pygame.K_s:
            speedY = 0
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 370 and pos[0] <= 790 and pos[1] >= 825 and pos[1] <= 915 and gamestatus == 0:
              run = False
            elif pos[0] >= 1455 and pos[0] <= 1705 and pos[1] >= 135 and pos[1] <= 195 and gamestatus == 1:
              run = False
            if pos[0] >= 225 and pos[0] <= 425 and pos[1] >= 350 and pos[1] <= 750 and signed_in == True:
              gamestatus = 1
              print("Solo Game")
            if pos[0] >= 475 and pos[0] <= 675 and pos[1] >= 350 and pos[1] <= 750:
              print("Ranked Game")
            if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 350 and pos[1] <= 750:
              print("Squads Game")
            if pos[0] >= 1430 and pos[0] <= 2000 and pos[1] >= 570 and pos[1] <= 610 and customization == 0:
              customization = 1
            elif pos[0] >= 1430 and pos[0] <= 2000 and pos[1] >= 570 and pos[1] <= 610 and customization == 1:
              customization = 0
            if gamestatus == 1:
              bulletpositionX = positionX + 5
              bulletpositionY = positionY - 35
              bulletspeedX = 1
              bulletspeedY = -1
              if bulletpositionX > -100 and bulletpositionY > -100:
                bulletspeedY += bulletgravity
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              equippedtank = tanks["Earth"][0]
              equippedtankpreview = tanks["Earth"][1]
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              equippedtank = tanks["Electric"][0]
              equippedtankpreview = tanks["Electric"][1]
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              equippedtank = tanks["Fire"][0]
              equippedtankpreview = tanks["Fire"][1]
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              equippedtank = tanks["Grass"][0]
              equippedtankpreview = tanks["Grass"][1]
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              equippedtank = tanks["Ice"][0]
              equippedtankpreview = tanks["Ice"][1]
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              equippedtank = tanks["Plasma"][0]
              equippedtankpreview = tanks["Plasma"][1]
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              equippedtank = tanks["Water"][0]
              equippedtankpreview = tanks["Water"][1]
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              equippedtank = tanks["Wind"][0]
              equippedtankpreview = tanks["Wind"][1]
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 1
              equipped_gun = guns["DefaultGuns"]["Red"]
              damage_gun = 1
              speed_gun = 1
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 2
              equipped_gun = guns["ShortGuns"]["Red"]
              damage_gun = 0.75
              speed_gun = 1.25
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 3
              equipped_gun = guns["LongGuns"]["Red"]
              damage_gun = 1.25
              speed_gun = 0.75
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 4
              equipped_gun = guns["SpikeGuns"]["Red"]
              damage_gun = 1.5
              speed_gun = 1.25
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 5
              equipped_gun = guns["BladeGuns"]["Red"]
              damage_gun = 1.25
              speed_gun = 1.5
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 6
              equipped_gun = guns["AncientGuns"]["Red"]
              damage_gun = 0.5
              speed_gun = 2
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 7
              equipped_gun = guns["ModernGuns"]["Red"]
              damage_gun = 2
              speed_gun = 0.5
            if ((pos[0] >= 315 and pos[0] <= 435 and pos[1] >= 140 and pos[1] <= 190) or (pos[0] >= 445 and pos[0] <= 540 and pos[1] >= 140 and pos[1] <= 190)) and signed_in == False:
              signing_up = True
              logging_in = False
              username_text = ""
              password_text = ""
              username_typing = False
              password_typing = False
              password_text_hide = ""
            if pos[0] >= 615 and pos[0] <= 885 and pos[1] >= 185 and pos[1] <= 215 and (logging_in == True or signing_up == True):
              username_typing = True
            else:
              username_typing = False
            if pos[0] >= 615 and pos[0] <= 885 and pos[1] >= 235 and pos[1] <= 265 and (logging_in == True or signing_up == True):
              password_typing = True
            else:
              password_typing = False
            if pos[0] >= 550 and pos[0] <= 600 and pos[1] >= 140 and pos[1] <= 190 and (logging_in == True or signing_up == True):
              username_text = ""
              password_text = ""
              username_typing = False
              password_typing = False
              password_text_hide = ""
              logging_in = False
              signing_up = False
            if pos[0] >= 890 and pos[0] <= 945 and pos[1] >= 185 and pos[1] <= 265 and (logging_in == True or signing_up == True):
              signed_in = True
    if gamestatus == 1:
      # Send movement if alive
      with lock:
        if my_id in players and not players[my_id]["is_dead"]:
          if speedX != 0 or speedY != 0:
              send_to_server({
                "action": "move",
                "player_id": my_id,
                "dx": speedX,
                "dy": speedY
              })
      display.fill((0, 255, 255))
      display.blit(bottom_left_earth_map, (330, 345))
      display.blit(bottom_right_earth_map, (955, 345))
      display.blit(top_left_earth_map, (330, 110))
      display.blit(top_right_earth_map, (955, 110))
      # Draw leaderboard (top-right)
      draw_leaderboard(display)
      pygame.draw.rect(display, pygame.Color(colors["Blue"]), (0, lavaY, 2000, 2000))
      pygame.draw.rect(display, pygame.Color(0, 0, 0), (200, 130, 1110, 70))
      pygame.draw.rect(display, pygame.Color(colors["White"]), (205, 135, 1100, 60))
      delta_time = clock.tick(60)/100
      minutes_remaining = int(time_remaining//60)
      seconds_remaining = int(time_remaining % 60)
      text19 = font2.render(f"Time Remaining: {minutes_remaining}:{seconds_remaining:02d}", False, (0, 0, 0))
      text20 = font2.render("Players Remaining: 12", False, (0, 0, 0))
      cooldown = time.time() - bullet_shooting_time
      if 2 - cooldown > 0:
        text21 = font2.render(f"Bullet Cooldown: {(2 - cooldown):.1f} seconds", False, (0, 0, 0))
      else:
        text21 = font2.render(f"Bullet Cooldown: 0.0 seconds", False, (0, 0, 0))
      text22 = font2.render(f"Bullets Remaining: {bullets_remaining}", False, (0, 0, 0))
      display.blit(text19, (220, 155))
      display.blit(text20, (470, 155))
      display.blit(text21, (720, 155))
      display.blit(text22, (1070, 155))
      positionY += playergravity * delta_time
      if positionX >= 300 and positionX <= 1575 and positionY >= 868:
        positionY = 868
      if shieldactive == True:
        shieldtimedifference = time.time() - shieldtime
        if shieldtimedifference > shieldduration:
          shieldactive = False
        else:
          display.blit(equippedshield, (positionX - 10, positionY - 10))
      with lock:
            # Draw players
            for pid, pdata in players.items():
                px, py = pdata["pos"]
                #element = pdata["element"]
                health = pdata["health"]
                is_dead = pdata["is_dead"]

                # If dead, optionally skip drawing the player, or draw them differently
                if is_dead:
                    # Let's not draw a dead player at all
                    continue

                # Draw the player's 20x20 rect
                
                # spawn each player's image
                pygame.draw.rect(display, (255, 255, 255), (px - 10, py - 10, 20, 20))

                # Health bar above the player
                
                # instead of health rectangles we have health images
                bar_width = 20
                bar_height = 5
                health_ratio = max(0, health) / 100.0
                pygame.draw.rect(display, (0, 255, 0),
                                 (px - 10, py - 20, int(bar_width * health_ratio), bar_height))
                # Red background for missing portion
                pygame.draw.rect(display, (255, 0, 0),
                                 (px - 10 + int(bar_width * health_ratio),
                                  py - 20,
                                  int(bar_width * (1 - health_ratio)),
                                  bar_height))

            # Draw bullets
            
            # bullet custom images 
            for b in bullets:
                bx, by = b["x"], b["y"]
                pygame.draw.rect(display, (255, 0, 0), (bx - 4, by - 4, 8, 8))

            # If we're dead, show the gray box with "YOU DIED!"
            if my_id in players and players[my_id]["is_dead"]:
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (445, 245, 1010, 610))
                pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (450, 250, 1000, 600))
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (475, 655, 280, 60))
                pygame.draw.rect(display, pygame.Color(colors["Silver"]), (480, 660, 270, 50))
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (475, 755, 230, 60))
                pygame.draw.rect(display, pygame.Color(colors["Silver"]), (480, 760, 220, 50))
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (1175, 655, 230, 60))
                pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1180, 660, 220, 50))
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (1175, 755, 250, 60))
                pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1180, 760, 240, 50))
                text27 = font6.render("Game Over", False, (0, 0, 0))
                text23 = font2.render("Play another game", False, (0, 0, 0))
                text24 = font2.render("Return to home screen", False, (0, 0, 0))
                text25 = font2.render("Placement:", False, (0, 0, 0))
                kills =  players[my_id]["kills"]
                text_str = f"Kills: {kills}"
                text26 = font2.render(text_str, True, (0, 0, 0))
                display.blit(text26, (1200, 675))
                display.blit(text27, (750, 350))
                display.blit(text23, (500, 775))
                display.blit(text24, (500, 675))
                display.blit(text25, (1200, 775))
                if pos[0] >= 480 and pos[0] <= 750 and pos[1] >= 660 and pos[1] <= 710 and gamestatus == 1:
                  gamestatus = 0
    else:
      display.fill((255, 255, 255))
      pygame.draw.rect(display, pygame.Color(colors["Gold"]), (0, 0, 960, 1200))
      text1 = font3.render("PLAY SOLO", False, pygame.Color(0, 0, 0))
      text2 = font3.render("PLAY RANKED", False, pygame.Color(0, 0, 0))
      text3 = font3.render("PLAY SQUADS", False, pygame.Color(0, 0, 0))
      text4 = font3.render("Damage Buff: X" + str(damage_gun), False, pygame.Color(0, 0, 0))
      text5 = font3.render("Speed Buff: X" + str(speed_gun), False, pygame.Color(0, 0, 0))
      text6 = font3.render("Cash: " + str(cash), False, pygame.Color(0, 0, 0))
      text7 = font3.render(str(level_number), False, pygame.Color(255, 255, 255))
      text8 = font3.render("Sign Up", False, (0, 0, 0))
      text9 = font3.render("Log In", False, (0, 0, 0))
      text10 = font3.render("You must be signed in to play a game!", False, (0, 0, 0))
      text11 = font1.render("Username", False, (255, 255, 255))
      text12 = font1.render("Password", False, (255, 255, 255))
      text13 = font5.render("X", False, (0, 0, 0))
      text14 = font6.render(">", False, (0, 0, 0))
      text15 = font2.render("Tank Customization", False, (0, 0, 0))
      text16 = font2.render("Gun Customization", False, (0, 0, 0))
      text17 = font4.render("Exit Game", False, (0, 0, 0))
      text18 = font3.render("Exit Game", False, (0, 0, 0))
      display.blit(levels_icons[level_number // 10], (200, 115))
      if customization == 0:
        pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (960, 0, 1200, 1200))
        if equippedtank == tanks["Earth"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 140, 170, 170))
        elif equippedtank == tanks["Electric"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 140, 170, 170))
        elif equippedtank == tanks["Fire"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 140, 170, 170))
        elif equippedtank == tanks["Grass"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1510, 140, 170, 170))
        elif equippedtank == tanks["Ice"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 310, 170, 170))
        elif equippedtank == tanks["Plasma"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 310, 170, 170))
        elif equippedtank == tanks["Water"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 310, 170, 170))
        elif equippedtank == tanks["Wind"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1510, 310, 170, 170))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (220, 345, 210, 410))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (470, 345, 210, 410))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (720, 345, 210, 410))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1005, 145, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1175, 145, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1345, 145, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1515, 145, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1005, 315, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1175, 315, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1345, 315, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1515, 315, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1005, 485, 670, 465))
        pygame.draw.rect(display, pygame.Color(colors["Blue"]), (225, 350, 200, 400))
        pygame.draw.rect(display, pygame.Color(colors["Yellow"]), (475, 350, 200, 400))
        pygame.draw.rect(display, pygame.Color(colors["Green"]), (725, 350, 200, 400))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1010, 150, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1180, 150, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1350, 150, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1520, 150, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1010, 320, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1180, 320, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1350, 320, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1520, 320, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Light Gold"]), (1010, 490, 660, 455))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1425, 565, 220, 50))
        pygame.draw.rect(display, pygame.Color(colors["Silver"]), (1430, 570, 210, 40))
        display.blit(text1, (250, 525))
        display.blit(text2, (475, 525))
        display.blit(text3, (725, 525))
        display.blit(text6, (1475, 515))
        if level_number > 99:
          level_number_positionX = 227
        elif level_number > 9:
          level_number_positionX = 235
        display.blit(text7, (level_number_positionX, 153))
        display.blit(text16, (1435, 580))
        display.blit(tanks["Earth"][1], (1010, 150))
        display.blit(tanks["Electric"][1], (1180, 150))
        display.blit(tanks["Fire"][1], (1350, 150))
        display.blit(tanks["Grass"][1], (1520, 150))
        display.blit(tanks["Ice"][1], (1010, 320))
        display.blit(tanks["Plasma"][1], (1180, 320))
        display.blit(tanks["Water"][1], (1350, 320))
        display.blit(tanks["Wind"][1], (1520, 320))
        display.blit(equippedtankpreview, (1265, 490))
      if customization == 1:
        pygame.draw.rect(display, pygame.Color(colors["Silver"]), (960, 0, 1200, 1200))
        if equipped_gun_type == 1:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 140, 170, 170))
        elif equipped_gun_type == 2:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 140, 170, 170))
        elif equipped_gun_type == 3:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 140, 170, 170))
        elif equipped_gun_type == 4:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1510, 140, 170, 170))
        elif equipped_gun_type == 5:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 310, 170, 170))
        elif equipped_gun_type == 6:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 310, 170, 170))
        elif equipped_gun_type == 7:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 310, 170, 170))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (220, 345, 210, 410))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (470, 345, 210, 410))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (720, 345, 210, 410))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1005, 145, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1175, 145, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1345, 145, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1515, 145, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1005, 315, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1175, 315, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1345, 315, 160, 160))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1005, 485, 670, 465))
        pygame.draw.rect(display, pygame.Color(colors["Blue"]), (225, 350, 200, 400))
        pygame.draw.rect(display, pygame.Color(colors["Yellow"]), (475, 350, 200, 400))
        pygame.draw.rect(display, pygame.Color(colors["Green"]), (725, 350, 200, 400))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (1010, 150, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (1180, 150, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (1350, 150, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (1520, 150, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (1010, 320, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (1180, 320, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (1350, 320, 150, 150))
        pygame.draw.rect(display, pygame.Color(colors["Light Diamond"]), (1010, 490, 660, 455))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1425, 565, 220, 50))
        pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1430, 570, 210, 40))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1120, 645, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1210, 645, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1300, 645, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1390, 645, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1480, 645, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1120, 735, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1210, 735, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1300, 735, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1390, 735, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1480, 735, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1120, 825, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1210, 825, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1300, 825, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1390, 825, 80, 80))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1480, 825, 80, 80))
        pygame.draw.rect(display, pygame.Color(colors["Red"]), (1125, 650, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Orange"]), (1215, 650, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Yellow"]), (1305, 650, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Green"]), (1395, 650, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Teal"]), (1485, 650, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Blue"]), (1125, 740, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Purple"]), (1215, 740, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Pink"]), (1305, 740, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Brown"]), (1395, 740, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["White"]), (1485, 740, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Black"]), (1125, 830, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1215, 830, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Silver"]), (1305, 830, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Gold"]), (1395, 830, 70, 70))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (1485, 830, 70, 70))
        display.blit(text1, (250, 525))
        display.blit(text2, (475, 525))
        display.blit(text3, (725, 525))
        display.blit(text4, (1020, 505))
        display.blit(text5, (1020, 545))
        display.blit(text6, (1475, 515))
        if level_number > 99:
          level_number_positionX = 227
        elif level_number > 9:
          level_number_positionX = 235
        display.blit(text7, (level_number_positionX, 153))
        display.blit(text15, (1435, 580))
        display.blit(guns["DefaultGuns"]["Red"], (985, 130))
        display.blit(guns["ShortGuns"]["Red"], (1155, 130))
        display.blit(guns["LongGuns"]["Red"], (1325, 130))
        display.blit(guns["SpikeGuns"]["Red"], (1495, 130))
        display.blit(guns["BladeGuns"]["Red"], (985, 300))
        display.blit(guns["AncientGuns"]["Red"], (1155, 300))
        display.blit(guns["ModernGuns"]["Red"], (1325, 300))
        display.blit(equipped_gun, (1250, 470))
      if signed_in == False:
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (313, 138, 124, 54))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (443, 138, 99, 54))
        pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (315, 140, 120, 50))
        pygame.draw.rect(display, pygame.Color(colors["Silver"]), (445, 140, 95, 50))
        display.blit(text8, (320, 150))
        display.blit(text9, (450, 150))
        display.blit(text10, (320, 300))
        if signing_up == True:
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (548, 138, 404, 154))
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (548, 138, 54, 54))
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (613, 183, 274, 34))
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (613, 233, 274, 34))
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (888, 183, 59, 84))
          pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (550, 140, 400, 150))
          pygame.draw.rect(display, pygame.Color(colors["Red"]), (550, 140, 50, 50))
          pygame.draw.rect(display, pygame.Color(colors["Black"]), (615, 185, 270, 30))
          pygame.draw.rect(display, pygame.Color(colors["Black"]), (615, 235, 270, 30))
          pygame.draw.rect(display, pygame.Color(colors["Gold"]), (890, 185, 55, 80))
          text_surface = font2.render(username_text, True, (255, 255, 255))
          text_surface2 = font2.render(password_text_hide, True, (255, 255, 255))
          display.blit(text_surface, (620, 190))
          display.blit(text_surface2, (620, 240))
          display.blit(text11, (615, 170))
          display.blit(text12, (615, 220))
          display.blit(text13, (560, 145))
          display.blit(text14, (900, 185))
        if logging_in == True:
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (548, 138, 404, 154))
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (548, 138, 54, 54))
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (613, 183, 274, 34))
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (613, 233, 274, 34))
          pygame.draw.rect(display, pygame.Color(0, 0, 0), (888, 183, 59, 84))
          pygame.draw.rect(display, pygame.Color(colors["Silver"]), (550, 140, 400, 150))
          pygame.draw.rect(display, pygame.Color(colors["Red"]), (550, 140, 50, 50))
          pygame.draw.rect(display, pygame.Color(colors["Black"]), (615, 185, 270, 30))
          pygame.draw.rect(display, pygame.Color(colors["Black"]), (615, 235, 270, 30))
          pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (890, 185, 55, 80))
          text_surface = font2.render(username_text, True, (255, 255, 255))
          text_surface2 = font2.render(password_text_hide, True, (255, 255, 255))
          display.blit(text_surface, (620, 190))
          display.blit(text_surface2, (620, 240))
          display.blit(text11, (615, 170))
          display.blit(text12, (615, 220))
          display.blit(text13, (560, 145))
          display.blit(text14, (900, 185))
      else:
        username_surface = font3.render(username_text, True, (0, 0, 0))
        display.blit(username_surface, (300, 153))
    if gamestatus == 0:
      pygame.draw.rect(display, pygame.Color(0, 0, 0), (365, 820, 430, 100))
      pygame.draw.rect(display, pygame.Color(colors["Red"]), (370, 825, 420, 90))
      display.blit(text17, (485, 850))
    elif gamestatus == 1:
      pygame.draw.rect(display, pygame.Color(0, 0, 0), (1450, 130, 260, 70))
      pygame.draw.rect(display, pygame.Color(colors["Red"]), (1455, 135, 250, 60))
      display.blit(text18, (1515, 152.5))
    pygame.display.flip()