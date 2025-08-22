import pygame
import socket
import threading
import time
import math
import pickle
import sys
player_id = 1

players = {}
bullets_images = []

client_socket = None

def receive_data():
    global players, bullets, time_remaining, players_remaining, lavaY

    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break
            msg = pickle.loads(data)
            if "action" in msg:
                if msg["action"] == "server_full":
                    pygame.quit()
                    sys.exit()

            if "players" in msg and "bullets" in msg:
                with lock:
                    players = msg["players"]
                    bullets = msg["bullets"]
                    time_remaining = msg.get("time_left", 300)
                    players_remaining = len(players)
                    for pid, pdata in players.items():
                       if pdata["is_dead"] == True:
                          players_remaining -= 1
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
    sorted_players = sorted(players.items(), key=lambda p: p[1]["kills"], reverse=True)
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
font1 = pygame.font.SysFont("Cascadia Code", 20)
font2 = pygame.font.SysFont("Cascadia Code", 30)
font3 = pygame.font.SysFont("Cascadia Code", 40)
font4 = pygame.font.SysFont("Cascadia Code", 50)
font5 = pygame.font.SysFont("Cascadia Code", 65)
font6 = pygame.font.SysFont("Cascadia Code", 100)
display = pygame.display.set_mode((1920, 1080))
gamestatus = 0
customization = 0
playergravity = 25
bullet_shooting_time = time.time()
bullets_remaining = 100
speedX = 0
speedY = 0
speed1 = 2
positionX = 1000
positionY = 700
time_remaining = 300
players_remaining = 0
lavaY = 950
active_bullets = [] 
bullet_speedX = 5
bulletpositionX = -1000
bulletpositionY = -1000
health = 40
healthtype = 1
bullettype = 1
multibullettype = 1
nuketype = 1
shieldtype = 1
shieldtime = 0
shieldduration = 10
trackertype = 1
ancientbullettype = 1
blastertype = 1
equipped_gun_type = 1
bulletkey = pygame.K_1
multibulletkey = pygame.K_2
nukeactive = False
nukekey = pygame.K_3
shieldactive = False
shieldkey = pygame.K_4
trackeractive = False
trackerkey = pygame.K_5
ancientbulletactive = False
ancientbulletkey = pygame.K_6
blasteractive = False
blasterkey = pygame.K_7
element = "Earth"
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
"Gray": "#777777",
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
colors_names = [
    "Red", "Orange", "Yellow", "Green", "Teal", "Blue", 
    "Purple", "Pink", "Brown", "White", "Black", 
    "Bronze", "Silver", "Gold", "Diamond"
]

tank_types = ["Earth", "Electric", "Fire", "Grass", "Ice", "Plasma", "Water", "Wind"]
levels = ["One", "Two", "Three", "Four", "Five"]

bullets_images = {}
for t in tank_types:
    bullets_images[t] = {}
    for level in levels:
        filename = f"Bullets/{t}Bullets/{t}BulletLevel{level}.png"
        bullet_image = pygame.image.load(filename)
        scaled_bullet = pygame.transform.scale(bullet_image, (50, 50))
        bullets_images[t][level] = scaled_bullet
equipped_bullet = bullets_images["Earth"]["One"]

nukes = {}
for t in tank_types:
    nukes[t] = {}
    for level in levels:
        filename = f"Nukes/{t}Nukes/{t}NukeLevel{level}.png"
        nuke_image = pygame.image.load(filename)
        scaled_nuke = pygame.transform.scale(nuke_image, (100, 100))
        nukes[t][level] = scaled_nuke
equipped_nuke = nukes["Earth"]["One"]

shields = {}
for t in tank_types:
    shields[t] = {}
    for level in levels:
        filename = f"Shields/{t}Shields/{t}ShieldLevel{level}.png"
        shield_image = pygame.image.load(filename)
        scaled_shield = pygame.transform.scale(shield_image, (75, 75))
        shields[t][level] = scaled_shield
equipped_shield = shields["Earth"]["One"]

trackers = {}
for t in tank_types:
    trackers[t] = {}
    for level in levels:
        filename = f"Trackers/{t}Trackers/{t}TrackerLevel{level}.png"
        tracker_image = pygame.image.load(filename)
        scaled_tracker = pygame.transform.scale(tracker_image, (50, 50))
        trackers[t][level] = scaled_tracker
equipped_tracker = trackers["Earth"]["One"]

ancient_bullets = {}
for t in tank_types:
    ancient_bullets[t] = {}
    for level in levels:
        filename = f"AncientBullets/{t}AncientBullets/{t}AncientBulletLevel{level}.png"
        ancient_bullet_image = pygame.image.load(filename)
        scaled_ancient_bullet = pygame.transform.scale(ancient_bullet_image, (50, 50))
        ancient_bullets[t][level] = scaled_ancient_bullet
equipped_ancient_bullet = ancient_bullets["Earth"]["One"]

blasters = {}
for t in tank_types:
    blasters[t] = {}
    for level in levels:
        filename = f"Blasters/{t}Blasters/{t}BlasterLevel{level}.png"
        blaster_image = pygame.image.load(filename)
        scaled_blaster = pygame.transform.scale(blaster_image, (50, 50))
        blasters[t][level] = scaled_blaster
equipped_blaster = blasters["Earth"]["One"]

categories = [
    "DefaultGuns", "ShortGuns", "LongGuns", "SpikeGuns",
    "BladeGuns", "AncientGuns", "ModernGuns"
]
guns = {}
for category in categories:
    guns[category] = {}
    for t in tank_types:
        filename = f"Guns/{category}/{t}{category[:-4]}Gun.png"
        gun_image = pygame.image.load(filename)
        scaled_gun = pygame.transform.scale(gun_image, (50, 50))
        guns[category][t] = scaled_gun
equipped_gun = guns[categories[equipped_gun_type]][element]

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
#healthbars[1][40]

levels_icons = {}
for i in range(0, 10):
  levels_icons[i] = pygame.image.load(f"LevelIcons/Levels{i * 10 + 1}-{i * 10 + 10}.png")
  levels_icons[i] = pygame.transform.scale(levels_icons[i], (100, 100))
levels_icons[10] = pygame.image.load("LevelIcons/Level100.png")
levels_icons[10] = pygame.transform.scale(levels_icons[10], (100, 100))

tanks = {}
for t in tank_types:
  tanks[t] = {}
  tanks[t][0] = pygame.image.load(f"Tanks/{t}Tank.png")
  tanks[t][0] = pygame.transform.scale(tanks[t][0], (40, 40))
  tanks[t][1] = pygame.image.load(f"Tanks/{t}Tank.png")
  tanks[t][1] = pygame.transform.scale(tanks[t][1], (150, 150))
equipped_tank = tanks["Earth"][0]
equipped_tank_preview = tanks["Earth"][1]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5555))
client_socket.setblocking(True)
initial_data = client_socket.recv(4096)
handshake = pickle.loads(initial_data)
if handshake.get("action") == "server_full":
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
          if event.key == pygame.K_w or event.key == pygame.K_UP:
            send_to_server({
              "action": "jump",
              "player_id": my_id
            })
          if event.key == bulletkey and time.time() - bullet_shooting_time >= 2 and bullets_remaining >= 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            with lock:
              if my_id in players:
                px, py = players[my_id]["pos"]
              else:
                px, py = (0, 0)
            dir_x = mouse_x - px
            dir_y = mouse_y - py
            angle = -math.degrees(math.atan2(dir_y, dir_x)) - 90
            length = math.hypot(dir_x, dir_y)
            if length != 0:
              dir_x /= length
              dir_y /= length
            send_to_server({
            "action": "shoot",
            "player_id": my_id,
            "dx": dir_x,
            "dy": dir_y,
            "angle": angle
                    })
          if event.key == multibulletkey:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            with lock:
              if my_id in players:
                px, py = players[my_id]["pos"]
              else:
                px, py = (0, 0)
            dir_x = mouse_x - px
            dir_y = mouse_y - py
            angle = -math.degrees(math.atan2(dir_y, dir_x)) - 90
            length = math.hypot(dir_x, dir_y)
            if length != 0:
              dir_x /= length
              dir_y /= length
            send_to_server({
            "action": "multibullet",
            "player_id": my_id,
            "dx": dir_x,
            "dy": dir_y,
            "angle": angle
                    })
          if event.key == nukekey:
            nukeactive = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            with lock:
              if my_id in players:
                px, py = players[my_id]["pos"]
              else:
                px, py = (0, 0)
            dir_x = mouse_x - px
            dir_y = mouse_y - py
            angle = -math.degrees(math.atan2(dir_y, dir_x)) - 90
            length = math.hypot(dir_x, dir_y)
            if length != 0:
              dir_x /= length
              dir_y /= length
            send_to_server({
            "action": "nuke",
            "player_id": my_id,
            "dx": dir_x,
            "dy": dir_y,
            "angle": angle
                    })
          if event.key == shieldkey and shieldactive == False:
            shieldactive = True
            send_to_server({
                 "action": "shield",
                 "player_id": my_id
              })
            shieldtime = time.time()
          if event.key == trackerkey:
            trackeractive = True
          if event.key == ancientbulletkey:
            ancientbulletactive = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            with lock:
              if my_id in players:
                px, py = players[my_id]["pos"]
              else:
                px, py = (0, 0)
            dir_x = mouse_x - px
            dir_y = mouse_y - py
            angle = -math.degrees(math.atan2(dir_y, dir_x)) - 90
            length = math.hypot(dir_x, dir_y)
            if length != 0:
              dir_x /= length
              dir_y /= length
            send_to_server({
            "action": "ancient_bullet",
            "player_id": my_id,
            "dx": dir_x,
            "dy": dir_y,
            "angle": angle
                    })
          if event.key == blasterkey:
            blasteractive = True
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
            
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              element = "Earth"
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              element = "Electric"
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              element = "Fire"
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              element = "Grass"
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              element = "Ice"
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              element = "Plasma"
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              element = "Water"
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              element = "Wind"
            if pos[0] >= 1067 and pos[0] <= 1157 and pos[1] >= 680 and pos[1] <= 770 and gamestatus == 0:
              element = "Earth"
            if pos[0] >= 1219 and pos[0] <= 1309 and pos[1] >= 680 and pos[1] <= 770 and gamestatus == 0:
              element = "Electric"
            if pos[0] >= 1371 and pos[0] <= 1461 and pos[1] >= 680 and pos[1] <= 770 and gamestatus == 0:
              element = "Fire"
            if pos[0] >= 1523 and pos[0] <= 1613 and pos[1] >= 680 and pos[1] <= 770 and gamestatus == 0:
              element = "Grass"
            if pos[0] >= 1067 and pos[0] <= 1157 and pos[1] >= 810 and pos[1] <= 900 and gamestatus == 0:
              element = "Ice"
            if pos[0] >= 1219 and pos[0] <= 1309 and pos[1] >= 810 and pos[1] <= 900 and gamestatus == 0:
              element = "Plasma"
            if pos[0] >= 1371 and pos[0] <= 1461 and pos[1] >= 810 and pos[1] <= 900 and gamestatus == 0:
              element = "Water"
            if pos[0] >= 1523 and pos[0] <= 1613 and pos[1] >= 810 and pos[1] <= 900 and gamestatus == 0:
              element = "Wind"
            send_to_server({
                 "action": "element",
                 "player_id": my_id,
                 "element": element
              })
            
            equipped_tank = tanks[element][0]
            equipped_tank_preview = tanks[element][1]
            equipped_gun = guns[categories[equipped_gun_type - 1]][element]
            equipped_bullet = bullets_images[element]["One"]
            equipped_shield = shields[element]["One"]
            equipped_nuke = nukes[element]["One"]
            equipped_ancient_bullet = ancient_bullets[element]["One"]

            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 0
              damage_gun = 1
              speed_gun = 1
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 1
              damage_gun = 0.75
              speed_gun = 1.25
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 2
              damage_gun = 1.25
              speed_gun = 0.75
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 3
              damage_gun = 1.5
              speed_gun = 1.25
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 4
              damage_gun = 1.25
              speed_gun = 1.5
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 5
              damage_gun = 0.5
              speed_gun = 2
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 1:
              equipped_gun_type = 6
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
      draw_leaderboard(display)
      pygame.draw.rect(display, pygame.Color(colors["Blue"]), (0, lavaY, 2000, 2000))
      pygame.draw.rect(display, pygame.Color(0, 0, 0), (200, 130, 1110, 70))
      pygame.draw.rect(display, pygame.Color(colors["White"]), (205, 135, 1100, 60))
      delta_time = clock.tick(60)/100
      minutes_remaining = int(time_remaining//60)
      seconds_remaining = int(time_remaining % 60)
      text19 = font2.render(f"Time Remaining: {minutes_remaining}:{seconds_remaining:02d}", False, (0, 0, 0))
      text20 = font2.render("Players Remaining: " + str(players_remaining), False, (0, 0, 0))
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
      if shieldactive == True:
        shieldtimedifference = time.time() - shieldtime
        if shieldtimedifference > shieldduration:
          shieldactive = False
          send_to_server({
                 "action": "shield",
                 "player_id": my_id
              })
      with lock:
            for pid, pdata in players.items():
                px, py = pdata["pos"]
                element = pdata["element"]
                health = pdata["health"]
                is_dead = pdata["is_dead"]
                if is_dead:
                    continue
                if pdata["shield"] == True:
                  display.blit(equipped_shield, (px - 28, py - 28))
                display.blit(tanks[pdata["element"]][0], (px - 10, py - 10))
                display.blit(health_bars[1][health], (px - 23, py - 50))

            for b in bullets:
                bx, by = b["x"], b["y"]
                if b["type"] == "bullet":
                  rotated_bullet = pygame.transform.rotate(equipped_bullet, b["angle"])
                  display.blit(rotated_bullet, (bx - 15, by - 10, 8, 8))
                elif b["type"] == "multibullet":
                  rotated_multibullet = pygame.transform.rotate(equipped_bullet, b["angle"])
                  display.blit(rotated_multibullet, (bx - 15, by - 10, 8, 8))
                elif b["type"] == "nuke":
                  rotated_nuke = pygame.transform.rotate(equipped_nuke, b["angle"])
                  display.blit(rotated_nuke, (bx - 45, by - 55, 8, 8))
                elif b["type"] == "ancient_bullet":
                  rotated_ancient_bullet = pygame.transform.rotate(equipped_ancient_bullet, b["angle"])
                  display.blit(rotated_ancient_bullet, (bx - 15, by - 10, 8, 8))

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
                text25 = font2.render("Placement: " + str(players_remaining + 1), False, (0, 0, 0))
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
            if players_remaining == 1 and not players[my_id]["is_dead"]:
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (445, 245, 1010, 610))
                pygame.draw.rect(display, pygame.Color(colors["Gold"]), (450, 250, 1000, 600))
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (475, 655, 280, 60))
                pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (480, 660, 270, 50))
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (475, 755, 230, 60))
                pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (480, 760, 220, 50))
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (1175, 655, 230, 60))
                pygame.draw.rect(display, pygame.Color(colors["Silver"]), (1180, 660, 220, 50))
                pygame.draw.rect(display, pygame.Color(0, 0, 0), (1175, 755, 250, 60))
                pygame.draw.rect(display, pygame.Color(colors["Silver"]), (1180, 760, 240, 50))
                text23 = font2.render("Play another game", False, (0, 0, 0))
                text24 = font2.render("Return to home screen", False, (0, 0, 0))
                text28 = font6.render("You Won", False, (0, 0, 0))
                text29 = font2.render("Placement: 1st", False, (0, 0, 0))
                kills = players[my_id]["kills"]
                text_str = f"Kills: {kills}"
                text26 = font2.render(text_str, True, (0, 0, 0))
                display.blit(text26, (1200, 675))
                display.blit(text28, (750, 350))
                display.blit(text23, (500, 775))
                display.blit(text24, (500, 675))
                display.blit(text29, (1200, 775))
    else:
      display.fill((255, 255, 255))
      pygame.draw.rect(display, pygame.Color(0, 0, 0), (192, 108, 771, 864))
      pygame.draw.rect(display, pygame.Color(colors["Gold"]), (197, 113, 761, 854))
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
      if customization == 0:
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (958, 108, 771, 864))
        pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (963, 113, 761, 854))
        if equipped_tank == tanks["Earth"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 140, 170, 170))
        elif equipped_tank == tanks["Electric"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 140, 170, 170))
        elif equipped_tank == tanks["Fire"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 140, 170, 170))
        elif equipped_tank == tanks["Grass"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1510, 140, 170, 170))
        elif equipped_tank == tanks["Ice"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 310, 170, 170))
        elif equipped_tank == tanks["Plasma"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 310, 170, 170))
        elif equipped_tank == tanks["Water"][0]:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 310, 170, 170))
        elif equipped_tank == tanks["Wind"][0]:
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
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1062, 675, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Brown"]), (1067, 680, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1214, 675, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Yellow"]), (1219, 680, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1366, 675, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Red"]), (1371, 680, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1518, 675, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Green"]), (1523, 680, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1062, 805, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["White"]), (1067, 810, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1214, 805, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Purple"]), (1219, 810, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1366, 805, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Blue"]), (1371, 810, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1518, 805, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Gray"]), (1523, 810, 90, 90))
        display.blit(levels_icons[level_number // 10], (200, 115))
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
        display.blit(equipped_tank_preview, (1265, 490))
      if customization == 1:
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (192, 108, 771, 864))
        pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (197, 113, 761, 854))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (958, 108, 771, 864))
        pygame.draw.rect(display, pygame.Color(colors["Silver"]), (963, 113, 761, 854))
        if equipped_gun_type == 0:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 140, 170, 170))
        elif equipped_gun_type == 1:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 140, 170, 170))
        elif equipped_gun_type == 2:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 140, 170, 170))
        elif equipped_gun_type == 3:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1510, 140, 170, 170))
        elif equipped_gun_type == 4:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 310, 170, 170))
        elif equipped_gun_type == 5:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 310, 170, 170))
        elif equipped_gun_type == 6:
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
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1062, 675, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Brown"]), (1067, 680, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1214, 675, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Yellow"]), (1219, 680, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1366, 675, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Red"]), (1371, 680, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1518, 675, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Green"]), (1523, 680, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1062, 805, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["White"]), (1067, 810, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1214, 805, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Purple"]), (1219, 810, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1366, 805, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Blue"]), (1371, 810, 90, 90))
        pygame.draw.rect(display, pygame.Color(0, 0, 0), (1518, 805, 100, 100))
        pygame.draw.rect(display, pygame.Color(colors["Gray"]), (1523, 810, 90, 90))
        display.blit(levels_icons[level_number // 10], (200, 115))
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
        display.blit(guns["DefaultGuns"][element], (985, 130))
        display.blit(guns["ShortGuns"][element], (1155, 130))
        display.blit(guns["LongGuns"][element], (1325, 130))
        display.blit(guns["SpikeGuns"][element], (1495, 130))
        display.blit(guns["BladeGuns"][element], (985, 300))
        display.blit(guns["AncientGuns"][element], (1155, 300))
        display.blit(guns["ModernGuns"][element], (1325, 300))
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