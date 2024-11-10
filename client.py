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
font1 = pygame.font.SysFont("Lexend", 40)
font2 = pygame.font.SysFont("Lexend", 30)
font3 = pygame.font.SysFont("Lexend", 20)
font4 = pygame.font.SysFont("Lexend", 65)
font5 = pygame.font.SysFont("Lexend", 100)
display = pygame.display.set_mode((1920, 1080))
gamestatus = 0
speedX = 0
speedY = 0
speed1 = 1
positionX = 1000
positionY = 700
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
equippedguntype = 1
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
DamageGun = 1
SpeedGun = 1
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

red_bullet_one = pygame.image.load("Bullets/RedBullets/RedBulletLevelOne.png")
red_bullet_one = pygame.transform.scale(red_bullet_one, (30, 30))
red_bullet_two = pygame.image.load("Bullets/RedBullets/RedBulletLevelTwo.png")
red_bullet_two = pygame.transform.scale(red_bullet_two, (30, 30))
red_bullet_three = pygame.image.load("Bullets/RedBullets/RedBulletLevelThree.png")
red_bullet_three = pygame.transform.scale(red_bullet_three, (30, 30))
red_bullet_four = pygame.image.load("Bullets/RedBullets/RedBulletLevelFour.png")
red_bullet_four = pygame.transform.scale(red_bullet_four, (30, 30))
red_bullet_five = pygame.image.load("Bullets/RedBullets/RedBulletLevelFive.png")
red_bullet_five = pygame.transform.scale(red_bullet_five, (30, 30))
orange_bullet_one = pygame.image.load("Bullets/OrangeBullets/OrangeBulletLevelOne.png")
orange_bullet_one = pygame.transform.scale(orange_bullet_one, (30, 30))
orange_bullet_two = pygame.image.load("Bullets/OrangeBullets/OrangeBulletLevelTwo.png")
orange_bullet_two = pygame.transform.scale(orange_bullet_two, (30, 30))
orange_bullet_three = pygame.image.load("Bullets/OrangeBullets/OrangeBulletLevelThree.png")
orange_bullet_three = pygame.transform.scale(orange_bullet_three, (30, 30))
orange_bullet_four = pygame.image.load("Bullets/OrangeBullets/OrangeBulletLevelFour.png")
orange_bullet_four = pygame.transform.scale(orange_bullet_four, (30, 30))
orange_bullet_five = pygame.image.load("Bullets/OrangeBullets/OrangeBulletLevelFive.png")
orange_bullet_five = pygame.transform.scale(orange_bullet_five, (30, 30))
yellow_bullet_one = pygame.image.load("Bullets/YellowBullets/YellowBulletLevelOne.png")
yellow_bullet_one = pygame.transform.scale(yellow_bullet_one, (30, 30))
yellow_bullet_two = pygame.image.load("Bullets/YellowBullets/YellowBulletLevelTwo.png")
yellow_bullet_two = pygame.transform.scale(yellow_bullet_two, (30, 30))
yellow_bullet_three = pygame.image.load("Bullets/YellowBullets/YellowBulletLevelThree.png")
yellow_bullet_three = pygame.transform.scale(yellow_bullet_three, (30, 30))
yellow_bullet_four = pygame.image.load("Bullets/YellowBullets/YellowBulletLevelFour.png")
yellow_bullet_four = pygame.transform.scale(yellow_bullet_four, (30, 30))
yellow_bullet_five = pygame.image.load("Bullets/YellowBullets/YellowBulletLevelFive.png")
yellow_bullet_five = pygame.transform.scale(yellow_bullet_five, (30, 30))
green_bullet_one = pygame.image.load("Bullets/GreenBullets/GreenBulletLevelOne.png")
green_bullet_one = pygame.transform.scale(green_bullet_one, (30, 30))
green_bullet_two = pygame.image.load("Bullets/GreenBullets/GreenBulletLevelTwo.png")
green_bullet_two = pygame.transform.scale(green_bullet_two, (30, 30))
green_bullet_three = pygame.image.load("Bullets/GreenBullets/GreenBulletLevelThree.png")
green_bullet_three = pygame.transform.scale(green_bullet_three, (30, 30))
green_bullet_four = pygame.image.load("Bullets/GreenBullets/GreenBulletLevelFour.png")
green_bullet_four = pygame.transform.scale(green_bullet_four, (30, 30))
green_bullet_five = pygame.image.load("Bullets/GreenBullets/GreenBulletLevelFive.png")
green_bullet_five = pygame.transform.scale(green_bullet_five, (30, 30))
teal_bullet_one = pygame.image.load("Bullets/TealBullets/TealBulletLevelOne.png")
teal_bullet_one = pygame.transform.scale(teal_bullet_one, (30, 30))
teal_bullet_two = pygame.image.load("Bullets/TealBullets/TealBulletLevelTwo.png")
teal_bullet_two = pygame.transform.scale(teal_bullet_two, (30, 30))
teal_bullet_three = pygame.image.load("Bullets/TealBullets/TealBulletLevelThree.png")
teal_bullet_three = pygame.transform.scale(teal_bullet_three, (30, 30))
teal_bullet_four = pygame.image.load("Bullets/TealBullets/TealBulletLevelFour.png")
teal_bullet_four = pygame.transform.scale(teal_bullet_four, (30, 30))
teal_bullet_five = pygame.image.load("Bullets/TealBullets/TealBulletLevelFive.png")
teal_bullet_five = pygame.transform.scale(teal_bullet_five, (30, 30))
blue_bullet_one = pygame.image.load("Bullets/BlueBullets/BlueBulletLevelOne.png")
blue_bullet_one = pygame.transform.scale(blue_bullet_one, (30, 30))
blue_bullet_two = pygame.image.load("Bullets/BlueBullets/BlueBulletLevelTwo.png")
blue_bullet_two = pygame.transform.scale(blue_bullet_two, (30, 30))
blue_bullet_three = pygame.image.load("Bullets/BlueBullets/BlueBulletLevelThree.png")
blue_bullet_three = pygame.transform.scale(blue_bullet_three, (30, 30))
blue_bullet_four = pygame.image.load("Bullets/BlueBullets/BlueBulletLevelFour.png")
blue_bullet_four = pygame.transform.scale(blue_bullet_four, (30, 30))
blue_bullet_five = pygame.image.load("Bullets/BlueBullets/BlueBulletLevelFive.png")
blue_bullet_five = pygame.transform.scale(blue_bullet_five, (30, 30))
purple_bullet_one = pygame.image.load("Bullets/PurpleBullets/PurpleBulletLevelOne.png")
purple_bullet_one = pygame.transform.scale(purple_bullet_one, (30, 30))
purple_bullet_two = pygame.image.load("Bullets/PurpleBullets/PurpleBulletLevelTwo.png")
purple_bullet_two = pygame.transform.scale(purple_bullet_two, (30, 30))
purple_bullet_three = pygame.image.load("Bullets/PurpleBullets/PurpleBulletLevelThree.png")
purple_bullet_three = pygame.transform.scale(purple_bullet_three, (30, 30))
purple_bullet_four = pygame.image.load("Bullets/PurpleBullets/PurpleBulletLevelFour.png")
purple_bullet_four = pygame.transform.scale(purple_bullet_four, (30, 30))
purple_bullet_five = pygame.image.load("Bullets/PurpleBullets/PurpleBulletLevelFive.png")
purple_bullet_five = pygame.transform.scale(purple_bullet_five, (30, 30))
pink_bullet_one = pygame.image.load("Bullets/PinkBullets/PinkBulletLevelOne.png")
pink_bullet_one = pygame.transform.scale(pink_bullet_one, (30, 30))
pink_bullet_two = pygame.image.load("Bullets/PinkBullets/PinkBulletLevelTwo.png")
pink_bullet_two = pygame.transform.scale(pink_bullet_two, (30, 30))
pink_bullet_three = pygame.image.load("Bullets/PinkBullets/PinkBulletLevelThree.png")
pink_bullet_three = pygame.transform.scale(pink_bullet_three, (30, 30))
pink_bullet_four = pygame.image.load("Bullets/PinkBullets/PinkBulletLevelFour.png")
pink_bullet_four = pygame.transform.scale(pink_bullet_four, (30, 30))
pink_bullet_five = pygame.image.load("Bullets/PinkBullets/PinkBulletLevelFive.png")
pink_bullet_five = pygame.transform.scale(pink_bullet_five, (30, 30))
brown_bullet_one = pygame.image.load("Bullets/BrownBullets/BrownBulletLevelOne.png")
brown_bullet_one = pygame.transform.scale(brown_bullet_one, (30, 30))
brown_bullet_two = pygame.image.load("Bullets/BrownBullets/BrownBulletLevelTwo.png")
brown_bullet_two = pygame.transform.scale(brown_bullet_two, (30, 30))
brown_bullet_three = pygame.image.load("Bullets/BrownBullets/BrownBulletLevelThree.png")
brown_bullet_three = pygame.transform.scale(brown_bullet_three, (30, 30))
brown_bullet_four = pygame.image.load("Bullets/BrownBullets/BrownBulletLevelFour.png")
brown_bullet_four = pygame.transform.scale(brown_bullet_four, (30, 30))
brown_bullet_five = pygame.image.load("Bullets/BrownBullets/BrownBulletLevelFive.png")
brown_bullet_five = pygame.transform.scale(brown_bullet_five, (30, 30))
white_bullet_one = pygame.image.load("Bullets/WhiteBullets/WhiteBulletLevelOne.png")
white_bullet_one = pygame.transform.scale(white_bullet_one, (30, 30))
white_bullet_two = pygame.image.load("Bullets/WhiteBullets/WhiteBulletLevelTwo.png")
white_bullet_two = pygame.transform.scale(white_bullet_two, (30, 30))
white_bullet_three = pygame.image.load("Bullets/WhiteBullets/WhiteBulletLevelThree.png")
white_bullet_three = pygame.transform.scale(white_bullet_three, (30, 30))
white_bullet_four = pygame.image.load("Bullets/WhiteBullets/WhiteBulletLevelFour.png")
white_bullet_four = pygame.transform.scale(white_bullet_four, (30, 30))
white_bullet_five = pygame.image.load("Bullets/WhiteBullets/WhiteBulletLevelFive.png")
white_bullet_five = pygame.transform.scale(white_bullet_five, (30, 30))
black_bullet_one = pygame.image.load("Bullets/BlackBullets/BlackBulletLevelOne.png")
black_bullet_one = pygame.transform.scale(black_bullet_one, (30, 30))
black_bullet_two = pygame.image.load("Bullets/BlackBullets/BlackBulletLevelTwo.png")
black_bullet_two = pygame.transform.scale(black_bullet_two, (30, 30))
black_bullet_three = pygame.image.load("Bullets/BlackBullets/BlackBulletLevelThree.png")
black_bullet_three = pygame.transform.scale(black_bullet_three, (30, 30))
black_bullet_four = pygame.image.load("Bullets/BlackBullets/BlackBulletLevelFour.png")
black_bullet_four = pygame.transform.scale(black_bullet_four, (30, 30))
black_bullet_five = pygame.image.load("Bullets/BlackBullets/BlackBulletLevelFive.png")
black_bullet_five = pygame.transform.scale(black_bullet_five, (30, 30))
bronze_bullet_one = pygame.image.load("Bullets/BronzeBullets/BronzeBulletLevelOne.png")
bronze_bullet_one = pygame.transform.scale(bronze_bullet_one, (30, 30))
bronze_bullet_two = pygame.image.load("Bullets/BronzeBullets/BronzeBulletLevelTwo.png")
bronze_bullet_two = pygame.transform.scale(bronze_bullet_two, (30, 30))
bronze_bullet_three = pygame.image.load("Bullets/BronzeBullets/BronzeBulletLevelThree.png")
bronze_bullet_three = pygame.transform.scale(bronze_bullet_three, (30, 30))
bronze_bullet_four = pygame.image.load("Bullets/BronzeBullets/BronzeBulletLevelFour.png")
bronze_bullet_four = pygame.transform.scale(bronze_bullet_four, (30, 30))
bronze_bullet_five = pygame.image.load("Bullets/BronzeBullets/BronzeBulletLevelFive.png")
bronze_bullet_five = pygame.transform.scale(bronze_bullet_five, (30, 30))
silver_bullet_one = pygame.image.load("Bullets/SilverBullets/SilverBulletLevelOne.png")
silver_bullet_one = pygame.transform.scale(silver_bullet_one, (30, 30))
silver_bullet_two = pygame.image.load("Bullets/SilverBullets/SilverBulletLevelTwo.png")
silver_bullet_two = pygame.transform.scale(silver_bullet_two, (30, 30))
silver_bullet_three = pygame.image.load("Bullets/SilverBullets/SilverBulletLevelThree.png")
silver_bullet_three = pygame.transform.scale(silver_bullet_three, (30, 30))
silver_bullet_four = pygame.image.load("Bullets/SilverBullets/SilverBulletLevelFour.png")
silver_bullet_four = pygame.transform.scale(silver_bullet_four, (30, 30))
silver_bullet_five = pygame.image.load("Bullets/SilverBullets/SilverBulletLevelFive.png")
silver_bullet_five = pygame.transform.scale(silver_bullet_five, (30, 30))
gold_bullet_one = pygame.image.load("Bullets/GoldBullets/GoldBulletLevelOne.png")
gold_bullet_one = pygame.transform.scale(gold_bullet_one, (30, 30))
gold_bullet_two = pygame.image.load("Bullets/GoldBullets/GoldBulletLevelTwo.png")
gold_bullet_two = pygame.transform.scale(gold_bullet_two, (30, 30))
gold_bullet_three = pygame.image.load("Bullets/GoldBullets/GoldBulletLevelThree.png")
gold_bullet_three = pygame.transform.scale(gold_bullet_three, (30, 30))
gold_bullet_four = pygame.image.load("Bullets/GoldBullets/GoldBulletLevelFour.png")
gold_bullet_four = pygame.transform.scale(gold_bullet_four, (30, 30))
gold_bullet_five = pygame.image.load("Bullets/GoldBullets/GoldBulletLevelFive.png")
gold_bullet_five = pygame.transform.scale(gold_bullet_five, (30, 30))
diamond_bullet_one = pygame.image.load("Bullets/DiamondBullets/DiamondBulletLevelOne.png")
diamond_bullet_one = pygame.transform.scale(diamond_bullet_one, (30, 30))
diamond_bullet_two = pygame.image.load("Bullets/DiamondBullets/DiamondBulletLevelTwo.png")
diamond_bullet_two = pygame.transform.scale(diamond_bullet_two, (30, 30))
diamond_bullet_three = pygame.image.load("Bullets/DiamondBullets/DiamondBulletLevelThree.png")
diamond_bullet_three = pygame.transform.scale(diamond_bullet_three, (30, 30))
diamond_bullet_four = pygame.image.load("Bullets/DiamondBullets/DiamondBulletLevelFour.png")
diamond_bullet_four = pygame.transform.scale(diamond_bullet_four, (30, 30))
diamond_bullet_five = pygame.image.load("Bullets/DiamondBullets/DiamondBulletLevelFive.png")
diamond_bullet_five = pygame.transform.scale(diamond_bullet_five, (30, 30))

red_default_gun = pygame.image.load("Guns/DefaultGuns/RedDefaultGun.png")
red_default_gun = pygame.transform.scale(red_default_gun, (200, 200))
orange_default_gun = pygame.image.load("Guns/DefaultGuns/OrangeDefaultGun.png")
orange_default_gun = pygame.transform.scale(orange_default_gun, (200, 200))
yellow_default_gun = pygame.image.load("Guns/DefaultGuns/YellowDefaultGun.png")
yellow_default_gun = pygame.transform.scale(yellow_default_gun, (200, 200))
green_default_gun = pygame.image.load("Guns/DefaultGuns/GreenDefaultGun.png")
green_default_gun = pygame.transform.scale(green_default_gun, (200, 200))
teal_default_gun = pygame.image.load("Guns/DefaultGuns/TealDefaultGun.png")
teal_default_gun = pygame.transform.scale(teal_default_gun, (200, 200))
blue_default_gun = pygame.image.load("Guns/DefaultGuns/BlueDefaultGun.png")
blue_default_gun = pygame.transform.scale(blue_default_gun, (200, 200))
purple_default_gun = pygame.image.load("Guns/DefaultGuns/PurpleDefaultGun.png")
purple_default_gun = pygame.transform.scale(purple_default_gun, (200, 200))
pink_default_gun = pygame.image.load("Guns/DefaultGuns/PinkDefaultGun.png")
pink_default_gun = pygame.transform.scale(pink_default_gun, (200, 200))
brown_default_gun = pygame.image.load("Guns/DefaultGuns/BrownDefaultGun.png")
brown_default_gun = pygame.transform.scale(brown_default_gun, (200, 200))
white_default_gun = pygame.image.load("Guns/DefaultGuns/WhiteDefaultGun.png")
white_default_gun = pygame.transform.scale(white_default_gun, (200, 200))
black_default_gun = pygame.image.load("Guns/DefaultGuns/BlackDefaultGun.png")
black_default_gun = pygame.transform.scale(black_default_gun, (200, 200))
bronze_default_gun = pygame.image.load("Guns/DefaultGuns/BronzeDefaultGun.png")
bronze_default_gun = pygame.transform.scale(bronze_default_gun, (200, 200))
silver_default_gun = pygame.image.load("Guns/DefaultGuns/SilverDefaultGun.png")
silver_default_gun = pygame.transform.scale(silver_default_gun, (200, 200))
gold_default_gun = pygame.image.load("Guns/DefaultGuns/GoldDefaultGun.png")
gold_default_gun = pygame.transform.scale(gold_default_gun, (200, 200))
diamond_default_gun = pygame.image.load("Guns/DefaultGuns/DiamondDefaultGun.png")
diamond_default_gun = pygame.transform.scale(diamond_default_gun, (200, 200))

red_short_gun = pygame.image.load("Guns/ShortGuns/RedShortGun.png")
red_short_gun = pygame.transform.scale(red_short_gun, (200, 200))
orange_short_gun = pygame.image.load("Guns/ShortGuns/OrangeShortGun.png")
orange_short_gun = pygame.transform.scale(orange_short_gun, (200, 200))
yellow_short_gun = pygame.image.load("Guns/ShortGuns/YellowShortGun.png")
yellow_short_gun = pygame.transform.scale(yellow_short_gun, (200, 200))
green_short_gun = pygame.image.load("Guns/ShortGuns/GreenShortGun.png")
green_short_gun = pygame.transform.scale(green_short_gun, (200, 200))
teal_short_gun = pygame.image.load("Guns/ShortGuns/TealShortGun.png")
teal_short_gun = pygame.transform.scale(teal_short_gun, (200, 200))
blue_short_gun = pygame.image.load("Guns/ShortGuns/BlueShortGun.png")
blue_short_gun = pygame.transform.scale(blue_short_gun, (200, 200))
purple_short_gun = pygame.image.load("Guns/ShortGuns/PurpleShortGun.png")
purple_short_gun = pygame.transform.scale(purple_short_gun, (200, 200))
pink_short_gun = pygame.image.load("Guns/ShortGuns/PinkShortGun.png")
pink_short_gun = pygame.transform.scale(pink_short_gun, (200, 200))
brown_short_gun = pygame.image.load("Guns/ShortGuns/BrownShortGun.png")
brown_short_gun = pygame.transform.scale(brown_short_gun, (200, 200))
white_short_gun = pygame.image.load("Guns/ShortGuns/WhiteShortGun.png")
white_short_gun = pygame.transform.scale(white_short_gun, (200, 200))
black_short_gun = pygame.image.load("Guns/ShortGuns/BlackShortGun.png")
black_short_gun = pygame.transform.scale(black_short_gun, (200, 200))
bronze_short_gun = pygame.image.load("Guns/ShortGuns/BronzeShortGun.png")
bronze_short_gun = pygame.transform.scale(bronze_short_gun, (200, 200))
silver_short_gun = pygame.image.load("Guns/ShortGuns/SilverShortGun.png")
silver_short_gun = pygame.transform.scale(silver_short_gun, (200, 200))
gold_short_gun = pygame.image.load("Guns/ShortGuns/GoldShortGun.png")
gold_short_gun = pygame.transform.scale(gold_short_gun, (200, 200))
diamond_short_gun = pygame.image.load("Guns/ShortGuns/DiamondShortGun.png")
diamond_short_gun = pygame.transform.scale(diamond_short_gun, (200, 200))

red_long_gun = pygame.image.load("Guns/LongGuns/RedLongGun.png")
red_long_gun = pygame.transform.scale(red_long_gun, (200, 200))
orange_long_gun = pygame.image.load("Guns/LongGuns/OrangeLongGun.png")
orange_long_gun = pygame.transform.scale(orange_long_gun, (200, 200))
yellow_long_gun = pygame.image.load("Guns/LongGuns/YellowLongGun.png")
yellow_long_gun = pygame.transform.scale(yellow_long_gun, (200, 200))
green_long_gun = pygame.image.load("Guns/LongGuns/GreenLongGun.png")
green_long_gun = pygame.transform.scale(green_long_gun, (200, 200))
teal_long_gun = pygame.image.load("Guns/LongGuns/TealLongGun.png")
teal_long_gun = pygame.transform.scale(teal_long_gun, (200, 200))
blue_long_gun = pygame.image.load("Guns/LongGuns/BlueLongGun.png")
blue_long_gun = pygame.transform.scale(blue_long_gun, (200, 200))
purple_long_gun = pygame.image.load("Guns/LongGuns/PurpleLongGun.png")
purple_long_gun = pygame.transform.scale(purple_long_gun, (200, 200))
pink_long_gun = pygame.image.load("Guns/LongGuns/PinkLongGun.png")
pink_long_gun = pygame.transform.scale(pink_long_gun, (200, 200))
brown_long_gun = pygame.image.load("Guns/LongGuns/BrownLongGun.png")
brown_long_gun = pygame.transform.scale(brown_long_gun, (200, 200))
white_long_gun = pygame.image.load("Guns/LongGuns/WhiteLongGun.png")
white_long_gun = pygame.transform.scale(white_long_gun, (200, 200))
black_long_gun = pygame.image.load("Guns/LongGuns/BlackLongGun.png")
black_long_gun = pygame.transform.scale(black_long_gun, (200, 200))
bronze_long_gun = pygame.image.load("Guns/LongGuns/BronzeLongGun.png")
bronze_long_gun = pygame.transform.scale(bronze_long_gun, (200, 200))
silver_long_gun = pygame.image.load("Guns/LongGuns/SilverLongGun.png")
silver_long_gun = pygame.transform.scale(silver_long_gun, (200, 200))
gold_long_gun = pygame.image.load("Guns/LongGuns/GoldLongGun.png")
gold_long_gun = pygame.transform.scale(gold_long_gun, (200, 200))
diamond_long_gun = pygame.image.load("Guns/LongGuns/DiamondLongGun.png")
diamond_long_gun = pygame.transform.scale(diamond_long_gun, (200, 200))

red_spike_gun = pygame.image.load("Guns/SpikeGuns/RedSpikeGun.png")
red_spike_gun = pygame.transform.scale(red_spike_gun, (200, 200))
orange_spike_gun = pygame.image.load("Guns/SpikeGuns/OrangeSpikeGun.png")
orange_spike_gun = pygame.transform.scale(orange_spike_gun, (200, 200))
yellow_spike_gun = pygame.image.load("Guns/SpikeGuns/YellowSpikeGun.png")
yellow_spike_gun = pygame.transform.scale(yellow_spike_gun, (200, 200))
green_spike_gun = pygame.image.load("Guns/SpikeGuns/GreenSpikeGun.png")
green_spike_gun = pygame.transform.scale(green_spike_gun, (200, 200))
teal_spike_gun = pygame.image.load("Guns/SpikeGuns/TealSpikeGun.png")
teal_spike_gun = pygame.transform.scale(teal_spike_gun, (200, 200))
blue_spike_gun = pygame.image.load("Guns/SpikeGuns/BlueSpikeGun.png")
blue_spike_gun = pygame.transform.scale(blue_spike_gun, (200, 200))
purple_spike_gun = pygame.image.load("Guns/SpikeGuns/PurpleSpikeGun.png")
purple_spike_gun = pygame.transform.scale(purple_spike_gun, (200, 200))
pink_spike_gun = pygame.image.load("Guns/SpikeGuns/PinkSpikeGun.png")
pink_spike_gun = pygame.transform.scale(pink_spike_gun, (200, 200))
brown_spike_gun = pygame.image.load("Guns/SpikeGuns/BrownSpikeGun.png")
brown_spike_gun = pygame.transform.scale(brown_spike_gun, (200, 200))
white_spike_gun = pygame.image.load("Guns/SpikeGuns/WhiteSpikeGun.png")
white_spike_gun = pygame.transform.scale(white_spike_gun, (200, 200))
black_spike_gun = pygame.image.load("Guns/SpikeGuns/BlackSpikeGun.png")
black_spike_gun = pygame.transform.scale(black_spike_gun, (200, 200))
bronze_spike_gun = pygame.image.load("Guns/SpikeGuns/BronzeSpikeGun.png")
bronze_spike_gun = pygame.transform.scale(bronze_spike_gun, (200, 200))
silver_spike_gun = pygame.image.load("Guns/SpikeGuns/SilverSpikeGun.png")
silver_spike_gun = pygame.transform.scale(silver_spike_gun, (200, 200))
gold_spike_gun = pygame.image.load("Guns/SpikeGuns/GoldSpikeGun.png")
gold_spike_gun = pygame.transform.scale(gold_spike_gun, (200, 200))
diamond_spike_gun = pygame.image.load("Guns/SpikeGuns/DiamondSpikeGun.png")
diamond_spike_gun = pygame.transform.scale(diamond_spike_gun, (200, 200))

red_blade_gun = pygame.image.load("Guns/BladeGuns/RedBladeGun.png")
red_blade_gun = pygame.transform.scale(red_blade_gun, (200, 200))
orange_blade_gun = pygame.image.load("Guns/BladeGuns/OrangeBladeGun.png")
orange_blade_gun = pygame.transform.scale(orange_blade_gun, (200, 200))
yellow_blade_gun = pygame.image.load("Guns/BladeGuns/YellowBladeGun.png")
yellow_blade_gun = pygame.transform.scale(yellow_blade_gun, (200, 200))
green_blade_gun = pygame.image.load("Guns/BladeGuns/GreenBladeGun.png")
green_blade_gun = pygame.transform.scale(green_blade_gun, (200, 200))
teal_blade_gun = pygame.image.load("Guns/BladeGuns/TealBladeGun.png")
teal_blade_gun = pygame.transform.scale(teal_blade_gun, (200, 200))
blue_blade_gun = pygame.image.load("Guns/BladeGuns/BlueBladeGun.png")
blue_blade_gun = pygame.transform.scale(blue_blade_gun, (200, 200))
purple_blade_gun = pygame.image.load("Guns/BladeGuns/PurpleBladeGun.png")
purple_blade_gun = pygame.transform.scale(purple_blade_gun, (200, 200))
pink_blade_gun = pygame.image.load("Guns/BladeGuns/PinkBladeGun.png")
pink_blade_gun = pygame.transform.scale(pink_blade_gun, (200, 200))
brown_blade_gun = pygame.image.load("Guns/BladeGuns/BrownBladeGun.png")
brown_blade_gun = pygame.transform.scale(brown_blade_gun, (200, 200))
white_blade_gun = pygame.image.load("Guns/BladeGuns/WhiteBladeGun.png")
white_blade_gun = pygame.transform.scale(white_blade_gun, (200, 200))
black_blade_gun = pygame.image.load("Guns/BladeGuns/BlackBladeGun.png")
black_blade_gun = pygame.transform.scale(black_blade_gun, (200, 200))
bronze_blade_gun = pygame.image.load("Guns/BladeGuns/BronzeBladeGun.png")
bronze_blade_gun = pygame.transform.scale(bronze_blade_gun, (200, 200))
silver_blade_gun = pygame.image.load("Guns/BladeGuns/SilverBladeGun.png")
silver_blade_gun = pygame.transform.scale(silver_blade_gun, (200, 200))
gold_blade_gun = pygame.image.load("Guns/BladeGuns/GoldBladeGun.png")
gold_blade_gun = pygame.transform.scale(gold_blade_gun, (200, 200))
diamond_blade_gun = pygame.image.load("Guns/BladeGuns/DiamondBladeGun.png")
diamond_blade_gun = pygame.transform.scale(diamond_blade_gun, (200, 200))

red_ancient_gun = pygame.image.load("Guns/AncientGuns/RedAncientGun.png")
red_ancient_gun = pygame.transform.scale(red_ancient_gun, (200, 200))
orange_ancient_gun = pygame.image.load("Guns/AncientGuns/OrangeAncientGun.png")
orange_ancient_gun = pygame.transform.scale(orange_ancient_gun, (200, 200))
yellow_ancient_gun = pygame.image.load("Guns/AncientGuns/YellowAncientGun.png")
yellow_ancient_gun = pygame.transform.scale(yellow_ancient_gun, (200, 200))
green_ancient_gun = pygame.image.load("Guns/AncientGuns/GreenAncientGun.png")
green_ancient_gun = pygame.transform.scale(green_ancient_gun, (200, 200))
teal_ancient_gun = pygame.image.load("Guns/AncientGuns/TealAncientGun.png")
teal_ancient_gun = pygame.transform.scale(teal_ancient_gun, (200, 200))
blue_ancient_gun = pygame.image.load("Guns/AncientGuns/BlueAncientGun.png")
blue_ancient_gun = pygame.transform.scale(blue_ancient_gun, (200, 200))
purple_ancient_gun = pygame.image.load("Guns/AncientGuns/PurpleAncientGun.png")
purple_ancient_gun = pygame.transform.scale(purple_ancient_gun, (200, 200))
pink_ancient_gun = pygame.image.load("Guns/AncientGuns/PinkAncientGun.png")
pink_ancient_gun = pygame.transform.scale(pink_ancient_gun, (200, 200))
brown_ancient_gun = pygame.image.load("Guns/AncientGuns/BrownAncientGun.png")
brown_ancient_gun = pygame.transform.scale(brown_ancient_gun, (200, 200))
white_ancient_gun = pygame.image.load("Guns/AncientGuns/WhiteAncientGun.png")
white_ancient_gun = pygame.transform.scale(white_ancient_gun, (200, 200))
black_ancient_gun = pygame.image.load("Guns/AncientGuns/BlackAncientGun.png")
black_ancient_gun = pygame.transform.scale(black_ancient_gun, (200, 200))
bronze_ancient_gun = pygame.image.load("Guns/AncientGuns/BronzeAncientGun.png")
bronze_ancient_gun = pygame.transform.scale(bronze_ancient_gun, (200, 200))
silver_ancient_gun = pygame.image.load("Guns/AncientGuns/SilverAncientGun.png")
silver_ancient_gun = pygame.transform.scale(silver_ancient_gun, (200, 200))
gold_ancient_gun = pygame.image.load("Guns/AncientGuns/GoldAncientGun.png")
gold_ancient_gun = pygame.transform.scale(gold_ancient_gun, (200, 200))
diamond_ancient_gun = pygame.image.load("Guns/AncientGuns/DiamondAncientGun.png")
diamond_ancient_gun = pygame.transform.scale(diamond_ancient_gun, (200, 200))

red_modern_gun = pygame.image.load("Guns/ModernGuns/RedModernGun.png")
red_modern_gun = pygame.transform.scale(red_modern_gun, (200, 200))
orange_modern_gun = pygame.image.load("Guns/ModernGuns/OrangeModernGun.png")
orange_modern_gun = pygame.transform.scale(orange_modern_gun, (200, 200))
yellow_modern_gun = pygame.image.load("Guns/ModernGuns/YellowModernGun.png")
yellow_modern_gun = pygame.transform.scale(yellow_modern_gun, (200, 200))
green_modern_gun = pygame.image.load("Guns/ModernGuns/GreenModernGun.png")
green_modern_gun = pygame.transform.scale(green_modern_gun, (200, 200))
teal_modern_gun = pygame.image.load("Guns/ModernGuns/TealModernGun.png")
teal_modern_gun = pygame.transform.scale(teal_modern_gun, (200, 200))
blue_modern_gun = pygame.image.load("Guns/ModernGuns/BlueModernGun.png")
blue_modern_gun = pygame.transform.scale(blue_modern_gun, (200, 200))
purple_modern_gun = pygame.image.load("Guns/ModernGuns/PurpleModernGun.png")
purple_modern_gun = pygame.transform.scale(purple_modern_gun, (200, 200))
pink_modern_gun = pygame.image.load("Guns/ModernGuns/PinkModernGun.png")
pink_modern_gun = pygame.transform.scale(pink_modern_gun, (200, 200))
brown_modern_gun = pygame.image.load("Guns/ModernGuns/BrownModernGun.png")
brown_modern_gun = pygame.transform.scale(brown_modern_gun, (200, 200))
white_modern_gun = pygame.image.load("Guns/ModernGuns/WhiteModernGun.png")
white_modern_gun = pygame.transform.scale(white_modern_gun, (200, 200))
black_modern_gun = pygame.image.load("Guns/ModernGuns/BlackModernGun.png")
black_modern_gun = pygame.transform.scale(black_modern_gun, (200, 200))
bronze_modern_gun = pygame.image.load("Guns/ModernGuns/BronzeModernGun.png")
bronze_modern_gun = pygame.transform.scale(bronze_modern_gun, (200, 200))
silver_modern_gun = pygame.image.load("Guns/ModernGuns/SilverModernGun.png")
silver_modern_gun = pygame.transform.scale(silver_modern_gun, (200, 200))
gold_modern_gun = pygame.image.load("Guns/ModernGuns/GoldModernGun.png")
gold_modern_gun = pygame.transform.scale(gold_modern_gun, (200, 200))
diamond_modern_gun = pygame.image.load("Guns/ModernGuns/DiamondModernGun.png")
diamond_modern_gun = pygame.transform.scale(diamond_modern_gun, (200, 200))

equippedgun = red_default_gun

health_bars = {
1: [],
2: [],
3: []
}
h = 40
for i in range(1, 4):
  for j in range(1, h + 1):
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
          if event.key == pygame.K_w:
            speedY = -1
          if event.key == pygame.K_s:
            speedY = 1
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
            if pos[0] >= 225 and pos[0] <= 425 and pos[1] >= 350 and pos[1] <= 750 and signed_in == True:
              gamestatus = 1
              print("Solo Game")
            if pos[0] >= 475 and pos[0] <= 675 and pos[1] >= 350 and pos[1] <= 750:
              print("Ranked Game")
            if pos[0] >= 725 and pos[0] <= 925 and pos[1] >= 350 and pos[1] <= 750:
              print("Squads Game")
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 150 and pos[1] <= 300:
              equippedguntype = 1
              equippedgun = red_default_gun
              DamageGun = 1
              SpeedGun = 1
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 150 and pos[1] <= 300:
              equippedguntype = 2
              equippedgun = red_short_gun
              DamageGun = 0.75
              SpeedGun = 1.25
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 150 and pos[1] <= 300:
              equippedguntype = 3
              equippedgun = red_long_gun
              DamageGun = 1.25
              SpeedGun = 0.75
            if pos[0] >= 1520 and pos[0] <= 1670 and pos[1] >= 150 and pos[1] <= 300:
              equippedguntype = 4
              equippedgun = red_spike_gun
              DamageGun = 1.5
              SpeedGun = 1.25
            if pos[0] >= 1010 and pos[0] <= 1160 and pos[1] >= 320 and pos[1] <= 470:
              equippedguntype = 5
              equippedgun = red_blade_gun
              DamageGun = 1.25
              SpeedGun = 1.5
            if pos[0] >= 1180 and pos[0] <= 1330 and pos[1] >= 320 and pos[1] <= 470:
              equippedguntype = 6
              equippedgun = red_ancient_gun
              DamageGun = 0.5
              SpeedGun = 2
            if pos[0] >= 1350 and pos[0] <= 1500 and pos[1] >= 320 and pos[1] <= 470:
              equippedguntype = 7
              equippedgun = red_modern_gun
              DamageGun = 2
              SpeedGun = 0.5
            if pos[0] >= 1125 and pos[0] <= 1195 and pos[1] >= 650 and pos[1] <= 720:
              if equippedguntype == 1:
                equippedgun = red_default_gun
              elif equippedguntype == 2:
                equippedgun = red_short_gun
              elif equippedguntype == 3:
                equippedgun = red_long_gun
              elif equippedguntype == 4:
                equippedgun = red_spike_gun
              elif equippedguntype == 5:
                equippedgun = red_blade_gun
              elif equippedguntype == 6:
                equippedgun = red_ancient_gun
              elif equippedguntype == 7:
                equippedgun = red_modern_gun
            if pos[0] >= 1215 and pos[0] <= 1285 and pos[1] >= 650 and pos[1] <= 720:
              if equippedguntype == 1:
                equippedgun = orange_default_gun
              elif equippedguntype == 2:
                equippedgun = orange_short_gun
              elif equippedguntype == 3:
                equippedgun = orange_long_gun
              elif equippedguntype == 4:
                equippedgun = orange_spike_gun
              elif equippedguntype == 5:
                equippedgun = orange_blade_gun
              elif equippedguntype == 6:
                equippedgun = orange_ancient_gun
              elif equippedguntype == 7:
                equippedgun = orange_modern_gun
            if pos[0] >= 1305 and pos[0] <= 1375 and pos[1] >= 650 and pos[1] <= 720:
              if equippedguntype == 1:
                equippedgun = yellow_default_gun
              elif equippedguntype == 2:
                equippedgun = yellow_short_gun
              elif equippedguntype == 3:
                equippedgun = yellow_long_gun
              elif equippedguntype == 4:
                equippedgun = yellow_spike_gun
              elif equippedguntype == 5:
                equippedgun = yellow_blade_gun
              elif equippedguntype == 6:
                equippedgun = yellow_ancient_gun
              elif equippedguntype == 7:
                equippedgun = yellow_modern_gun
            if pos[0] >= 1395 and pos[0] <= 1465 and pos[1] >= 650 and pos[1] <= 720:
              if equippedguntype == 1:
                equippedgun = green_default_gun
              elif equippedguntype == 2:
                equippedgun = green_short_gun
              elif equippedguntype == 3:
                equippedgun = green_long_gun
              elif equippedguntype == 4:
                equippedgun = green_spike_gun
              elif equippedguntype == 5:
                equippedgun = green_blade_gun
              elif equippedguntype == 6:
                equippedgun = green_ancient_gun
              elif equippedguntype == 7:
                equippedgun = green_modern_gun
            if pos[0] >= 1485 and pos[0] <= 1555 and pos[1] >= 650 and pos[1] <= 720:
              if equippedguntype == 1:
                equippedgun = teal_default_gun
              elif equippedguntype == 2:
                equippedgun = teal_short_gun
              elif equippedguntype == 3:
                equippedgun = teal_long_gun
              elif equippedguntype == 4:
                equippedgun = teal_spike_gun
              elif equippedguntype == 5:
                equippedgun = teal_blade_gun
              elif equippedguntype == 6:
                equippedgun = teal_ancient_gun
              elif equippedguntype == 7:
                equippedgun = teal_modern_gun
            if pos[0] >= 1125 and pos[0] <= 1195 and pos[1] >= 740 and pos[1] <= 810:
              if equippedguntype == 1:
                equippedgun = blue_default_gun
              elif equippedguntype == 2:
                equippedgun = blue_short_gun
              elif equippedguntype == 3:
                equippedgun = blue_long_gun
              elif equippedguntype == 4:
                equippedgun = blue_spike_gun
              elif equippedguntype == 5:
                equippedgun = blue_blade_gun
              elif equippedguntype == 6:
                equippedgun = blue_ancient_gun
              elif equippedguntype == 7:
                equippedgun = blue_modern_gun
            if pos[0] >= 1215 and pos[0] <= 1285 and pos[1] >= 740 and pos[1] <= 810:
              if equippedguntype == 1:
                equippedgun = purple_default_gun
              elif equippedguntype == 2:
                equippedgun = purple_short_gun
              elif equippedguntype == 3:
                equippedgun = purple_long_gun
              elif equippedguntype == 4:
                equippedgun = purple_spike_gun
              elif equippedguntype == 5:
                equippedgun = purple_blade_gun
              elif equippedguntype == 6:
                equippedgun = purple_ancient_gun
              elif equippedguntype == 7:
                equippedgun = purple_modern_gun
            if pos[0] >= 1305 and pos[0] <= 1375 and pos[1] >= 740 and pos[1] <= 810:
              if equippedguntype == 1:
                equippedgun = pink_default_gun
              elif equippedguntype == 2:
                equippedgun = pink_short_gun
              elif equippedguntype == 3:
                equippedgun = pink_long_gun
              elif equippedguntype == 4:
                equippedgun = pink_spike_gun
              elif equippedguntype == 5:
                equippedgun = pink_blade_gun
              elif equippedguntype == 6:
                equippedgun = pink_ancient_gun
              elif equippedguntype == 7:
                equippedgun = pink_modern_gun
            if pos[0] >= 1395 and pos[0] <= 1465 and pos[1] >= 740 and pos[1] <= 810:
              if equippedguntype == 1:
                equippedgun = brown_default_gun
              elif equippedguntype == 2:
                equippedgun = brown_short_gun
              elif equippedguntype == 3:
                equippedgun = brown_long_gun
              elif equippedguntype == 4:
                equippedgun = brown_spike_gun
              elif equippedguntype == 5:
                equippedgun = brown_blade_gun
              elif equippedguntype == 6:
                equippedgun = brown_ancient_gun
              elif equippedguntype == 7:
                equippedgun = brown_modern_gun
            if pos[0] >= 1485 and pos[0] <= 1555 and pos[1] >= 740 and pos[1] <= 810:
              if equippedguntype == 1:
                equippedgun = white_default_gun
              elif equippedguntype == 2:
                equippedgun = white_short_gun
              elif equippedguntype == 3:
                equippedgun = white_long_gun
              elif equippedguntype == 4:
                equippedgun = white_spike_gun
              elif equippedguntype == 5:
                equippedgun = white_blade_gun
              elif equippedguntype == 6:
                equippedgun = white_ancient_gun
              elif equippedguntype == 7:
                equippedgun = white_modern_gun
            if pos[0] >= 1125 and pos[0] <= 1195 and pos[1] >= 830 and pos[1] <= 900:
              if equippedguntype == 1:
                equippedgun = black_default_gun
              elif equippedguntype == 2:
                equippedgun = black_short_gun
              elif equippedguntype == 3:
                equippedgun = black_long_gun
              elif equippedguntype == 4:
                equippedgun = black_spike_gun
              elif equippedguntype == 5:
                equippedgun = black_blade_gun
              elif equippedguntype == 6:
                equippedgun = black_ancient_gun
              elif equippedguntype == 7:
                equippedgun = black_modern_gun
            if pos[0] >= 1215 and pos[0] <= 1285 and pos[1] >= 830 and pos[1] <= 900:
              if equippedguntype == 1:
                equippedgun = bronze_default_gun
              elif equippedguntype == 2:
                equippedgun = bronze_short_gun
              elif equippedguntype == 3:
                equippedgun = bronze_long_gun
              elif equippedguntype == 4:
                equippedgun = bronze_spike_gun
              elif equippedguntype == 5:
                equippedgun = bronze_blade_gun
              elif equippedguntype == 6:
                equippedgun = bronze_ancient_gun
              elif equippedguntype == 7:
                equippedgun = bronze_modern_gun
            if pos[0] >= 1305 and pos[0] <= 1375 and pos[1] >= 830 and pos[1] <= 900:
              if equippedguntype == 1:
                equippedgun = silver_default_gun
              elif equippedguntype == 2:
                equippedgun = silver_short_gun
              elif equippedguntype == 3:
                equippedgun = silver_long_gun
              elif equippedguntype == 4:
                equippedgun = silver_spike_gun
              elif equippedguntype == 5:
                equippedgun = silver_blade_gun
              elif equippedguntype == 6:
                equippedgun = silver_ancient_gun
              elif equippedguntype == 7:
                equippedgun = silver_modern_gun
            if pos[0] >= 1395 and pos[0] <= 1465 and pos[1] >= 830 and pos[1] <= 900:
              if equippedguntype == 1:
                equippedgun = gold_default_gun
              elif equippedguntype == 2:
                equippedgun = gold_short_gun
              elif equippedguntype == 3:
                equippedgun = gold_long_gun
              elif equippedguntype == 4:
                equippedgun = gold_spike_gun
              elif equippedguntype == 5:
                equippedgun = gold_blade_gun
              elif equippedguntype == 6:
                equippedgun = gold_ancient_gun
              elif equippedguntype == 7:
                equippedgun = gold_modern_gun
            if pos[0] >= 1485 and pos[0] <= 1555 and pos[1] >= 830 and pos[1] <= 900:
              if equippedguntype == 1:
                equippedgun = diamond_default_gun
              elif equippedguntype == 2:
                equippedgun = diamond_short_gun
              elif equippedguntype == 3:
                equippedgun = diamond_long_gun
              elif equippedguntype == 4:
                equippedgun = diamond_spike_gun
              elif equippedguntype == 5:
                equippedgun = diamond_blade_gun
              elif equippedguntype == 6:
                equippedgun = diamond_ancient_gun
              elif equippedguntype == 7:
                equippedgun = diamond_modern_gun
            if pos[0] >= 315 and pos[0] <= 435 and pos[1] >= 140 and pos[1] <= 190 and signed_in == False:
              signing_up = True
              logging_in = False
              username_text = ""
              password_text = ""
              username_typing = False
              password_typing = False
              password_text_hide = ""
            if pos[0] >= 445 and pos[0] <= 540 and pos[1] >= 140 and pos[1] <= 190 and signed_in == False:
              logging_in = True
              signing_up == False
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
      if shieldactive == True:
        shieldtimedifference = time.time() - shieldtime
        if shieldtimedifference > shieldduration:
          shieldactive = False
        else:
          display.blit(equippedshield, (positionX - 10, positionY - 10))
      display.blit(purple_bullet_five, (positionX + 5, positionY - 35))
      display.blit(health_bars[healthtype][health - 1],(positionX, positionY - 25))
      for player, (x, y) in positions.items():
        display.blit(plasmatank, (x, y))
      positionX += speedX
      positionY += speedY
    else:
      display.fill((255, 255, 255))
      pygame.draw.rect(display, pygame.Color(colors["Gold"]), (0, 0, 960, 972))
      pygame.draw.rect(display, pygame.Color(colors["Silver"]), (960, 0, 960, 972))
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
      pygame.draw.rect(display, pygame.Color(0, 0, 0), (1410, 565, 220, 50))
      pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1415, 570, 210, 40))
      text1 = font1.render("PLAY SOLO", False, pygame.Color(colors["White"]))
      text2 = font1.render("PLAY RANKED", False, pygame.Color(colors["White"]))
      text3 = font1.render("PLAY SQUADS", False, pygame.Color(colors["White"]))
      text4 = font1.render("Damage Buff: X" + str(DamageGun), False, pygame.Color(0, 0, 0))
      text5 = font1.render("Speed Buff: X" + str(SpeedGun), False, pygame.Color(0, 0, 0))
      text6 = font1.render("Cash: " + str(cash), False, pygame.Color(0, 0, 0))
      text7 = font1.render(str(level), False, pygame.Color(255, 255, 255))
      text8 = font1.render("Sign Up", False, (0, 0, 0))
      text9 = font1.render("Log In", False, (0, 0, 0))
      text10 = font1.render("You must be signed in to play a game!", False, (0, 0, 0))
      text11 = font3.render("Username", False, (255, 255, 255))
      text12 = font3.render("Password", False, (255, 255, 255))
      text13 = font4.render("X", False, (255, 255, 255))
      text14 = font5.render(">", False, (0, 0, 0))
      text15 = font2.render("Gun Customization", False, (0, 0, 0))
      text16 = font2.render("Tank Customization", False, (0, 0, 0))
      display.blit(red_default_gun, (985, 130))
      display.blit(red_short_gun, (1155, 130))
      display.blit(red_long_gun, (1325, 130))
      display.blit(red_spike_gun, (1495, 130))
      display.blit(red_blade_gun, (985, 300))
      display.blit(red_ancient_gun, (1155, 300))
      display.blit(red_modern_gun, (1325, 300))
      display.blit(equippedgun, (1250, 470))
      display.blit(levels_ninetyone_hundred, (200, 115))
      display.blit(text1, (250, 525))
      display.blit(text2, (475, 525))
      display.blit(text3, (725, 525))
      display.blit(text4, (1020, 505))
      display.blit(text5, (1020, 545))
      display.blit(text6, (1450, 505))
      display.blit(text7, (243, 153))
      display.blit(text16, (1420, 580))
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
        username_surface = font1.render(username_text, True, (0, 0, 0))
        display.blit(username_surface, (300, 153))
    pygame.display.flip()