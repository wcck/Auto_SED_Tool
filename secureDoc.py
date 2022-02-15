import sys
import os
import time
from pynput.keyboard import Key, Controller
from win32 import win32gui


def installSecureDocTool() :
    # Get tool path
    SEDPath = r"C:\Users\User\Desktop\SED_Offline_8.6_SR1\SecureDoc_64.exe"
    
    # Install SecureDoc_64.exe
    os.startfile(SEDPath)
    
    # Waiting for tool appear


def settingPWD() :
    # Get hwnd for SecureDoc x64
    titleHwnd = 0
    titleHwnd  = win32gui.FindWindow("Qt5QWindowIcon", "SecureDoc: Set Device Primary Owner Credentials")
    print(titleHwnd)

    # Trigger button events
    child = []   
    def all_ok(hwnd, parm):
        child.append(hwnd)
        ClassName = win32gui.GetClassName(hwnd)
        title = win32gui.GetWindowText(hwnd)
        print("title : %s, class : %s, hwnd : %d" %(title, ClassName, hwnd))

    #
    # while(True):
    #     win32gui.EnumChildWindows(titleHwnd, all_ok, None)

    # Type pwd -> Tab -> Confirm pwd -> Tab -> Enter
    keyboard = Controller()
    # passWordKeys = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # time.sleep(5)
    # print("Waiting for 5 secnods")
    # for i in range(len(passWordKeys)) :
    #     keyboard.press(passWordKeys[i])
    #     keyboard.release(passWordKeys[i])
    
    time.sleep(5)
    print("Waiting for 5 secnods")

    keyboard.type("123456789")

    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.release(Key.tab)

    keyboard.type("123456789")
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.release(Key.tab)

    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)



def main() :
    #installSecureDocTool()
    settingPWD()

if __name__ == "__main__" :
    main()