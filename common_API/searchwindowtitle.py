import threading
import time
import os
import websocket
import pyautogui
import win32com.client
import json
import ssl
import sys
import subprocess
from win32 import win32gui

def leftClickForegroundWindow(left, top, right, bottom, hwnd):
    # Calculate coordinate for event button
    x = int(left+(right-left)/2)
    y = int(top+(bottom-top)/2)         
    print("Coordinate(%d, %d)" %(x, y))
    
    # Move to specific coordinate by mouse
    pyautogui.moveTo(x, y)  

    # Left click by mouse left
    pyautogui.click(x, y)  
    print('Left Click')

def searchWindowTitle(target):
    titleHwnd = 0
    def win_enum_callback(hwnd, results):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
            results.append(hwnd)

    handles = []
    win32gui.EnumWindows(win_enum_callback, handles)

    for h in handles :
        if win32gui.GetWindowText(h) == target :
            print('\n'.join(['%d\t%s' % (h, win32gui.GetWindowText(h)) for h in handles]))
            titleHwnd = h
    print(handles)
    print(titleHwnd)
    
    # Continue polling util secureDoc jump window
    if titleHwnd == 0 :                
        print("Waiting for 15 seconds")
        time.sleep(15)        
        searchWindowTitle(target)    
    else :
        # Set fore ground secureDoc tool
        print("Waiting for 5 seconds")
        time.sleep(5)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        print(titleHwnd)
        win32gui.SetForegroundWindow(titleHwnd)
        
        # Click title to confirm in tool
        left, top, right, bottom = win32gui.GetWindowRect(titleHwnd)
        print(left, top, right, bottom)
        
        # Click left event by mouse
        leftClickForegroundWindow(left, top, right, bottom, titleHwnd)