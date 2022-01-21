import cv2
import pyautogui
from time import sleep as sleep
from subprocess import call

# def find_to_click(img, screen):
def find_to_click(img):
    # call(["screencapture", "screenshot.png"])
    # image = pyautogui.screenshot()
    image= cv2.imread(pyautogui.screenshot())
    # image= cv2.imread(screen)
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    template= cv2.imread('img_recog/'+ img,0)
    result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)
    height, width= template.shape[:2]
    Ax = max_loc[0]
    Ay = max_loc[1]
    center = (((width/2)+(Ax))/2,(((height/2)+Ay))/2)
    pyautogui.click(center)

browser_refresh_cord = (85,85) # ตำแหน่งปุ่มรีเฟรช
while True:
    image_list = ['active_windows.png', 'connect_wallet.png', 'metamask_sign.png', 'show_heros.png', 'all_work.png', 'close_btn.png', 'treasure_hunt.png']
    pyautogui.click(1022, 565)
    pyautogui.click(browser_refresh_cord)
    # find_to_click('refresh_btn.png')
    sleep(10)
    for index, img_file in enumerate(image_list):
        if index <= 1:
            sleep(2)
        if index == 2:
            sleep(12)
        if index == 3:
            sleep(50)
        if index > 3:
            sleep(2)
            
        # find_to_click(img_file, str(index)+'.png')
        find_to_click(img_file)
    sleep(120*60)