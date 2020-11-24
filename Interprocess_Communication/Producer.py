from multiprocessing.connection import Client
import random
import string 
import time
i = 0
random_string = ''
address = ('192.168.232.177', 5000)
conn = Client(address)
while i < 10 :
    num= random.randint(1,10)
    conn.send(num)
    time.sleep(1) 
    letters = string.ascii_lowercase
    random_string = ( ''.join(random.choice(letters) for i in range(10)) )
    conn.send(random_string)
conn.send('close')
    #if num == None :
        #conn.close()
conn.close()