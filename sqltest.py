import pyodbc

driver= '{ODBC Driver 17 for SQL Server}'

server = 'dbtest0526.database.windows.net'
database = 'dbtest'
username = 'ojh75880367'
password = '$ojh1902417'   

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("select * from dbo.azureex$")
        #row = cursor.fetchone()
        row = cursor.fetchall()
        #while row:
        #    print (str(row[0]) + " " + str(row[1]))
        #    row = cursor.fetchone()    
        for data in row:
            print(data)