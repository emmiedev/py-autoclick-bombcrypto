#!/usr/bin/python3

import os, time, json
#****************************************************************************************#

try:
    import pyautogui
except :
    print('คุณยังไม่มี Library pyautogui. เดี๋ยวเราจะทำการติดตั้งให้คุณเอง')
    os.system('pip install pyautogui')
    import pyautogui

try:
    from colorama import init, Fore, Style
except :
    print('คุณยังไม่มี Library colorama. เดี๋ยวเราจะทำการติดตั้งให้คุณเอง')
    os.system('pip install colorama')
    from colorama import init, Fore, Style
    
try:
    import threading
except :
    print('คุณยังไม่มี Library threading. เดี๋ยวเราจะทำการติดตั้งให้คุณเอง')
    os.system('pip install threading')
    import threading
    
#****************************************************************************************#

init()
os.system('clear')
print(Fore.CYAN + '*********************************************************************\n' + Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX + "Hello, I'm EmmieDev. วันนี้ฉันว่างเลยมานั่งทำ Autoclick แบบโง่ๆใช้เล่นๆ\n" + Style.RESET_ALL)
print(Fore.RED + 'ท่านผู้เจริญทั้งหลายสามารถบริจาคสนับสนุนได้ที่\n' + Style.RESET_ALL)
print(Fore.GREEN + 'Wallet Address (BSC):0x55dBA6cb9eA827D518FfDEcF92f2c706A803581e\n' + Style.RESET_ALL)
print(Fore.CYAN + '*********************************************************************\n\n' + Style.RESET_ALL)

print(Fore.LIGHTGREEN_EX + 'มาเริ่มกันเลย. . .\n')

def run_click(pos):
    pyautogui.moveTo(int(pos["x"]), int(pos["y"]))
    pyautogui.click()

class keep_state (threading.Thread):
    def __init__(self, threadID, name, timer, pos):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.timer = timer
        self.pos = pos
    def run(self):
        while True:
            print(Fore.RED + '[ระบบ Active Windows กำลังทำงาน]\n' + Style.RESET_ALL)
            pyautogui.moveTo(self.pos["x"], self.pos["y"])
            pyautogui.click()
            time.sleep(self.timer)
            print('ACTIVE')
      
json_data = json.load(open('./config.json'))
# thread1 = keep_state(1, "keep-up-1", 600, json_data["close_btn_pos"]).start()
time.sleep(2)

while True:
    pos_name_list = ["refresh_btn", "connect_btn_pos","sign_bnt_pos", "start_game", "get_bomber_pos","get_bomber_pos", "all_work_btn_pos", "close_btn_pos", "close_btn_pos"]
    status_list = [ "Refreshing. . .", "Connecting", "Signing","Starting . . .", "กำลังเปิดไอคอนตัวละคร", "กำลังเปิดรายการตัวละคร", "กำลังกดปุ่มสั่งให้ทุกตัวทำงาน", "กำลังปิดหน้าต่างตัวละคร", "เรียบร้อย!! น้อง ๆ ออกมาวิ่งกันแล้ว"]
    for index, item in enumerate(pos_name_list):
        print(Fore.LIGHTBLUE_EX + status_list[index])
        run_click(json_data[item])
        if item == "connect_btn_pos":
            time.sleep(10)
        if item == "sign_bnt_pos":
            time.sleep(30)
        if item == "start_game":
            time.sleep(5)
        if item == "refresh_btn":
            time.sleep(15)
        else:
            time.sleep(2)
    print(Fore.RED + 'กำลังหน่วงเวลา '+str(json_data["loop_time"])+' นาที' + Style.RESET_ALL)
    time.sleep(json_data["loop_time"] * 60)
