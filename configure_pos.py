import sys
import json

import mouse
import keyboard


def hotkey(data):
    pos = mouse.get_position()
    print(f'Added {pos}')
    data.append(pos)


def stop(data):
    print(f'Saving {data}')

    with open('positions.json', 'w') as fp:
        json.dump(data, fp)


def main():
    data = []
    keyboard.add_hotkey('alt+c', hotkey, args=(data, ))

    keyboard.wait('esc')
    print('Stopping program')
    stop(data)


if __name__ == '__main__':
    main()
