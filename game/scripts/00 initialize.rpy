# Seeds of Sylvia
# Copyright 2015, Watercress
# Created for the Lemmasoft Forums 2015 Secret Santa

# Written by:
# Blank
# Brythain
# Electro
# EmpireRuled
# Leaty
# TheForeverLoneWolf
# Tutty
# Valjean

# Art by:
# Eddie
# Erica
# InstantRiot

# Music by:
# Numb
# Praxic

# Coding by:
# DarkArcher

# Now, for the fun stuff.

#NVL Characters
define nar = Character(None, kind=nvl)
define anr = Character('News Anchor', kind=nvl, color='#8c6b48')
define dor = Character('Dr. Mördorj', kind=nvl, color='#a62e1f')

# Characters
define ann = Character('News Anchor', color='#8c6b48', show_two_window=True)
define mor = Character('Dr. Mördorj', color='#a62e1f', show_two_window=True)
define ash = Character('Ashley', color='#595c2d', show_two_window=True)
define sib = Character('Sibyl', color='#5b758e', show_two_window=True)
define flo = DynamicCharacter('turname', color='#b6ccd9', show_two_window=True)
define copa = Character('Thug', color='#f1bf66', show_two_window=True)
define copb = Character('Thug', color='#57452f', show_two_window=True)

# Backgrounds
image nobg = "bg/nobg.png"
image grass = "bg/grass.png"
image grassnight = "bg/grassnight.png"
image bar = "bg/bar.png"
image forestoutskirts = "bg/forestoutskirts.png"
image forestpath = "bg/forestpath.png"
image cabin = "bg/cabinint.png"


# CGs
image tv = "cg/tv.png"
image turnip = "cg/turnip.png"

# VFX
image watercress = "vfx/watercress.png"
image credit1 = "vfx/credit1.png"
image credit2 = "vfx/credit2.png"
image credit3 = "vfx/credit3.png"
image credit4 = "vfx/credit4.png"

# Sprites
image floafraid = "sprites/flo/afraid.png"
image flobittersweet = "sprites/flo/bittersweet.png"
image flocalm = "sprites/flo/calm.png"
image flocheery = "sprites/flo/cheery.png"
image flocrying = "sprites/flo/crying.png"
image flocurious = "sprites/flo/curious.png"
image floeager = "sprites/flo/eager.png"
image floeyesclosed = "sprites/flo/eyesclosed.png"
image floeyesnarrow = "sprites//flo/eyesnarrow.png"
image floforelorn = "sprites/flo/forelorn.png"
image flohappy = "sprites/flo/happy.png"
image flohopeful = "sprites/flo/hopeful.png"
image flohopeless = "sprites/flo/hopeless.png"
image flolistening = "sprites/flo/listening.png"
image flopeaceful = "sprites/flo/peaceful.png"
image flopleasant = "sprites/flo/pleasant.png"
image flopray = "sprites/flo/pray.png"
image floresigned = "sprites/flo/resigned.png"
image floshocked = "sprites/flo/shocked.png"
image flosmile = "sprites/flo/smile.png"
image flosweetsmile = "sprites/flo/sweetsmile.png"
image flojoy = "sprites/flo/zoom/joy.png"
image flotender = "sprites/flo/tender.png"
image floworried = "sprites/flo/worried.png"

image floafraidzoom = "sprites/flo/zoom/afraid.png"
image flobittersweetzoom = "sprites/flo/zoom/bittersweet.png"
image flocalmzoom = "sprites/flo/zoom/calm.png"
image flocheeryzoom = "sprites/flo/zoom/cheery.png"
image flocryingzoom = "sprites/flo/zoom/crying.png"
image flocuriouszoom = "sprites/flo/zoom/curious.png"
image floeagerzoom = "sprites/flo/zoom/eager.png"
image floeyesclosedzoom = "sprites/flo/zoom/eyesclosed.png"
image floeyesnarrowzoom = "sprites//flo/zoom/eyesnarrow.png"
image floforelornzoom = "sprites/flo/zoom/forelorn.png"
image flohappyzoom = "sprites/flo/zoom/happy.png"
image flohopefulzoom = "sprites/flo/zoom/hopeful.png"
image flohopelesszoom = "sprites/flo/zoom/hopeless.png"
image flolisteningzoom = "sprites/flo/zoom/listening.png"
image flopeacefulzoom = "sprites/flo/zoom/peaceful.png"
image flopleasantzoom = "sprites/flo/zoom/pleasant.png"
image floprayzoom = "sprites/flo/zoom/pray.png"
image floresignedzoom = "sprites/flo/zoom/resigned.png"
image floshockedzoom = "sprites/flo/zoom/shocked.png"
image flosmilezoom = "sprites/flo/zoom/smile.png"
image flosweetsmilezoom = "sprites/flo/zoom/sweetsmile.png"
image flojoyzoom = "sprites/flo/zoom/joy.png"
image flotenderzoom = "sprites/flo/zoom/tender.png"
image floworriedzoom = "sprites/flo/zoom/worried.png"

# Splash Screen
label splashscreen:
    scene black 
    with Pause(1)

    show watercress with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return


# The game starts here.
label start:

    # Initialize Variables
    $ turname = "Voice"

    stop music

    jump prologue