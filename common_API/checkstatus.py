import os, shutil
import time

def createShortcut(startupPath):
    shutil.copy(r"./checkStatus.exe", startupPath)

def saveTxt(res):
    f = open(r"./result.txt", "w")
    f.write(res)
    f.close()

# Judge sample whether support OPAL feature
def determineOPAL(resultList, beforeEncrypt, afterEncrypt):
    # get status val
    val = resultList[5].split(":")[1].strip()
    # print(val)
    # print(resultList[5])
    if beforeEncrypt == True :
        if val == "0x0" :
            print("Support OPAL")
        else :
            print("Don't support OPAL")
            return False
    elif afterEncrypt == True :
        if val == "0x6" or val == "0x7" :
            print("PASS")
            res = "PASS"
            # saveTxt(res)
        else :
            print("FAIL")
            res = "FAIL"
            # saveTxt(res)
            return False

def getTimestamp():
    # Setting timeStamp    
    struct_time = time.localtime()
     # Transfer string
    timeString = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
    print(timeString)
    
    return timeString

def checkStatus(encryptBefore, encryptAfter):
    os.system('WMTCGTST_8.6.0.188.exe -i > result.txt')         
    
    getTimestamp()
    f = open("./result.txt", "r")
    output = f.read()
    print(output)
    f.close()

    f = open("./result.txt", "r")

    lines = f.readlines()
    resultList = lines
    f.close()
    
    if encryptBefore == True:
        determineOPAL(resultList, beforeEncrypt=True, afterEncrypt=False)
    elif encryptAfter == True:
        determineOPAL(resultList, beforeEncrypt=False, afterEncrypt=True)

  