import pyautogui
import time

#For some reasons when this is written in one function pyautogui 
# wait with click until all other function commands are completed. 
# dividing that beetween two functions resolve that issue.


def click_desktop_button_on_taskbar():
	x, y = pyautogui.size()    # SCREEN SIZE
	pyautogui.moveTo(x-5,y-5)   # POSIITION OF PIXELS IN RIGHT DOWN CORNER -5PIXELS TO PREVENT FAILSAFE MECHANISM OF PYAUTOGUI
	pyautogui.click()

def other_pyautogui_commands(): #SOME OTHER PYAUTOGUI COMMANDS
	pyautogui.moveTo(500,500)
	time.sleep(1)
	pyautogui.moveTo(10,10)
	time.sleep(1)
	pyautogui.moveTo(500,500)
	time.sleep(1)
	
click_desktop_button_on_taskbar()
other_pyautogui_commands()
