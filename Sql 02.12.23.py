import sqlite3
filename='c:\\Zmeya\\base.sqlite'
conn = sqlite3.connect(filename)
cursor = conn.cursor()

print('update:')  
cursor.execute("SELECT Name FROM Customer JOIN Invoice ON Customer.CustomerId=Invoice.CustomerId JOIN InvoiceLine ON Invoice.InvoiceId=InvoiceLine.InvoiceId JOIN Track ON InvoiceLine.TrackId=Track.TrackId WHERE Customer.CustomerId=41")
results4 = cursor.fetchall()
conn.commit()
print(results4)