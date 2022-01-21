import random, pyautogui


FIRST_ROW = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
SECOND_ROW = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
PIXEL_X = [x for x in range(0, 1920)]
PIXEL_Y = [y for y in range(0, 1080)]
DURATION = [0.2, 0.25, 0.27, 0.21, 0.41, 0.45, 0.69, 0.31, 1.2, 0.7, 0.6]


# нажимаем кнопочки
def press():
    while True:
        pyautogui.press('{}'.format(random.choice(FIRST_ROW)))
        pyautogui.sleep(1)
        pyautogui.press('{}'.format(random.choice(SECOND_ROW)))


# если хочешь еще и двигать мышкой
def mouse_movement():
    while True:
        x, y = random.choice(PIXEL_X),random.choice(PIXEL_Y)
        x1, y1 = random.choice(PIXEL_X), random.choice(PIXEL_Y)
        duration_random_first = random.choice(DURATION)
        duration_random_second = random.choice(DURATION)
        pyautogui.moveTo(x, y, duration=duration_random_first)
        pyautogui.moveTo(x1, y1, duration=duration_random_second)
        pyautogui.sleep(random.choice([1, 2, 3, 4, 5]))
        pyautogui.click(button='right')
        pyautogui.sleep(1)
        pyautogui.press('esc')


if __name__ == '__main__':
    mouse_movement()
    # press()
