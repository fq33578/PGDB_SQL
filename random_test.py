import random,psycopg2,threading
from time import sleep,strftime
#######隨機0~3000的亂數#####
def n3000():
    # global count
    tmp=random.uniform(0, 3000)
    count=round(tmp,2)
    return count
#######n3000()亂數四捨五入#######
def out_3000():
    op_out=[]
    for _ in range(10):
        count = n3000()
        op_out.append(float(count))
    return op_out
#######隨機0~10的亂數#####
def n10():
    # global count
    count=random.uniform(0, 10)
    return count
#######n10()亂數四捨五入#######
def out_10():
    op_out=[]
    for _ in range(10):
        count = n10()
        op_out.append(int(count))
    return op_out
#######隨機20~23的亂數#####
def n_temp1():
    # global count
    tmp=random.uniform(20,23)
    count=round(tmp,2)
    return count
#######隨機20~40的亂數#####
def n_temp2():
    # global count
    count=random.uniform(20,40)
    return count
#######n_temp1()亂數四捨五入#######
def out_temp1():
    op_out=[]
    for _ in range(10):
        count = n_temp1()
        op_out.append(float(count))
    return op_out
#######n_temp2亂數四捨五入#######
def out_temp2():
    op_out=[]
    for _ in range(10):
        count = n_temp2()
        op_out.append(float(count))
    return op_out
############pgdb連線#############
def pgdb_connect():
    global conn,cur
    conn = psycopg2.connect(database="saa_graphic", user="postgres", password="70753397", host="localhost", port="5432")
    print ("Opened database successfully")
    conn.autocommit = True 
    cur = conn.cursor()
############變數上傳到PGDB#############
def upload_sensor():
    while 1:
        try:
            date_time=strftime("%Y-%m-%d %H:%M:%S")
            tmp=out_3000()
            cur.execute("INSERT INTO saa_machine VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (date_time,tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], tmp[8], tmp[9]))
            conn.commit()
            print ("[saa_machine] upload ok")
            sleep(3)
        except Exception as e:
            print(e)
            conn.close()
            pgdb_connect()
            sleep(3)
def upload_human():
    while 1:
        try:
            date_time=strftime("%Y-%m-%d %H:%M:%S")
            tmp=out_10()
            cur.execute("INSERT INTO saa_human VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (date_time,tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], tmp[8], tmp[9]))
            conn.commit()
            print ("[saa_human] upload ok")
            sleep(3)
        except Exception as e:
            print(e)
            conn.close()
            pgdb_connect()
            sleep(3)
def upload_temp():
    while 1:
        try:
            date_time=strftime("%Y-%m-%d %H:%M:%S")
            tmp=out_temp1()#20~23
            tmp2=out_temp2()#20~40
            cur.execute("INSERT INTO saa_temp VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (date_time,tmp[0], tmp2[1], tmp2[2], tmp2[3], tmp2[4], tmp2[5], tmp2[6], tmp2[7], tmp2[8], tmp2[9]))
            conn.commit()
            print ("[saa_temp] upload ok")
            sleep(3)
        except Exception as e:
            print(e)
            conn.close()
            pgdb_connect()
            sleep(3)
pgdb_connect()
t = threading.Thread(target =  upload_sensor)
t2=threading.Thread(target = upload_human)
t3=threading.Thread(target = upload_temp)
# 執行該子執行緒
t.start()
t2.start()
t3.start()

#_thread.start_new_thread(TS_LINE, ())
#_thread.start_new_thread(LCD_SCAN, ())
   
#     out_1000()
#     sleep(1) 

