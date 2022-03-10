from common_API import checkstatus, searchwindowtitle, issucmdbywebsocket, connectdb
import threading
import time
import os
import subprocess

print("Run Verify SecureDoc Client and PreBoot Installation")

def installSecureDocTool() :
    # Get tool path
    SEDPath = os.path.join(os.path.expandvars("%userprofile%"), "Desktop", "SED_Offline_8.6_SR1", "SecureDoc_64.exe")
    print(SEDPath)
    
    # Install SecureDoc_64.exe
    os.startfile(SEDPath)

def runColdBoot():
    # Run cold boot    
    coldBootPath = os.path.join(os.path.expandvars("%userprofile%"), "Desktop", "Auto_SED_Tool", "coldboot", "coldboot.bat")
    subprocess.call([coldBootPath])

def RunCase4():
    # # Check Status for DUT
    res = checkstatus.checkStatus(encryptBefore=False, encryptAfter=True)
	# if res == False:
    #     return False
    
    # # Install SecureDoc Tool in Desktop
    installSecureDocTool()        

    # Show tool and Click it
    target = "SecureDoc: Set Device Primary Owner Credentials"
    searchwindowtitle.searchWindowTitle(target, delayTime)   
    # Issue event by web UI i.e. confirm pwd
    remoteIP = "192.168.54.64"
    macroPath = r"./macro/secureDocPWD.json"
    issucmdbywebsocket.issueEventByWebSocket(ip = remoteIP, macro=macroPath)
    print("Waiting for encryption....")

    # Press Cancel for secureDoc
    target = "SecureDoc Disk Encryption"    
    searchwindowtitle.searchWindowTitle(target, delayTime)
    print("Encryption Done!")    
    # Issue event by web UI i.e. press tab
    macroPath = r"./macro/pressTab.json"
    issucmdbywebsocket.issueEventByWebSocket(ip = remoteIP, macro=macroPath)
    macroPath = r"./macro/pressEnter.json"
    issucmdbywebsocket.issueEventByWebSocket(ip = remoteIP, macro=macroPath)

    # Press OK
    target = "SecureDoc"
    searchwindowtitle.searchWindowTitle(target, delayTime) 
    # Issue event by web UI i.e. press enter
    macroPath = r"./macro/pressEnter.json"
    issucmdbywebsocket.issueEventByWebSocket(ip = remoteIP, macro=macroPath)

    # Connect DB and update table
    connectRes = connectdb.connectDB()
    targetTable = u'John_Test'
    id = 1
    val = 1
    connectdb.updatePreShutdownData(connectRes, targetTable, val, id)

    # Run coldboot.bat 
    thread_cold_boot = threading.Thread(target=runColdBoot)
    thread_cold_boot.start()
    time.sleep(6)
    macroPath = r"./macro/pressTab.json"
    issucmdbywebsocket.issueEventByWebSocket(ip = remoteIP, macro=macroPath)
    macroPath = r"./macro/pressTab.json"
    issucmdbywebsocket.issueEventByWebSocket(ip = remoteIP, macro=macroPath)
    macroPath = r"./macro/pressEnter.json"
    issucmdbywebsocket.issueEventByWebSocket(ip = remoteIP, macro=macroPath)


if __name__ == "__main__" :
    # Global variable.
    retry  = 0
    commandList = []
    delayMsList = []
    delayTime = 5
    RunCase4()