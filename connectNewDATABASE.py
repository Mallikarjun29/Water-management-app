import mysql.connector as mysql
conn=mysql.connect(
  host="10.21.163.236",
  database="new_water_dashboard",
  user="root",
  password="realtime123")
mycursor = conn.cursor()
file = open('data.txt', "a+")
import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(3)
Node,Flow_A,Flow_B,Level= (0 for i in range(4))
try:
    while(True):
        line = ser.readline()
        Node,Flow_A,Flow_B,Level= (0 for i in range(4))
        if line:
            try:
                s = line.decode()
                ss=s.strip()
                print(ss)
                dt_string = time.strftime("%d/%m/%Y %H:%M:%S")
                try:
                    if ss[0]=='$':
                        Node= ss[1]
                        x=ss[3:]
                        x+='b'
                        y=''
                        z=1
                        for i in x:
                            if i.isnumeric() and z==1:
                                y+=i
                            elif z==1:
                                Flow_A=int(y)
                                y=''
                                z=2
                            elif z==2 and i.isnumeric():
                                y+=i
                            elif z==2:
                                Flow_B=int(y)
                                y=''
                                z=3
                            elif z==3 and i.isnumeric():
                                y+=i
                            elif z==3:
                                Level=int(y)
                                
                        sql = "INSERT INTO water_table (Date_time,Node,Flow_A,Flow_B,Level) VALUES (%s,%s,%s,%s,%s)"
                        val =  (dt_string,Node,Flow_A,Flow_B,Level)
                        mycursor.execute(sql, val)
                        conn.commit()
                except IndexError or mysql.connector.errors.DatabaseErmysql.connector.errors.DatabaseError:
                    #print('Database not connected')
                    continue
            except UnicodeDecodeError or mysql.connector.errors.DatabaseErmysql.connector.errors.DatabaseError:
                #print('Database not connected')
                continue
except KeyboardInterrupt:
    ser.close()
    conn.commit()
    conn.close()


