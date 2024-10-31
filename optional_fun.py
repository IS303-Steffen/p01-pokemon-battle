import sys, subprocess, os, random, time, platform

################
## SKIP THIS####
################
def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Function to install packages using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try to import pygame, and install it if it's missing
try:
    import pygame
except ImportError:
    print("Pygame is not installed. Installing now...")
    install('pygame')
    import pygame  # Try importing again after installation

# Initialize the mixer
pygame.mixer.init()

clear_screen()


###############################################
# PUT THIS AT THE START OF YOUR BATTLE FUNCTION
###############################################

def battle_music():
    # Define the path to the media file
    media_path = os.path.join(os.path.dirname(__file__), 'media', '1-15 Battle (Vs Trainer).mp3')

    # Load and play the MP3 file in the background
    pygame.mixer.music.load(media_path)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Use -1 to loop indefinitely

###############################################
# PUT THIS AT THE START OF YOUR ATTACK FUNCTION
###############################################

# if you are really bored, you can make this match the attack chosen instead
# of choosing a random one.

def attack_sfx():
    sfx_list = [
        'Ember.wav',
        'Flamethrower.wav',
        'HydroPumpSingle.wav',
        'QuickAttack.wav',
        'Slash.wav',
        'SolarBeam.wav',
        'Tackle.wav',
        'VineWhip.wav',
        'WaterGun.wav'
    ]
    sfx = random.choice(sfx_list)
    
    # Define the path to the media file
    media_path = os.path.join(os.path.dirname(__file__), 'media', sfx)

    # Load the sound effect as a Sound object
    sound_effect = pygame.mixer.Sound(media_path)
    sound_effect.set_volume(.7)
    sound_effect.play()  # Play sound effect on a separate channel without interrupting the background music

#############################################
# PUT THIS AT THE START OF YOUR HEAL FUNCTION
#############################################

def heal_sfx():
    # Define the path to the media file
    media_path = os.path.join(os.path.dirname(__file__), 'media', '1-11 Pokémon Recovery.mp3')

    # Load the sound effect as a Sound object
    sound_effect = pygame.mixer.Sound(media_path)
    sound_effect.set_volume(.8)
    sound_effect.play()  # Play sound effect on a separate channel without interrupting the background music

#################################################################################
# PUT THIS AT THE VERY END OF YOUR BATTLE FUNCTION AFTER THE DEFEATED/WON MESSAGE
#################################################################################
def victory_music():
    # Define the path to the media file
    media_path = os.path.join(os.path.dirname(__file__), 'media', '1-16 Victory (Vs Trainer).mp3')

    # Load and play the MP3 file in the background
    pygame.mixer.music.load(media_path)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Loop the music indefinitely
    pygame.mixer.music.fadeout(12000)
    time.sleep(12)

    