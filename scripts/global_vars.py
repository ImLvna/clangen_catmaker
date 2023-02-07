import pygame
import pygame_gui
from bidict import bidict
pygame.init()
screen_x, screen_y = 800, 700
SCREEN = pygame.display.set_mode((screen_x, screen_y))
MANAGER = pygame_gui.ui_manager.UIManager((screen_x, screen_y), 'resources/defaults.json')

MANAGER.get_theme().load_theme('resources/buttons.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')

import scripts.cat.cats

CREATED_CAT = scripts.cat.cats.Cat()

pelt_options = bidict({"SingleColour": "Plain",  "Smoke": "Smoke", 'Singlestripe': "Single Stripe", 'Tabby': "Tabby",
                       'Ticked': "Ticked Tabby", 'Mackerel': "Mackerel Tabby", 'Classic': "Classic Tabby",
                       'Sokoke': 'Sokoke', 'Agouti': "Agouti", "Speckled": "Speckled Tabby", "Rosette": "Rosette",
                       "Bengal": "Bengal", "Marbled": "Marbled Tabby"})

tortie_patches_patterns = ["Tabby", ]

colors = bidict({'WHITE': 'White', 'GREY': 'Grey', 'DARKGREY': 'Dark Grey', 'PALEGREY': 'Pale Grey',
                 'SILVER': 'Silver', 'GOLDEN': 'Golden', 'DARKGINGER': 'Dark Ginger', 'PALEGINGER': 'Pale Ginger',
                 'CREAM': 'Cream', 'BROWN': 'Brown', 'DARKBROWN': 'Dark Brown', 'LIGHTBROWN': 'Light Brown',
                 'BLACK': 'Black', "GHOST": "Ghost", "GINGER": "Ginger"})

white_patches = bidict({None: 'None', 'LITTLE': 'Little', 'LITTLECREAMY': 'Little Creamy', 'TUXEDO': 'Tuxedo',
                        'LIGHTTUXEDO': 'Light Tuxedo', 'TUXEDOCREAMY': 'Tuxedo Creamy', 'BUZZARDFANG': 'Buzzardfang',
                        'TIP': 'Tip', 'BLAZE': 'Blaze', 'BIB': 'Bib', 'VEE': 'Vee', 'PAWS': 'Paws', 'BELLY': 'Belly',
                        'TAILTIP': 'Tail Tip', 'TOES': 'Toes', 'BROKENBLAZE': 'Broken Blaze', 'LILTWO': 'Lil Two',
                        'SCOURGE': 'Scourge', 'TOESTAIL': 'Toes Tail', 'RAVENPAW': 'Ravenpaw', 'HONEY': 'Honey',
                        'FANCY': 'Fancy', 'UNDERS': 'Unders', 'DAMIEN': 'Damien', 'SKUNK': 'Skunk',
                        'MITAINE': 'Mitaine', 'SQUEAKS': 'Squeaks', 'STAR': 'Star', 'ANY': 'Any',
                        'ANYCREAMY': 'Any Creamy', 'ANY2': 'Any 2', 'ANY2CREAMY': 'Any 2 Creamy', 'BROKEN': 'Broken',
                        'FRECKLES': 'Freckles', 'RINGTAIL': 'Ringtail', 'HALFFACE': 'Half Face', 'PANTS2': 'Pants 2',
                        'GOATEE': 'Goatee', 'PRINCE': 'Prince', 'FAROFA': 'Farofa', 'MISTER': 'Mister',
                        'PANTS': 'Pants', 'REVERSEPANTS': 'Reverse Pants', 'HALFWHITE': 'Half White',
                        'APPALOOSA': 'Appaloosa', 'PIEBALD': 'Piebald', 'CURVED': 'Curved', 'GLASS': 'Glass',
                        'MASKMANTLE': 'Mask Mantle', 'VAN': 'Van', 'VANCREAMY': 'Van Creamy', 'ONEEAR': 'One Ear',
                        'LIGHTSONG': 'Lightsong', 'TAIL': 'Tail', 'HEART': 'Heart', 'MOORISH': 'Moorish',
                        'APRON': 'Apron', 'CAPSADDLE': 'Cap Saddle', 'COLOURPOINT': 'Colorpoint',
                        'COLOURPOINTCREAMY': 'Colorpoint Creamy', 'RAGDOLL': 'Ragdoll', 'KARPATI': 'Karpati',
                        'SEPIAPOINT': 'Sepiapoint', 'MINKPOINT': 'Minkpoint', 'SEALPOINT': 'Sealpoint',
                        'FULLWHITE': 'Full White', 'VITILIGO': 'Vitiligo', 'VITILIGO2': 'Vitiligo 2'})

tints = ["None", "Gray", "Blue", "Pink", "Red", "Black", "Orange", "Yellow", "Purple"]
scars = ["None"]

poses = {
    "short": {
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 6,
            "2": 7,
            "3": 8
        },
        "elder": {
            "1": 3,
            "2": 4,
            "3": 5
        }
    },
    "long": {
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "elder": {
            "1": 3,
            "2": 4,
            "3": 5
        }
    }
}