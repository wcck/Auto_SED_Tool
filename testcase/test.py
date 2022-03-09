import checkstatus


def runTestCase():
    checkstatus.checkStatus(encryptBefore=False, encryptAfter=True)

if __name__ == "__main__" :
    runTestCase()