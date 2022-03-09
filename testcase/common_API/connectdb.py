import pyodbc 

def insertData(connectRes):
    cursor = connectRes.cursor()
    
    uid = 1    
    ip = u'175.198.42.19'
    PrepareShutdown = 0
    TestCase = 7

    # Insert
    insertSQLCMD =  "INSERT INTO John_Test(UID, IP, PrepareShutdown, TestCase) \
        VALUES (?, ?, ?, ?)"
    
    cursor.execute(insertSQLCMD, uid, ip, PrepareShutdown, TestCase)
    # Commit the transaction
    connectRes.commit()

def deleteData(connectRes, targetTable, deleteItem, val):
    cursor = connectRes.cursor()

    # Delete
    deleteSQLCMD = "DELETE FROM {0} WHERE {1} in (?)".format(targetTable, deleteItem)
    cursor.execute(deleteSQLCMD, val)
    
    # Commit the transaction
    connectRes.commit()

def updatePreShutdownData(connectRes, targetTable, id, val):
    cursor = connectRes.cursor()

    # Update
    updateSQLCMD = "UPDATE {0} SET PrepareShutdown = {1} WHERE UID = {2}".format(targetTable, val, id)
    cursor.execute(updateSQLCMD)

    # Commit the transaction
    connectRes.commit()

def getPreShutdownData(connectRes):
    cursor = connectRes.cursor()
    
    getFirstSQLCMD = "SELECT * FROM John_Test WHERE UID = 1 and PrepareShutdown = 1"
    cursor.execute(getFirstSQLCMD)

    # Get first data   
    result = cursor.fetchone()
    # print(result)
    if result == None:
        print("Didn't prepare shutdown.")
        return False
    else:
        print("Do prepare shutdown.")
        return True

def searchTable(connectRes, target):
    cursor = connectRes.cursor()
    cursor.execute(target)

    # Print table data
    for data in cursor:
        print('data = %r' % (data,))



def connectDB():
    connectRes = pyodbc.connect("DRIVER={{SQL Server}};SERVER={0}; database={1}; \
       trusted_connection=no;UID={2};PWD={3}".format("172.29.1.1", "WS_DB", "WHATS", "D63Whats"))
    
    # target = 'SELECT * FROM John_Test'
    # targetTable = u'John_Test'
    # # prepareShutdownStatus = prepareShutdown = 1
    # id = 1
    # deleteItem = u'UID'
    # val = 1

    # # insertData(connectRes)
    # updatePreShutdownData(connectRes, targetTable, id, val=1)
    # searchTable(connectRes, target)
    # getPreShutdownData(connectRes)
    # print("****************************************")
    # # deleteData(connectRes, targetTable, deleteItem, val)
    # # searchTable(connectRes, target)
    # # print("****************************************")
    # updatePreShutdownData(connectRes, targetTable, id, val=0)
    # searchTable(connectRes, target)
    # print("****************************************")
    # getPreShutdownData(connectRes)
    
    return connectRes

    
def run():
    connectDB()


if __name__ == "__main__" :
    run()