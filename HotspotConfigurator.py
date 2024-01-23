import time
import pyautogui
import os
from dotenv import load_dotenv

load_dotenv()

ssid = os.getenv("SSID")
password = os.getenv("PASSWORD")

def click_serie(coordinate_list):
    for x, y in coordinate_list:
        time.sleep(0.01)
        pyautogui.click(x, y)

def configure_hotspot(ssid, password):
    try:
        os.startfile("ms-settings:Mobile Hotspot")
        time.sleep(0.01)
        pyautogui.hotkey("winleft", "up")
        click_serie([(95, 110), (1670, 350), (140, 700)])
        time.sleep(1.49)
        click_serie([(590, 550), (1310, 685)])
        time.sleep(0.01)
        pyautogui.write(ssid)
        click_serie([(1310, 820), (1310, 820)])
        time.sleep(0.01)
        pyautogui.write(password)
        click_serie([(1310, 950)])
        time.sleep(0.01)
        pyautogui.press('2')
        time.sleep(0.01)
        pyautogui.press('enter')
        click_serie([(1100, 1040), (560, 210)])
        time.sleep(0.01)
        pyautogui.hotkey('alt', 'f4')
    except Exception as e:
        print("Error:", e)

if __name__=='__main__':   
    configure_hotspot(ssid, password)