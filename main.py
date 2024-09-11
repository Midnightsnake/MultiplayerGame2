import pygame
import pygame.draw_py
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
bullettype = 1
rapidfiretype = 1
shieldtype = 1
nuketype = 1
homingtype = 1
ancientbullettype = 1
flaktype = 1
equippedguntype = 1
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

f_hb_0 = pygame.image.load("HealthBars/FirstHealthBar-0.png")
f_hb_0 = pygame.transform.scale(f_hb_0, (30, 30))
f_hb_1 = pygame.image.load("HealthBars/FirstHealthBar-1.png")
f_hb_1 = pygame.transform.scale(f_hb_1, (30, 30))
f_hb_2 = pygame.image.load("HealthBars/FirstHealthBar-2.png")
f_hb_2 = pygame.transform.scale(f_hb_2, (30, 30))
f_hb_3 = pygame.image.load("HealthBars/FirstHealthBar-3.png")
f_hb_3 = pygame.transform.scale(f_hb_3, (30, 30))
f_hb_4 = pygame.image.load("HealthBars/FirstHealthBar-4.png")
f_hb_4 = pygame.transform.scale(f_hb_4, (30, 30))
f_hb_5 = pygame.image.load("HealthBars/FirstHealthBar-5.png")
f_hb_5 = pygame.transform.scale(f_hb_5, (30, 30))
f_hb_6 = pygame.image.load("HealthBars/FirstHealthBar-6.png")
f_hb_6 = pygame.transform.scale(f_hb_6, (30, 30))
f_hb_7 = pygame.image.load("HealthBars/FirstHealthBar-7.png")
f_hb_7 = pygame.transform.scale(f_hb_7, (30, 30))
f_hb_8 = pygame.image.load("HealthBars/FirstHealthBar-8.png")
f_hb_8 = pygame.transform.scale(f_hb_8, (30, 30))
f_hb_9 = pygame.image.load("HealthBars/FirstHealthBar-9.png")
f_hb_9 = pygame.transform.scale(f_hb_9, (30, 30))
f_hb_10 = pygame.image.load("HealthBars/FirstHealthBar-10.png")
f_hb_10 = pygame.transform.scale(f_hb_10, (30, 30))
f_hb_11 = pygame.image.load("HealthBars/FirstHealthBar-11.png")
f_hb_11 = pygame.transform.scale(f_hb_11, (30, 30))
f_hb_12 = pygame.image.load("HealthBars/FirstHealthBar-12.png")
f_hb_12 = pygame.transform.scale(f_hb_12, (30, 30))
f_hb_13 = pygame.image.load("HealthBars/FirstHealthBar-13.png")
f_hb_13 = pygame.transform.scale(f_hb_13, (30, 30))
f_hb_14 = pygame.image.load("HealthBars/FirstHealthBar-14.png")
f_hb_14 = pygame.transform.scale(f_hb_14, (30, 30))
f_hb_15 = pygame.image.load("HealthBars/FirstHealthBar-15.png")
f_hb_15 = pygame.transform.scale(f_hb_15, (30, 30))
f_hb_16 = pygame.image.load("HealthBars/FirstHealthBar-16.png")
f_hb_16 = pygame.transform.scale(f_hb_16, (30, 30))
f_hb_17 = pygame.image.load("HealthBars/FirstHealthBar-17.png")
f_hb_17 = pygame.transform.scale(f_hb_17, (30, 30))
f_hb_18 = pygame.image.load("HealthBars/FirstHealthBar-18.png")
f_hb_18 = pygame.transform.scale(f_hb_18, (30, 30))
f_hb_19 = pygame.image.load("HealthBars/FirstHealthBar-19.png")
f_hb_19 = pygame.transform.scale(f_hb_19, (30, 30))
f_hb_20 = pygame.image.load("HealthBars/FirstHealthBar-20.png")
f_hb_20 = pygame.transform.scale(f_hb_20, (30, 30))
f_hb_21 = pygame.image.load("HealthBars/FirstHealthBar-21.png")
f_hb_21 = pygame.transform.scale(f_hb_21, (30, 30))
f_hb_22 = pygame.image.load("HealthBars/FirstHealthBar-22.png")
f_hb_22 = pygame.transform.scale(f_hb_22, (30, 30))
f_hb_23 = pygame.image.load("HealthBars/FirstHealthBar-23.png")
f_hb_23 = pygame.transform.scale(f_hb_23, (30, 30))
f_hb_24 = pygame.image.load("HealthBars/FirstHealthBar-24.png")
f_hb_24 = pygame.transform.scale(f_hb_24, (30, 30))
f_hb_25 = pygame.image.load("HealthBars/FirstHealthBar-25.png")
f_hb_25 = pygame.transform.scale(f_hb_25, (30, 30))
f_hb_26 = pygame.image.load("HealthBars/FirstHealthBar-26.png")
f_hb_26 = pygame.transform.scale(f_hb_26, (30, 30))
f_hb_27 = pygame.image.load("HealthBars/FirstHealthBar-27.png")
f_hb_27 = pygame.transform.scale(f_hb_27, (30, 30))
f_hb_28 = pygame.image.load("HealthBars/FirstHealthBar-28.png")
f_hb_28 = pygame.transform.scale(f_hb_28, (30, 30))
f_hb_29 = pygame.image.load("HealthBars/FirstHealthBar-29.png")
f_hb_29 = pygame.transform.scale(f_hb_29, (30, 30))
f_hb_30 = pygame.image.load("HealthBars/FirstHealthBar-30.png")
f_hb_30 = pygame.transform.scale(f_hb_30, (30, 30))
f_hb_31 = pygame.image.load("HealthBars/FirstHealthBar-31.png")
f_hb_31 = pygame.transform.scale(f_hb_31, (30, 30))
f_hb_32 = pygame.image.load("HealthBars/FirstHealthBar-32.png")
f_hb_32 = pygame.transform.scale(f_hb_32, (30, 30))
f_hb_33 = pygame.image.load("HealthBars/FirstHealthBar-33.png")
f_hb_33 = pygame.transform.scale(f_hb_33, (30, 30))
f_hb_34 = pygame.image.load("HealthBars/FirstHealthBar-34.png")
f_hb_34 = pygame.transform.scale(f_hb_34, (30, 30))
f_hb_35 = pygame.image.load("HealthBars/FirstHealthBar-35.png")
f_hb_35 = pygame.transform.scale(f_hb_35, (30, 30))
f_hb_36 = pygame.image.load("HealthBars/FirstHealthBar-36.png")
f_hb_36 = pygame.transform.scale(f_hb_36, (30, 30))
f_hb_37 = pygame.image.load("HealthBars/FirstHealthBar-37.png")
f_hb_37 = pygame.transform.scale(f_hb_37, (30, 30))
f_hb_38 = pygame.image.load("HealthBars/FirstHealthBar-38.png")
f_hb_38 = pygame.transform.scale(f_hb_38, (30, 30))
f_hb_39 = pygame.image.load("HealthBars/FirstHealthBar-39.png")
f_hb_39 = pygame.transform.scale(f_hb_39, (30, 30))
f_hb_40 = pygame.image.load("HealthBars/FirstHealthBar-40.png")
f_hb_40 = pygame.transform.scale(f_hb_40, (30, 30))
f_hb = [f_hb_0, f_hb_1, f_hb_2, f_hb_3, f_hb_4, f_hb_5, f_hb_6, f_hb_7, f_hb_8, f_hb_9, f_hb_10, f_hb_11, f_hb_12, f_hb_13, f_hb_14, f_hb_15, f_hb_16, f_hb_17, f_hb_18, f_hb_19, f_hb_20, f_hb_21, f_hb_22, f_hb_23, f_hb_24, f_hb_25, f_hb_26, f_hb_27, f_hb_28, f_hb_29, f_hb_30, f_hb_31, f_hb_32, f_hb_33, f_hb_34, f_hb_35, f_hb_36, f_hb_37, f_hb_38, f_hb_39, f_hb_40]

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
bottom_left_earth_map = pygame.image.load("Maps/BottomLeftEarthMap.png")
bottom_left_earth_map = pygame.transform.scale(bottom_left_earth_map, (625, 625))
bottom_right_earth_map = pygame.image.load("Maps/BottomRightEarthMap.png")
bottom_right_earth_map = pygame.transform.scale(bottom_right_earth_map, (625, 625))
top_left_earth_map = pygame.image.load("Maps/TopLeftEarthMap.png")
top_left_earth_map = pygame.transform.scale(top_left_earth_map, (625, 625))
top_right_earth_map = pygame.image.load("Maps/TopRightEarthMap.png")
top_right_earth_map = pygame.transform.scale(top_right_earth_map, (625, 625))

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
          if event.key == pygame.K_EQUALS:
            health += 1
          if event.key == pygame.K_MINUS:
            health -= 1
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
            if pos[0] >= 225 and pos[0] <= 525 and pos[1] >= 350 and pos[1] <= 750 and signed_in == True:
              gamestatus = 1
              print("Solo Game")
            if pos[0] >= 475 and pos[0] <= 825 and pos[1] >= 350 and pos[1] <= 750:
              print("Ranked Game")
            if pos[0] >= 725 and pos[0] <= 825 and pos[1] >= 350 and pos[1] <= 750:
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
      display.fill((0, 255, 255))
      display.blit(lobby_one_map, (330, 110))
    if gamestatus == 2:
      display.fill((0, 255, 255))
      display.blit(bottom_left_earth_map, (330, 345))
      display.blit(bottom_right_earth_map, (955, 345))
      display.blit(top_left_earth_map, (330, 110))
      display.blit(top_right_earth_map, (955, 110))
      bullettype = 1
      display.blit(purple_bullet_five, (positionX + 10, positionY - 15))
      display.blit(f_hb[health],(positionX, positionY - 15))
      positionX += speedX
      positionY += speedY
    else:
      display.fill((255, 255, 255))
      pygame.draw.rect(display, pygame.Color(colors["Gold"]), (0, 0, 960, 972))
      pygame.draw.rect(display, pygame.Color(colors["Diamond"]), (960, 0, 960, 972))
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
      pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1010, 150, 150, 150))
      pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1180, 150, 150, 150))
      pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1350, 150, 150, 150))
      pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1520, 150, 150, 150))
      pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1010, 320, 150, 150))
      pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1180, 320, 150, 150))
      pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (1350, 320, 150, 150))
      pygame.draw.rect(display, pygame.Color(colors["Light Bronze"]), (1010, 490, 660, 455))
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
      display.blit(text6, (1420, 505))
      display.blit(text7, (243, 153))
      if signed_in == False:
        pygame.draw.rect(display, pygame.Color(colors["Bronze"]), (315, 140, 120, 50))
        pygame.draw.rect(display, pygame.Color(colors["Silver"]), (445, 140, 95, 50))
        display.blit(text8, (320, 150))
        display.blit(text9, (450, 150))
        display.blit(text10, (320, 300))
        if signing_up == True:
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