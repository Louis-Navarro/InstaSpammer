import json
import pdb
import random
import string
import time

import keyboard
from autopy import key, mouse

ALPHABET = string.ascii_lowercase + string.digits


def load_positions(fn):
    with open(fn) as fp:
        data = json.load(fp)

    return data


def create_message(length=1_000):
    msg = random.choices(ALPHABET, k=length)
    return ''.join(msg)


def main():
    positions = load_positions('positions.json')

    print(positions)

    print('[*] Press ENTER when ready to launch the bot [*]')
    input()

    print('[*] Press ESCAPE when you want to stop the bot [*]')

    try:
        while not keyboard.is_pressed('esc'):
            msg = create_message(100)
            for pos in positions:
                mouse.move(*pos)
                mouse.click()
                keyboard.write(msg)
                # pdb.set_trace()
                time.sleep(.2)
                key.tap(key.Code.RETURN)

    except:
        print('[*] Stopping the bot [*]')
        print('Goodbye !')


if __name__ == '__main__':
    main()
