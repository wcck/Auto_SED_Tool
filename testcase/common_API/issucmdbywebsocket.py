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

# Global variable.
commandList = []
delayMsList = []

def parserJsonFile(filePath):
    print("*********** Parser start ***********")
    with open(filePath, newline="") as f:         
        # Load json file
        data = json.load(f)
        print(len(data))
        
        # Transfer '' to ""
        for i in range(len(data)):            
            commandList.append(json.dumps(data[i]))
            print(commandList[i])
            if "millis" in commandList[i]: 
                # Get delay ms
                delayMs = commandList[i].split("millis")[1].split(":")[1].strip("}'}'").strip()
                delayMs = int(delayMs)/1000
                print("delay ms is : %d" %(delayMs))
                delayMsList.append(delayMs)

    print("*********** Parser End ***********")
    f.close()

def sendCommand(remoteIP):   
    print("*********** Send CMD Start ***********") 
    uri = "wss://%s/api/ws?stream=0" %(remoteIP)
    headers = {"X-KVMD-User": "admin", "X-KVMD-Passwd": "admin"}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
    print(ssl.CERT_NONE)

    # Conncet to PiKVM server
    res = ws.connect(uri, header=headers)
    if res == False:
        print('[ERROR] Cannot connect this Web UI.')
        sys.exit()
    
    # Send command
    j = 0
    for i in range(len(commandList)):
        try:
            if "millis" in commandList[i]: 
                print("Sleep %d Second" %(delayMsList[j]))
                time.sleep(delayMsList[j])                
                j = j + 1
            
            ws.send(commandList[i])
            print("Send CMD : %s" %(commandList[i]))
        # Prevent WinError 10054
        except:
            # Sleep 5 seconds
            print("Enter exception and then sleep 5 seconds.")
            time.sleep(5)
            
            # Re-Connect host
            ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
            print(ssl.CERT_NONE)

            # Conncet to PiKVM server
            res = ws.connect(uri, header=headers)
            if res == False:
                print('[ERROR] Cannot connect this Web UI.')
                sys.exit()
    
    # Clear list avoid repeat sending CMD
    commandList.clear()     
    # Close websocket
    ws.close()
    print("*********** Send CMD End ***********") 

def issueEventByWebSocket(ip, macro) :    
    parserJsonFile(macro)    
    sendCommand(ip)