import random, pyautogui, time


FIRST_ROW = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
SECOND_ROW = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
DURATION = [0.2, 0.25, 0.27, 0.21, 0.41, 0.45, 0.69, 0.31, 1.2, 0.7, 0.6]
STEP_SWICHING = [x for x in range(0, 11)]


# определяем размер экрана для генерации переменных PIXEL_X, PIXEL_Y
def size_window():
    width, height = pyautogui.size()
    pixel_x = [x for x in range(0, width)]
    pixel_y = [y for y in range(0, height)]
    return pixel_x, pixel_y


# нажимаем кнопочки
def press():
    while True:
        pyautogui.press('{}'.format(random.choice(FIRST_ROW)))
        pyautogui.sleep(1)
        pyautogui.press('{}'.format(random.choice(SECOND_ROW)))


# горячие клавиши
def press_hot_key():
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(1)


# если хочешь еще и двигать мышкой
def mouse_movement(pixel_x, pixel_y):
    step_now = 0  # колличество циклов сделанных на данный момент
    while True:
        step = random.choice(STEP_SWICHING)
        x, y = random.choice(pixel_x), random.choice(pixel_y)
        x1, y1 = random.choice(pixel_x), random.choice(pixel_y)
        duration_random_first, duration_random_second = random.choice(DURATION), random.choice(DURATION)
        pyautogui.moveTo(x, y, duration=duration_random_first)
        pyautogui.moveTo(x1, y1, duration=duration_random_second)
        pyautogui.sleep(random.choice([1, 2, 3, 4, 5]))
        pyautogui.click(button='right')
        pyautogui.sleep(1)
        pyautogui.press('esc')
        step_now += 1
        if step_now >= step:
            press_hot_key()


if __name__ == '__main__':
    width_window, height_window = size_window()
    mouse_movement(width_window, height_window)

