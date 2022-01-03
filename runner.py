# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Note you can change the I2C address, or add a reset pin:
# disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c, reset=reset_pin)

# Clear display.
disp.fill(0)
disp.show()

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.UP

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT
button_B.pull = Pull.UP

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT
button_L.pull = Pull.UP

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT
button_R.pull = Pull.UP

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT
button_U.pull = Pull.UP

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT
button_D.pull = Pull.UP

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT
button_C.pull = Pull.UP


# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

stem = "/home/pi/assets-janna/"
# Image displayed on load
showImage = 'open/title.png'

mappings = {
    # in format of imageName: [[previous frame], [option 1, option 2]]

    # prompt options
    # phone prompts
    'open/phone-prompts-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 4,
        'prev': 'open/wakeup3.png', 
        'next1': 'open/weather.png'},
    'open/phone-prompts-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 4,
        'prev': 'open/wakeup3.png', 
        'next1': 'open/newsa.png'},
    'open/phone-prompts-3.png': { 
        'isPrompt': True,
        'opt-num': 3,
        'total-opt': 4,
        'prev': 'open/wakeup3.png', 
        'next1': 'open/texts.png'},
    'open/phone-prompts-4.png': { 
        'isPrompt': True,
        'opt-num': 4,
        'total-opt': 4,
        'prev': 'open/wakeup3.png', 
        'next1': 'open/in-or-out-1.png'},

    # inside or ouside prompts
    'open/in-or-out-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 2,
        'prev': 'open/phone-prompts-4.png', 
        'next1': 'inside/inside-prompts-1.png'},
    'open/in-or-out-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 2,
        'prev': 'open/phone-prompts-4.png', 
        'next1': 'outside/walk1.png'},
    # inside activity options (watch holotoons, cook breakfast, do chores)
    'inside/inside-prompts-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 3,
        'prev': 'open/in-or-out-1.png',
        'next1': 'inside/cartoons/cartoons1_a.png'
    },
    'inside/inside-prompts-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 3,
        'prev': 'open/in-or-out-1.png',
        'next1': 'inside/breakfast/kitchen.png'
    },
    'inside/inside-prompts-3.png': {
        'isPrompt': True,
        'opt-num': 3,
        'total-opt': 3,
        'prev': 'open/in-or-out-1.png',
        'next1': 'inside/chores/trash-compactor1.png'
    },
    # outside walking directions prompts (school, protest, boardwalk)
    'outside/walk-prompt-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 3,
        'prev': 'outside/walk2.png',
        'next1': 'outside/school/school.png'
    },
    'outside/walk-prompt-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 3,
        'prev': 'outside/walk2.png',
        'next1': 'outside/protest/protest.png'
    },
    'outside/walk-prompt-3.png': {
        'isPrompt': True,
        'opt-num': 3,
        'total-opt': 3,
        'prev': 'outside/walk2.png',
        'next1': 'outside/boardwalk/boardwalk1.png'
    },
    # school prompt get closer (get closer or go back)
    'outside/school/school-prompt-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 2,
        'prev': 'outside/school/school4.png',
        'next1': 'outside/school/sign.png'
    },
    'outside/school/school-prompt-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 2,
        'prev': 'outside/school/school4.png',
        'next1': 'outside/walk-prompt-1.png'
    },
    # sign prompt (vandalize or go back)
    'outside/school/sign-prompt-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 2,
        'prev': 'outside/school/sign4.png',
        'next1': 'outside/school/vandalize1.png'
    },
    'outside/school/sign-prompt-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 2,
        'prev': 'outside/school/sign4.png',
        'next1': 'outside/walk-prompt-1.png'
    },
    # get closer to protest prompt
    'outside/protest/protest-closer-prompt-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 2,
        'prev': 'outside/protest/protest3.png',
        'next1': 'outside/protest/protest-closer.png'
    },
    'outside/protest/protest-closer-prompt-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 2,
        'prev': 'outside/protest/protest3.png',
        'next1': 'outside/walk-prompt-1.png'
    },
    # get closer to protest prompt
    'outside/protest/join-protest-prompt-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 2,
        'prev': 'outside/protest/protest-closer2.png',
        'next1': 'outside/protest/protest-closer-joined.png'
    },
    'outside/protest/join-protest-prompt-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 2,
        'prev': 'outside/protest/protest-closer2.png',
        'next1': 'outside/walk-prompt-1.png'
    },
    # go on pier
    'outside/boardwalk/boardwalk-prompts-1.png': {
        'isPrompt': True,
        'opt-num': 1,
        'total-opt': 2,
        'prev': 'outside/boardwalk/boardwalk-prompt.png',
        'next1': 'outside/boardwalk/pier1.png'
    },
    'outside/boardwalk/boardwalk-prompts-2.png': {
        'isPrompt': True,
        'opt-num': 2,
        'total-opt': 2,
        'prev': 'outside/boardwalk/boardwalk-prompt.png',
        'next1': 'outside/walk-prompt-1.png'
    },

    # title and intro screen options
    'open/title.png': {
        'prev': 'open/title.png',
        'next1': 'open/controls.png'},
    'open/controls.png': {
        'prev': 'open/title.png', 
        'next1': 'open/exposition.png'},
    'open/exposition.png': {
        'prev': 'open/controls.png', 
        'next1': 'open/wakeup1.png'},
    'open/wakeup1.png': {
        'prev': 'open/exposition.png', 
        'next1': 'open/wakeup2.png'},
    'open/wakeup2.png': {
        'prev': 'open/wakeup1.png', 
        'next1': 'open/wakeup3.png'},
    'open/wakeup3.png': {
        'prev': 'open/wakeup2.png', 
        'next1': 'open/wakeup-prompta.png'},
    'open/wakeup-prompta.png': {
        'prev': 'open/wakeup3.png', 
        'next1': 'open/phone-prompts-1.png'},
    # phone options
    'open/weather.png': {
        'prev': 'open/phone-prompts-1.png', 
        'next1': 'open/phone-prompts-1.png'},
    'open/newsa.png': {
        'prev': 'open/phone-prompts-2.png', 
        'next1': 'open/newsb.png'},
    'open/newsb.png': {
        'prev': 'open/newsa.png', 
        'next1': 'open/phone-prompts-2.png'},
    'open/texts.png': {
        'prev': 'open/phone-prompts-3.png', 
        'next1': 'open/phone-prompts-3.png'},
    # cartoon watching
    'inside/cartoons/cartoons1_a.png': {
        'prev': 'inside/inside-prompts-1.png',
        'next1': 'inside/cartoons/cartoons1_b.png',
    },
    'inside/cartoons/cartoons1_b.png': {
        'prev': 'inside/cartoons/cartoons1_a.png',
        'next1': 'inside/cartoons/cartoons1_c.png',
    },
    'inside/cartoons/cartoons1_c.png': {
        'prev': 'inside/cartoons/cartoons1_b.png',
        'next1': 'inside/inside-game-over.png',
    },
    # cook breakfast
    'inside/breakfast/kitchen.png': {
        'prev': 'inside/inside-prompts-2.png',
        'next1': 'inside/breakfast/kitchen2.png',
    },
    'inside/breakfast/kitchen2.png': {
        'prev': 'inside/breakfast/kitchen.png',
        'next1': 'inside/breakfast/kitchen3.png',
    },
    'inside/breakfast/kitchen3.png': {
        'prev': 'inside/breakfast/kitchen2.png',
        'next1': 'inside/breakfast/cabinet-contents.png',
    },
    'inside/breakfast/cabinet-contents.png': {
        'prev': 'inside/breakfast/kitchen3.png',
        'next1': 'inside/breakfast/cabinet-contents-thoughts.png',
    },
    'inside/breakfast/cabinet-contents-thoughts.png': {
        'prev': 'inside/breakfast/cabinet-contents.png',
        'next1': 'inside/inside-game-over.png',
    },
    # do chores
    'inside/chores/trash-compactor1.png': {
        'prev': 'inside/inside-prompts-3.png',
        'next1': 'inside/chores/trash-compactor2.png',
    },
    'inside/chores/trash-compactor2.png': {
        'prev': 'inside/chores/trash-compactor1.png',
        'next1': 'inside/chores/trash-compactor3.png',
    },
    'inside/chores/trash-compactor3.png': {
        'prev': 'inside/chores/trash-compactor2.png',
        'next1': 'inside/inside-game-over.png',
    },
    # game over inside
    'inside/inside-game-over.png': {
        'prev': 'inside/inside-game-over.png',
        'next1': 'open/exposition.png',
    },
    #
    # OUTSIDE
    #
    'outside/walk1.png': {
        'prev': 'open/in-or-out-2.png',
        'next1': 'outside/walk2.png'
    },
    'outside/walk2.png': {
        'prev': 'outside/walk1.png',
        'next1': 'outside/walk-prompt-1.png'
    },
    # school
    'outside/school/school.png': {
        'prev': 'outside/walk-prompt-1.png',
        'next1': 'outside/school/school2.png'
    },
    'outside/school/school2.png': {
        'prev': 'outside/school/school.png',
        'next1': 'outside/school/school3.png'
    },
    'outside/school/school3.png': {
        'prev': 'outside/school/school2.png',
        'next1': 'outside/school/school4.png'
    },
    'outside/school/school4.png': {
        'prev': 'outside/school/school3.png',
        'next1': 'outside/school/school-prompt-1.png'
    },
    'outside/school/sign.png': {
        'prev': 'outside/school/school-prompt-1.png',
        'next1': 'outside/school/sign2.png'
    },
    'outside/school/sign2.png': {
        'prev': 'outside/school/sign.png',
        'next1': 'outside/school/sign3.png'
    },
    'outside/school/sign3.png': {
        'prev': 'outside/school/sign2.png',
        'next1': 'outside/school/sign4.png'
    },
    'outside/school/sign4.png': {
        'prev': 'outside/school/sign4.png',
        'next1': 'outside/school/sign-prompt-1.png'
    },
    'outside/school/vandalize1.png': {
        'prev': 'outside/school/sign-prompt-1.png',
        'next1': 'outside/school/vandalize2.png'
    },
    'outside/school/vandalize2.png': {
        'prev': 'outside/school/vandalize1.png',
        'next1': 'outside/school/vandalize3.png'
    },
    'outside/school/vandalize3.png': {
        'prev': 'outside/school/vandalize2.png',
        'next1': 'outside/school/vandalize4.png'
    },
    'outside/school/vandalize4.png': {
        'prev': 'outside/school/vandalize3.png',
        'next1': 'outside/school/vandalize5.png'
    },
    'outside/school/vandalize5.png': {
        'prev': 'outside/school/vandalize4.png',
        'next1': 'outside/school/vandalize6.png'
    },
    'outside/school/vandalize6.png': {
        'prev': 'outside/school/vandalize5.png',
        'next1': 'outside/school/vandalize7.png'
    },
    'outside/school/vandalize7.png': {
        'prev': 'outside/school/vandalize6.png',
        'next1': 'outside/school/vandalize8.png'
    },
    'outside/school/vandalize8.png': {
        'prev': 'outside/school/vandalize7.png',
        'next1': 'outside/school/vandalize9.png'
    },
    'outside/school/vandalize9.png': {
        'prev': 'outside/school/vandalize8.png',
        'next1': 'outside/school/vandalize10.png'
    },
    'outside/school/vandalize10.png': {
        'prev': 'outside/school/vandalize9.png',
        'next1': 'outside/school/vandalize11.png'
    },
    'outside/school/vandalize11.png': {
        'prev': 'outside/school/vandalize10.png',
        'next1': 'outside/school/vandalize12.png'
    },
    'outside/school/vandalize12.png': {
        'prev': 'outside/school/vandalize11.png',
        'next1': 'outside/school/vandalize-walk.png'
    },
    'outside/school/vandalize-walk.png': {
        'prev': 'outside/school/vandalize12.png',
        'next1': 'outside/school/vandalize-walk2.png'
    },
    'outside/school/vandalize-walk2.png': {
        'prev': 'outside/school/vandalize-walk.png',
        'next1': 'outside/school/vandalize-walk3.png'
    },
    'outside/school/vandalize-walk3.png': {
        'prev': 'outside/school/vandalize-walk2.png',
        'next1': 'outside/school/game-over.png'
    },
    'outside/school/game-over.png': {
        'prev': 'outside/school/game-over.png',
        'next1': 'open/exposition.png'
    },
    # protest
    'outside/protest/protest.png': {
        'prev': 'outside/walk-prompt-2.png',
        'next1': 'outside/protest/protest2.png'
    },
    'outside/protest/protest2.png': {
        'prev': 'outside/protest/protest.png',
        'next1': 'outside/protest/protest3.png'
    },
    'outside/protest/protest3.png': {
        'prev': 'outside/protest/protest2.png',
        'next1': 'outside/protest/protest-closer-prompt-1.png'
    },
    'outside/protest/protest-closer.png': {
        'prev': 'outside/protest/protest-closer-prompt-1.png',
        'next1': 'outside/protest/protest-closer2.png'
    },
    'outside/protest/protest-closer2.png': {
        'prev': 'outside/protest/protest-closer.png',
        'next1': 'outside/protest/join-protest-prompt-1.png'
    },
    'outside/protest/protest-closer-joined.png': {
        'prev': 'outside/protest/join-protest-prompt-1.png',
        'next1': 'outside/protest/protest-closer-joined2.png'
    },
    'outside/protest/protest-closer-joined2.png': {
        'prev': 'outside/protest/protest-closer-joined.png',
        'next1': 'outside/protest/protest-text1.png'
    },
    'outside/protest/protest-text1.png': {
        'prev': 'outside/protest/protest-closer-joined2.png',
        'next1': 'outside/protest/protest-text2.png'
    },
    'outside/protest/protest-text2.png': {
        'prev': 'outside/protest/protest-text1.png',
        'next1': 'outside/protest/protest-text3.png'
    },
    'outside/protest/protest-text3.png': {
        'prev': 'outside/protest/protest-text2.png',
        'next1': 'outside/protest/protest-firing.png'
    },
    'outside/protest/protest-firing.png': {
        'prev': 'outside/protest/protest-text3.png',
        'next1': 'outside/protest/protest-firing2.png'
    },
    'outside/protest/protest-firing2.png': {
        'prev': 'outside/protest/protest-firing.png',
        'next1': 'outside/protest/protest-firing3.png'
    },
    'outside/protest/protest-firing3.png': {
        'prev': 'outside/protest/protest-firing2.png',
        'next1': 'outside/protest/protest-firing4.png'
    },
    'outside/protest/protest-firing4.png': {
        'prev': 'outside/protest/protest-firing3.png',
        'next1': 'outside/protest/protest-game-over.png'
    },
    'outside/protest/protest-game-over.png': {
        'prev': 'outside/protest/protest-game-over.png',
        'next1': 'open/exposition.png'
    },
    # boardwalk
    'outside/boardwalk/boardwalk1.png': {
        'prev': 'outside/walk-prompt-3.png',
        'next1': 'outside/boardwalk/boardwalk2.png'
    },
    'outside/boardwalk/boardwalk2.png': {
        'prev': 'outside/boardwalk/boardwalk1.png',
        'next1': 'outside/boardwalk/boardwalk3.png'
    },
    'outside/boardwalk/boardwalk3.png': {
        'prev': 'outside/boardwalk/boardwalk2.png',
        'next1': 'outside/boardwalk/boardwalk4.png'
    },
    'outside/boardwalk/boardwalk4.png': {
        'prev': 'outside/boardwalk/boardwalk3.png',
        'next1': 'outside/boardwalk/boardwalk5.png'
    },
    'outside/boardwalk/boardwalk5.png': {
        'prev': 'outside/boardwalk/boardwalk4.png',
        'next1': 'outside/boardwalk/boardwalk-prompt.png'
    },
    'outside/boardwalk/boardwalk-prompt.png': {
        'prev': 'outside/boardwalk/boardwalk5.png',
        'next1': 'outside/boardwalk/boardwalk-prompts-1.png'
    },
    'outside/boardwalk/pier1.png': {
        'prev': 'outside/boardwalk/boardwalk-prompts-1.png',
        'next1': 'outside/boardwalk/pier2.png'
    },
    'outside/boardwalk/pier2.png': {
        'prev': 'outside/boardwalk/pier1.png',
        'next1': 'outside/boardwalk/pier3.png'
    },
    'outside/boardwalk/pier3.png': {
        'prev': 'outside/boardwalk/pier2.png',
        'next1': 'outside/boardwalk/pier4.png'
    },
    'outside/boardwalk/pier4.png': {
        'prev': 'outside/boardwalk/pier3.png',
        'next1': 'outside/boardwalk/pier5.png'
    },
    'outside/boardwalk/pier5.png': {
        'prev': 'outside/boardwalk/pier4.png',
        'next1': 'outside/boardwalk/pier6.png'
    },
    'outside/boardwalk/pier6.png': {
        'prev': 'outside/boardwalk/pier5.png',
        'next1': 'outside/boardwalk/pier7.png'
    },
    'outside/boardwalk/pier7.png': {
        'prev': 'outside/boardwalk/pier6.png',
        'next1': 'outside/boardwalk/pier8.png'
    },
    'outside/boardwalk/pier8.png': {
        'prev': 'outside/boardwalk/pier7.png',
        'next1': 'outside/boardwalk/pier9.png'
    },
    'outside/boardwalk/pier9.png': {
        'prev': 'outside/boardwalk/pier8.png',
        'next1': 'outside/boardwalk/game-over-boardwalk.png'
    },
    'outside/boardwalk/game-over-boardwalk.png': {
        'prev': 'outside/boardwalk/game-over-boardwalk.png',
        'next1': 'open/exposition.png'
    },
}


def getImageFromInput(currImageName, input, goBack):
    if goBack:
        return mappings[currImageName]['prev']
    else:
        return mappings[currImageName][input]

while True:
    if not button_U.value:  # UP joystick is released after pressed:
        # if we are on an options screen
        try:
            # find the next number of option choices and replace it
            nextNum = mappings[showImage]['opt-num'] - 1 
            if nextNum == 0:
                nextNum = mappings[showImage]['total-opt']
            showImage = showImage.replace(str(mappings[showImage]['opt-num']), str(nextNum))
            print("showImage is now: ", showImage)
        except (AttributeError, KeyError):
            pass

    if not button_D.value:  # DOWN joystick is released after pressed:
        # if we are on an options screen
        try:
            # find the next number of option choices and replace it
            nextNum = ( mappings[showImage]['opt-num'] + 1 ) % mappings[showImage]['total-opt']
            if nextNum == 0:
                nextNum = mappings[showImage]['total-opt']
            showImage = showImage.replace(str(mappings[showImage]['opt-num']), str(nextNum))
            print("showImage is now: ", showImage)
        except (AttributeError, KeyError):
            pass

    if not button_A.value:  # A button is released after press
        image2 = getImageFromInput(showImage, 'next1', False)
        showImage = image2

    if not button_B.value:  # B button is released after press
        showImage = getImageFromInput(showImage, '', True)

    else:
        # Display image.
        temp = Image.open(stem + showImage).resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
        disp.image(temp)
    disp.show()