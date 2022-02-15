import sys
import os
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

def main() :
    #installSecureDocTool()
    settingPWD()

if __name__ == "__main__" :
    main()