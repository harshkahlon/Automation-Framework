import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=sqlref1;'
                      'Database=Smart;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('EXEC Smart.accumulator.usp_Master @FacilityID = 4552')

print('Completed')

# for row in cursor:
#     print(row)