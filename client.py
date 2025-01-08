import pygame
import pygame.draw_py
import socket
import threading
import time
player_id = 1
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))
def receive_data():
  global positions
  while True:
    try:
      data = client_socket.recv(1024).decode("utf-8")
      positions = eval(data)
    except:
      break
thread = threading.Thread(target = receive_data)
thread.start()
pygame.init()
pygame.font.init()
font1 = pygame.font.SysFont("Lexend", 20)
font2 = pygame.font.SysFont("Lexend", 30)
font3 = pygame.font.SysFont("Lexend", 40)
font4 = pygame.font.SysFont("Lexend", 50)
font5 = pygame.font.SysFont("Lexend", 65)
font6 = pygame.font.SysFont("Lexend", 100)
display = pygame.display.set_mode((1920, 1080))
gamestatus = 0
customization = 0
playergravity = 1
bulletgravity = 0.1
speedX = 0
speedY = 0
speed1 = 1
positionX = 1000
positionY = 700
bulletpositionX = -1000
bulletpositionY = -1000
bulletspeedX = 0
bulletspeedY = 0
lavaY = 950
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
level = 1
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

import pygame

# Define bullet colors and levels
colors_names = [
    "Red", "Orange", "Yellow", "Green", "Teal", "Blue", 
    "Purple", "Pink", "Brown", "White", "Black", 
    "Bronze", "Silver", "Gold", "Diamond"
]
levels = ["One", "Two", "Three", "Four", "Five"]

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
      health_bars[i].append(pygame.image.load("HealthBars/HealthBarsType" + str(i) + "/HealthBars" + str(i) + "-" + str(j) + ".png.png"))
  h += 10
  
levels_one_ten = pygame.image.load("LevelIcons/Levels1-10.png")
levels_one_ten = pygame.transform.scale(levels_one_ten, (100, 100))
levels_eleven_twenty = pygame.image.load("LevelIcons/Levels11-20.png")
levels_eleven_twenty = pygame.transform.scale(levels_eleven_twenty, (100, 100))
levels_twentyone_thirty = pygame.image.load("LevelIcons/Levels21-30.png")
levels_twentyone_thirty = pygame.transform.scale(levels_twentyone_thirty, (100, 100))
levels_thirtyone_forty = pygame.image.load("LevelIcons/Levels31-40.png")
levels_thirtyone_forty = pygame.transform.scale(levels_thirtyone_forty, (100, 100))
levels_fortyone_fifty = pygame.image.load("LevelIcons/Levels41-50.png")
levels_fortyone_fifty = pygame.transform.scale(levels_fortyone_fifty, (100, 100))
levels_fiftyone_sixty = pygame.image.load("LevelIcons/Levels51-60.png")
levels_fiftyone_sixty = pygame.transform.scale(levels_fiftyone_sixty, (100, 100))
levels_sixtyone_seventy = pygame.image.load("LevelIcons/Levels61-70.png")
levels_sixtyone_seventy = pygame.transform.scale(levels_sixtyone_seventy, (100, 100))
levels_seventyone_eighty = pygame.image.load("LevelIcons/Levels71-80.png")
levels_seventyone_eighty = pygame.transform.scale(levels_seventyone_eighty, (100, 100))
levels_eightyone_ninety = pygame.image.load("LevelIcons/Levels81-90.png")
levels_eightyone_ninety = pygame.transform.scale(levels_eightyone_ninety, (100, 100))
levels_ninetyone_hundred = pygame.image.load("LevelIcons/Levels91-100.png")
levels_ninetyone_hundred = pygame.transform.scale(levels_ninetyone_hundred, (100, 100))

lobby_one_map = pygame.image.load("Maps/LobbyMaps/Lobby1.png")
lobby_one_map = pygame.transform.scale(lobby_one_map, (625, 625))
lobby_two_map = pygame.image.load("Maps/LobbyMaps/Lobby2.png")
lobby_two_map = pygame.transform.scale(lobby_two_map, (625, 625))
lobby_three_map = pygame.image.load("Maps/LobbyMaps/Lobby3.png")
lobby_three_map = pygame.transform.scale(lobby_three_map, (625, 625))
lobby_four_map = pygame.image.load("Maps/LobbyMaps/Lobby4.png")
lobby_four_map = pygame.transform.scale(lobby_four_map, (625, 625))
bottom_left_earth_map = pygame.image.load("Maps/EarthMaps/BottomLeftEarthMap.png")
bottom_left_earth_map = pygame.transform.scale(bottom_left_earth_map, (625, 625))
bottom_right_earth_map = pygame.image.load("Maps/EarthMaps/BottomRightEarthMap.png")
bottom_right_earth_map = pygame.transform.scale(bottom_right_earth_map, (625, 625))
top_left_earth_map = pygame.image.load("Maps/EarthMaps/TopLeftEarthMap.png")
top_left_earth_map = pygame.transform.scale(top_left_earth_map, (625, 625))
top_right_earth_map = pygame.image.load("Maps/EarthMaps/TopRightEarthMap.png")
top_right_earth_map = pygame.transform.scale(top_right_earth_map, (625, 625))

red_shield_one = pygame.image.load("Shields/RedShields/RedShieldLevelOne.png")
red_shield_one = pygame.transform.scale(red_shield_one, (60, 60)) 
red_shield_two = pygame.image.load("Shields/RedShields/RedShieldLevelTwo.png")
red_shield_two = pygame.transform.scale(red_shield_two, (60, 60))
red_shield_three = pygame.image.load("Shields/RedShields/RedShieldLevelThree.png")
red_shield_three = pygame.transform.scale(red_shield_three, (60, 60))
red_shield_four = pygame.image.load("Shields/RedShields/RedShieldLevelFour.png")
red_shield_four = pygame.transform.scale(red_shield_four, (60, 60))
red_shield_five = pygame.image.load("Shields/RedShields/RedShieldLevelFive.png")
red_shield_five = pygame.transform.scale(red_shield_five, (60, 60))
orange_shield_one = pygame.image.load("Shields/OrangeShields/OrangeShieldLevelOne.png")
orange_shield_one = pygame.transform.scale(orange_shield_one, (60, 60))
orange_shield_two = pygame.image.load("Shields/OrangeShields/OrangeShieldLevelTwo.png")
orange_shield_two = pygame.transform.scale(orange_shield_two, (60, 60))
orange_shield_three = pygame.image.load("Shields/OrangeShields/OrangeShieldLevelThree.png")
orange_shield_three = pygame.transform.scale(orange_shield_three, (60, 60))
orange_shield_four = pygame.image.load("Shields/OrangeShields/OrangeShieldLevelFour.png")
orange_shield_four = pygame.transform.scale(orange_shield_four, (60, 60))
orange_shield_five = pygame.image.load("Shields/OrangeShields/OrangeShieldLevelFive.png")
orange_shield_five = pygame.transform.scale(orange_shield_five, (60, 60))
yellow_shield_one = pygame.image.load("Shields/YellowShields/YellowShieldLevelOne.png")
yellow_shield_one = pygame.transform.scale(yellow_shield_one, (60, 60))
yellow_shield_two = pygame.image.load("Shields/YellowShields/YellowShieldLevelTwo.png")
yellow_shield_two = pygame.transform.scale(yellow_shield_two, (60, 60))
yellow_shield_three = pygame.image.load("Shields/YellowShields/YellowShieldLevelThree.png")
yellow_shield_three = pygame.transform.scale(yellow_shield_three, (60, 60))
yellow_shield_four = pygame.image.load("Shields/YellowShields/YellowShieldLevelFour.png")
yellow_shield_four = pygame.transform.scale(yellow_shield_four, (60, 60))
yellow_shield_five = pygame.image.load("Shields/YellowShields/YellowShieldLevelFive.png")
yellow_shield_five = pygame.transform.scale(yellow_shield_five, (60, 60))
green_shield_one = pygame.image.load("Shields/GreenShields/GreenShieldLevelOne.png")
green_shield_one = pygame.transform.scale(green_shield_one, (60, 60))
green_shield_two = pygame.image.load("Shields/GreenShields/GreenShieldLevelTwo.png")
green_shield_two = pygame.transform.scale(green_shield_two, (60, 60))
green_shield_three = pygame.image.load("Shields/GreenShields/GreenShieldLevelThree.png")
green_shield_three = pygame.transform.scale(green_shield_three, (60, 60))
green_shield_four = pygame.image.load("Shields/GreenShields/GreenShieldLevelFour.png")
green_shield_four = pygame.transform.scale(green_shield_four, (60, 60))
green_shield_five = pygame.image.load("Shields/GreenShields/GreenShieldLevelFive.png")
green_shield_five = pygame.transform.scale(green_shield_five, (60, 60))
teal_shield_one = pygame.image.load("Shields/TealShields/TealShieldLevelOne.png")
teal_shield_one = pygame.transform.scale(teal_shield_one, (60, 60))
teal_shield_two = pygame.image.load("Shields/TealShields/TealShieldLevelTwo.png")
teal_shield_two = pygame.transform.scale(teal_shield_two, (60, 60))
teal_shield_three = pygame.image.load("Shields/TealShields/TealShieldLevelThree.png")
teal_shield_three = pygame.transform.scale(teal_shield_three, (60, 60))
teal_shield_four = pygame.image.load("Shields/TealShields/TealShieldLevelFour.png")
teal_shield_four = pygame.transform.scale(teal_shield_four, (60, 60))
teal_shield_five = pygame.image.load("Shields/TealShields/TealShieldLevelFive.png")
teal_shield_five = pygame.transform.scale(teal_shield_five, (60, 60))
blue_shield_one = pygame.image.load("Shields/BlueShields/BlueShieldLevelOne.png")
blue_shield_one = pygame.transform.scale(blue_shield_one, (60, 60))
blue_shield_two = pygame.image.load("Shields/BlueShields/BlueShieldLevelTwo.png")
blue_shield_two = pygame.transform.scale(blue_shield_two, (60, 60))
blue_shield_three = pygame.image.load("Shields/BlueShields/BlueShieldLevelThree.png")
blue_shield_three = pygame.transform.scale(blue_shield_three, (60, 60))
blue_shield_four = pygame.image.load("Shields/BlueShields/BlueShieldLevelFour.png")
blue_shield_four = pygame.transform.scale(blue_shield_four, (60, 60))
blue_shield_five = pygame.image.load("Shields/BlueShields/BlueShieldLevelFive.png")
blue_shield_five = pygame.transform.scale(blue_shield_five, (60, 60))
purple_shield_one = pygame.image.load("Shields/PurpleShields/PurpleShieldLevelOne.png")
purple_shield_one = pygame.transform.scale(purple_shield_one, (60, 60))
purple_shield_two = pygame.image.load("Shields/PurpleShields/PurpleShieldLevelTwo.png")
purple_shield_two = pygame.transform.scale(purple_shield_two, (60, 60))
purple_shield_three = pygame.image.load("Shields/PurpleShields/PurpleShieldLevelThree.png")
purple_shield_three = pygame.transform.scale(purple_shield_three, (60, 60))
purple_shield_four = pygame.image.load("Shields/PurpleShields/PurpleShieldLevelFour.png")
purple_shield_four = pygame.transform.scale(purple_shield_four, (60, 60))
purple_shield_five = pygame.image.load("Shields/PurpleShields/PurpleShieldLevelFive.png")
purple_shield_five = pygame.transform.scale(purple_shield_five, (60, 60))
pink_shield_one = pygame.image.load("Shields/PinkShields/PinkShieldLevelOne.png")
pink_shield_one = pygame.transform.scale(pink_shield_one, (60, 60))
pink_shield_two = pygame.image.load("Shields/PinkShields/PinkShieldLevelTwo.png")
pink_shield_two = pygame.transform.scale(pink_shield_two, (60, 60))
pink_shield_three = pygame.image.load("Shields/PinkShields/PinkShieldLevelThree.png")
pink_shield_three = pygame.transform.scale(pink_shield_three, (60, 60))
pink_shield_four = pygame.image.load("Shields/PinkShields/PinkShieldLevelFour.png")
pink_shield_four = pygame.transform.scale(pink_shield_four, (60, 60))
pink_shield_five = pygame.image.load("Shields/PinkShields/PinkShieldLevelFive.png")
pink_shield_five = pygame.transform.scale(pink_shield_five, (60, 60))
brown_shield_one = pygame.image.load("Shields/BrownShields/BrownShieldLevelOne.png")
brown_shield_one = pygame.transform.scale(brown_shield_one, (60, 60))
brown_shield_two = pygame.image.load("Shields/BrownShields/BrownShieldLevelTwo.png")
brown_shield_two = pygame.transform.scale(brown_shield_two, (60, 60))
brown_shield_three = pygame.image.load("Shields/BrownShields/BrownShieldLevelThree.png")
brown_shield_three = pygame.transform.scale(brown_shield_three, (60, 60))
brown_shield_four = pygame.image.load("Shields/BrownShields/BrownShieldLevelFour.png")
brown_shield_four = pygame.transform.scale(brown_shield_four, (60, 60))
brown_shield_five = pygame.image.load("Shields/BrownShields/BrownShieldLevelFive.png")
brown_shield_five = pygame.transform.scale(brown_shield_five, (60, 60))
white_shield_one = pygame.image.load("Shields/WhiteShields/WhiteShieldLevelOne.png")
white_shield_one = pygame.transform.scale(white_shield_one, (60, 60))
white_shield_two = pygame.image.load("Shields/WhiteShields/WhiteShieldLevelTwo.png")
white_shield_two = pygame.transform.scale(white_shield_two, (60, 60))
white_shield_three = pygame.image.load("Shields/WhiteShields/WhiteShieldLevelThree.png")
white_shield_three = pygame.transform.scale(white_shield_three, (60, 60))
white_shield_four = pygame.image.load("Shields/WhiteShields/WhiteShieldLevelFour.png")
white_shield_four = pygame.transform.scale(white_shield_four, (60, 60))
white_shield_five = pygame.image.load("Shields/WhiteShields/WhiteShieldLevelFive.png")
white_shield_five = pygame.transform.scale(white_shield_five, (60, 60))
black_shield_one = pygame.image.load("Shields/BlackShields/BlackShieldLevelOne.png")
black_shield_one = pygame.transform.scale(black_shield_one, (60, 60))
black_shield_two = pygame.image.load("Shields/BlackShields/BlackShieldLevelTwo.png")
black_shield_two = pygame.transform.scale(black_shield_two, (60, 60))
black_shield_three = pygame.image.load("Shields/BlackShields/BlackShieldLevelThree.png")
black_shield_three = pygame.transform.scale(black_shield_three, (60, 60))
black_shield_four = pygame.image.load("Shields/BlackShields/BlackShieldLevelFour.png")
black_shield_four = pygame.transform.scale(black_shield_four, (60, 60))
black_shield_five = pygame.image.load("Shields/BlackShields/BlackShieldLevelFive.png")
black_shield_five = pygame.transform.scale(black_shield_five, (60, 60))
bronze_shield_one = pygame.image.load("Shields/BronzeShields/BronzeShieldLevelOne.png")
bronze_shield_one = pygame.transform.scale(bronze_shield_one, (60, 60))
bronze_shield_two = pygame.image.load("Shields/BronzeShields/BronzeShieldLevelTwo.png")
bronze_shield_two = pygame.transform.scale(bronze_shield_two, (60, 60))
bronze_shield_three = pygame.image.load("Shields/BronzeShields/BronzeShieldLevelThree.png")
bronze_shield_three = pygame.transform.scale(bronze_shield_three, (60, 60))
bronze_shield_four = pygame.image.load("Shields/BronzeShields/BronzeShieldLevelFour.png")
bronze_shield_four = pygame.transform.scale(bronze_shield_four, (60, 60))
bronze_shield_five = pygame.image.load("Shields/BronzeShields/BronzeShieldLevelFive.png")
bronze_shield_five = pygame.transform.scale(bronze_shield_five, (60, 60))
silver_shield_one = pygame.image.load("Shields/SilverShields/SilverShieldLevelOne.png")
silver_shield_one = pygame.transform.scale(silver_shield_one, (60, 60))
silver_shield_two = pygame.image.load("Shields/SilverShields/SilverShieldLevelTwo.png")
silver_shield_two = pygame.transform.scale(silver_shield_two, (60, 60))
silver_shield_three = pygame.image.load("Shields/SilverShields/SilverShieldLevelThree.png")
silver_shield_three = pygame.transform.scale(silver_shield_three, (60, 60))
silver_shield_four = pygame.image.load("Shields/SilverShields/SilverShieldLevelFour.png")
silver_shield_four = pygame.transform.scale(silver_shield_four, (60, 60))
silver_shield_five = pygame.image.load("Shields/SilverShields/SilverShieldLevelFive.png")
silver_shield_five = pygame.transform.scale(silver_shield_five, (60, 60))
gold_shield_one = pygame.image.load("Shields/GoldShields/GoldShieldLevelOne.png")
gold_shield_one = pygame.transform.scale(gold_shield_one, (60, 60))
gold_shield_two = pygame.image.load("Shields/GoldShields/GoldShieldLevelTwo.png")
gold_shield_two = pygame.transform.scale(gold_shield_two, (60, 60))
gold_shield_three = pygame.image.load("Shields/GoldShields/GoldShieldLevelThree.png")
gold_shield_three = pygame.transform.scale(gold_shield_three, (60, 60))
gold_shield_four = pygame.image.load("Shields/GoldShields/GoldShieldLevelFour.png")
gold_shield_four = pygame.transform.scale(gold_shield_four, (60, 60))
gold_shield_five = pygame.image.load("Shields/GoldShields/GoldShieldLevelFive.png")
gold_shield_five = pygame.transform.scale(gold_shield_five, (60, 60))
diamond_shield_one = pygame.image.load("Shields/DiamondShields/DiamondShieldLevelOne.png")
diamond_shield_one = pygame.transform.scale(diamond_shield_one, (60, 60))
diamond_shield_two = pygame.image.load("Shields/DiamondShields/DiamondShieldLevelTwo.png")
diamond_shield_two = pygame.transform.scale(diamond_shield_two, (60, 60))
diamond_shield_three = pygame.image.load("Shields/DiamondShields/DiamondShieldLevelThree.png")
diamond_shield_three = pygame.transform.scale(diamond_shield_three, (60, 60))
diamond_shield_four = pygame.image.load("Shields/DiamondShields/DiamondShieldLevelFour.png")
diamond_shield_four = pygame.transform.scale(diamond_shield_four, (60, 60))
diamond_shield_five = pygame.image.load("Shields/DiamondShields/DiamondShieldLevelFive.png")
diamond_shield_five = pygame.transform.scale(diamond_shield_five, (60, 60))

equippedshield = red_shield_one

earthtank = pygame.image.load("Tanks/EarthTank.png")
earthtank = pygame.transform.scale(earthtank, (40, 40))
electrictank = pygame.image.load("Tanks/ElectricTank.png")
electrictank = pygame.transform.scale(electrictank, (40, 40))
firetank = pygame.image.load("Tanks/FireTank.png")
firetank = pygame.transform.scale(firetank, (40, 40))
grasstank = pygame.image.load("Tanks/GrassTank.png")
grasstank = pygame.transform.scale(grasstank, (40, 40))
icetank = pygame.image.load("Tanks/IceTank.png")
icetank = pygame.transform.scale(icetank, (40, 40))
plasmatank = pygame.image.load("Tanks/PlasmaTank.png")
plasmatank = pygame.transform.scale(plasmatank, (40, 40))
watertank = pygame.image.load("Tanks/WaterTank.png")
watertank = pygame.transform.scale(watertank, (40, 40))
windtank = pygame.image.load("Tanks/WindTank.png")
windtank = pygame.transform.scale(windtank, (40, 40))
earthtankpreview = pygame.image.load("Tanks/EarthTank.png")
earthtankpreview = pygame.transform.scale(earthtankpreview, (150, 150))
electrictankpreview = pygame.image.load("Tanks/ElectricTank.png")
electrictankpreview = pygame.transform.scale(electrictankpreview, (150, 150))
firetankpreview = pygame.image.load("Tanks/FireTank.png")
firetankpreview = pygame.transform.scale(firetankpreview, (150, 150))
grasstankpreview = pygame.image.load("Tanks/GrassTank.png")
grasstankpreview = pygame.transform.scale(grasstankpreview, (150, 150))
icetankpreview = pygame.image.load("Tanks/IceTank.png")
icetankpreview = pygame.transform.scale(icetankpreview, (150, 150))
plasmatankpreview = pygame.image.load("Tanks/PlasmaTank.png")
plasmatankpreview = pygame.transform.scale(plasmatankpreview, (150, 150))
watertankpreview = pygame.image.load("Tanks/WaterTank.png")
watertankpreview = pygame.transform.scale(watertankpreview, (150, 150))
windtankpreview = pygame.image.load("Tanks/WindTank.png")
windtankpreview = pygame.transform.scale(windtankpreview, (150, 150))

equippedtank = earthtank
equippedtankpreview = earthtankpreview


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
          if event.key == bulletkey:
            bulletactive = True
            shieldactive = False
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
              bulletspeedX = 5
              bulletspeedY = -5
              if bulletpositionX > -100 and bulletpositionY > -100:
                bulletspeedY - bulletgravity
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              equippedtank = earthtank
              equippedtankpreview = earthtankpreview
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              equippedtank = electrictank
              equippedtankpreview = electrictankpreview
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              equippedtank = firetank
              equippedtankpreview = firetankpreview
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 150 and pos[1] <= 300 and gamestatus == 0 and customization == 0:
              equippedtank = grasstank
              equippedtankpreview = grasstankpreview
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              equippedtank = icetank
              equippedtankpreview = icetankpreview
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              equippedtank = plasmatank
              equippedtankpreview = plasmatankpreview
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              equippedtank = watertank
              equippedtankpreview = watertankpreview
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 320 and pos[1] <= 470 and gamestatus == 0 and customization == 0:
              equippedtank = windtank
              equippedtankpreview = windtankpreview
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
      client_socket.sendall(f"{player_id}, {positionX}, {positionY}".encode("utf-8"))
      display.fill((0, 255, 255))
      display.blit(bottom_left_earth_map, (330, 345))
      display.blit(bottom_right_earth_map, (955, 345))
      display.blit(top_left_earth_map, (330, 110))
      display.blit(top_right_earth_map, (955, 110))
      pygame.draw.rect(display, pygame.Color(colors["Blue"]), (190, lavaY, 1550, 1100))
      lavaY -= 0.06
      if positionY >= lavaY - 35:
        health = 0
        pygame.draw.rect(display, pygame.Color(colors["Silver"]), (400, 200, 1200, 700))
        s = pygame.Surface((1200,700), pygame.SRCALPHA)
        s.set_alpha(128)
        s.fill((255, 255, 255))
        display.blit(s, (400, 200))
        text21 = font4.render("Game Over", False, (0, 0, 0))
        display.blit(text21, (700, 250))
      pygame.draw.rect(display, pygame.Color(0, 0, 0), (200, 130, 610, 70))
      pygame.draw.rect(display, pygame.Color(colors["White"]), (205, 135, 600, 60))
      text19 = font2.render("Time Remaining: 5:00", False, (0, 0, 0))
      text20 = font2.render("Players Remaining: 12", False, (0, 0, 0))
      display.blit(text19, (220, 155))
      display.blit(text20, (470, 155))
      positionY += playergravity
      if positionX >= 300 and positionX <= 1575 and positionY >= 868:
        positionY = 868
      if shieldactive == True:
        shieldtimedifference = time.time() - shieldtime
        if shieldtimedifference > shieldduration:
          shieldactive = False
        else:
          display.blit(equippedshield, (positionX - 10, positionY - 10))
      display.blit(equippedbullet, (bulletpositionX, bulletpositionY))
      bulletpositionX += bulletspeedX
      bulletpositionY += bulletspeedY
      display.blit(health_bars[healthtype][health - 1],(positionX - 12, positionY - 35))
      #for player, (x, y) in positions.items():
        #display.blit(equippedtank, (x, y))
      display.blit(equippedtank,(positionX, positionY))
      positionX += speedX
      positionY += speedY
    else:
      display.fill((255, 255, 255))
      pygame.draw.rect(display, pygame.Color(colors["Gold"]), (0, 0, 960, 972))
      text1 = font3.render("PLAY SOLO", False, pygame.Color(0, 0, 0))
      text2 = font3.render("PLAY RANKED", False, pygame.Color(0, 0, 0))
      text3 = font3.render("PLAY SQUADS", False, pygame.Color(0, 0, 0))
      text4 = font3.render("Damage Buff: X" + str(damage_gun), False, pygame.Color(0, 0, 0))
      text5 = font3.render("Speed Buff: X" + str(speed_gun), False, pygame.Color(0, 0, 0))
      text6 = font3.render("Cash: " + str(cash), False, pygame.Color(0, 0, 0))
      text7 = font3.render(str(level), False, pygame.Color(255, 255, 255))
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
      display.blit(levels_ninetyone_hundred, (200, 115))
      if customization == 0:
        pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (960, 0, 960, 972))
        if equippedtank == earthtank:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 140, 170, 170))
        elif equippedtank == electrictank:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 140, 170, 170))
        elif equippedtank == firetank:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 140, 170, 170))
        elif equippedtank == grasstank:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1510, 140, 170, 170))
        elif equippedtank == icetank:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1000, 310, 170, 170))
        elif equippedtank == plasmatank:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1170, 310, 170, 170))
        elif equippedtank == watertank:
          pygame.draw.rect(display, pygame.Color(255, 255, 255), (1340, 310, 170, 170))
        elif equippedtank == windtank:
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
        display.blit(text7, (243, 153))
        display.blit(text16, (1435, 580))
        display.blit(earthtankpreview, (1010, 150))
        display.blit(electrictankpreview, (1180, 150))
        display.blit(firetankpreview, (1350, 150))
        display.blit(grasstankpreview, (1520, 150))
        display.blit(icetankpreview, (1010, 320))
        display.blit(plasmatankpreview, (1180, 320))
        display.blit(watertankpreview, (1350, 320))
        display.blit(windtankpreview, (1520, 320))
        display.blit(equippedtankpreview, (1265, 490))
      if customization == 1:
        pygame.draw.rect(display, pygame.Color(colors["Silver"]), (960, 0, 960, 972))
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
        display.blit(text7, (243, 153))
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