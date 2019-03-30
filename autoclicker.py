#!/usr/bin/python3
import pyautogui, time, random, threading

def auto_key_presser():
    while True:
        # find image on screen. Confidence calls for machine learning :) (Actually not machine learning :( )
        hospoda = pyautogui.locateOnScreen('resources/hospoda.png', confidence=.9, grayscale=True)
        dobrodruzstvi = pyautogui.locateOnScreen('resources/dobrodruzstvi.png', confidence=.9, grayscale=True)
        konec_boje = None
        level_up = None
        preskocit = None
        random_number = random.randrange(0,1)

        if hospoda != None:
            print("Hospoda - 2x Enter")
            time.sleep(3 * random_number)
            pyautogui.typewrite(["enter","enter"], interval=2 * random_number)
        elif dobrodruzstvi != None:
            print("Dobrodruzstvi - Sleep 25")
            time.sleep(25)
        else:
            preskocit = pyautogui.locateOnScreen('resources/preskocit.png', confidence=.9, grayscale=True)
            konec_boje = pyautogui.locateOnScreen('resources/ok_after_fight.png', confidence=.9, grayscale=True)

            if konec_boje != None:
                print("Boj dokončen - Enter")
                pyautogui.typewrite(["enter"])
            elif preskocit != None:
                print("Preskocit - Enter")
                pyautogui.typewrite(["enter"])
            else:
                level_up = pyautogui.locateOnScreen('resources/level_up.png', confidence=.9, grayscale=True)
                if level_up != None:
                    print("Level up - Escape")
                    pyautogui.typewrite(["escape"])
                else:
                    print("Not found")
        time.sleep(.5)
#auto_key_presser()
def mouse_mover():
    pyautogui.moveTo(400, 150)
    while True:
        pyautogui.moveRel(100, None,20)
        pyautogui.moveRel(-100, None,20)

#mouse_mover()
if __name__ == "__main__":
    threading.Thread(target = auto_key_presser).start()
    threading.Thread(target = mouse_mover).start()