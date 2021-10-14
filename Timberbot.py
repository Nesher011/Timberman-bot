import pyautogui
import time

class TimberBot:    
    def make_screenshot(self):
        self.image = pyautogui.screenshot('my_screenshot.png', region=(915,600,90,2))

    @staticmethod
    def check_branch(image):
        rgb_left=image.getpixel((1,1))
        rgb_right=image.getpixel((88,1))
        if rgb_left[0]<15 and rgb_left[1]<15 and rgb_left[2]<15 and rgb_right[0]<15 and rgb_right[1]<15 and rgb_right[2]<15:
            return "None"
        elif rgb_left[0]>15 or rgb_left[1]>15 or rgb_left[2]>15:
            return "Left"
        elif rgb_right[0]>15 or rgb_right[1]>15 or rgb_right[2]>15:
            return "Right"
        else:
            return "None"

    def run(self):
        last_pressed_left=True
        while True:
            self.make_screenshot()
            side=TimberBot.check_branch(self.image)
            if side=="Left":
                pyautogui.press('right', presses=2, interval=0.01)
                last_pressed_left=False
            elif side=="Right":
                pyautogui.press('left', presses=2, interval=0.01)
                last_pressed_left=True
            else:       
                if last_pressed_left:
                    pyautogui.press('left')
                else:
                    pyautogui.press('right')
            time.sleep(0.01)

if __name__=='__main__':
    timberBot=TimberBot()
    timberBot.run()