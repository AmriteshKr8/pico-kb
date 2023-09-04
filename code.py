import board
import keypad
import time
from adafruit_hid.keyboard import Keyboard
import usb_hid
from adafruit_hid.keycode import Keycode
import digitalio

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

space = digitalio.DigitalInOut(board.GP19)
space.direction = digitalio.Direction.INPUT
space.pull = digitalio.Pull.UP

k = keypad.KeyMatrix(
    row_pins=(board.GP17, board.GP20, board.GP8, board.GP21, board.GP14, board.GP16),
    column_pins=(board.GP18, board.GP15, board.GP13, board.GP12, board.GP10, board.GP9, board.GP6, board.GP3, board.GP2, board.GP1),
)
kbd = Keyboard(usb_hid.devices)

layout = [
    Keycode.ESCAPE,Keycode.LEFT_BRACKET,Keycode.RIGHT_BRACKET,Keycode.BACKSLASH,Keycode.FORWARD_SLASH,Keycode.COMMA,Keycode.PERIOD,Keycode.QUOTE,Keycode.SEMICOLON,Keycode.GRAVE_ACCENT,
    Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,
    Keycode.Q, Keycode.W, Keycode.E, Keycode.R, Keycode.T, Keycode.Y, Keycode.U, Keycode.I, Keycode.O, Keycode.P,
    Keycode.A, Keycode.S, Keycode.D, Keycode.F, Keycode.G, Keycode.H, Keycode.J, Keycode.K, Keycode.L,Keycode.CAPS_LOCK,
    Keycode.LEFT_ALT,Keycode.UP_ARROW,Keycode.Z, Keycode.X, Keycode.C, Keycode.V, Keycode.B, Keycode.N, Keycode.M,Keycode.SHIFT,
    Keycode.LEFT_ARROW,Keycode.DOWN_ARROW,Keycode.RIGHT_ARROW,Keycode.BACKSPACE,Keycode.TAB,Keycode.MINUS,Keycode.EQUALS,Keycode.GUI,Keycode.CONTROL,Keycode.ENTER 
]

while True:
    key_event = k.events.get()
    if key_event:
        if key_event.pressed: # and key_event.key_number == 40:
            kbd.press(layout[key_event.key_number])
            if key_event.key_number == 39:
                led.value = not led.value
        else:
            kbd.release(layout[key_event.key_number])
    if space.value == 0:
        kbd.press(Keycode.SPACE)
    else:
        kbd.release(Keycode.SPACE)
    time.sleep(0.1)
