import pandas as pd
import csv, sys
import sqlite3


data0 =pd.read_csv( 'shipping_data_0.csv')
data1=pd.read_csv("shipping_data_1.csv")
data2=pd.read_csv("shipping_data_2.csv")

print(data0.head(5),'\n',data1.head(5),'\n',data2.head(5),'\n')
print(data1.columns)

origin_warehouse = []
destination_store = []
driver_identifier = []

for i in data1['shipment_identifier']:
    count = 0
    for j in data2['shipment_identifier']:
        if i==j:
            origin_warehouse.append(data2.iloc[count, 1])
            destination_store.append(data2.iloc[count, 2])
            driver_identifier.append(data2.iloc[count, 3])
        count+=1


print(origin_warehouse,'\n',destination_store,'\n',driver_identifier)

data1["origin_warehouse"]=origin_warehouse
data1["destination_store"]=destination_store
data1["driver_identifier"]=driver_identifier


print(data1.columns)
print(data1["origin_warehouse"],data1["destination_store"],data1["driver_identifier"])

data1.to_csv("data1.csv", index=False)


'''creating the shipment details table'''
conn = sqlite3.connect ("shipment_database.db")
c = conn.cursor ()
#Creating Table 1 from shipping_data0
c.execute ("CREATE TABLE IF NOT EXISTS shipment_Details(origin_warehouse  TEXT,destination_store TEXT, product TEXT, on_time BOOLEAN, product_quantity INTEGER, driver_identifier TEXT NOT NULL PRIMARY KEY )")
#creating Table 2 from combining shipping_data1 and shipping_data2 to form data1.csv
c.execute ("CREATE TABLE IF NOT EXISTS shipment_Details1(shipment_identifier  TEXT,product TEXT, on_time BOOLEAN, origin_warehouse TEXT, destination_store TEXT, driver_identifier TEXT, FOREIGN KEY(driver_identifier) REFERENCES shipment_Details(driver_identifier))")
conn.commit ()
conn.close ()

with open('shipping_data_0.csv', newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
            conn = sqlite3.connect("shipment_database.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO shipment_Details VALUES(?, ?, ? ,? ,? ,?)", row)
            conn.commit()
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format('shipping_data_0.csv', reader.line_num, e))

with open('data1.csv', newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
            conn = sqlite3.connect("shipment_database.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO shipment_Details1 VALUES(?, ?, ? ,? ,? ,?)", row)
            conn.commit()
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format('data1.csv', reader.line_num, e))

conn = sqlite3.connect ("shipment_database.db")
c = conn.cursor ()
c.execute(" SELECT shipment_Details1.shipment_identifier, shipment_Details.product_quantity FROM shipment_Details1 INNER JOIN shipment_Details ON shipment_Details1.driver_identifier=shipment_Details.driver_identifier;")
conn.commit ()