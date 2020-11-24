from multiprocessing.connection import Listener
import time
i = 0 
random_string = ''
address = ('192.168.232.177', 5000)     # family is deduced to be 'AF_INET'
listener = Listener(address)
conn = listener.accept()
#print ('connection accepted from', listener.last_accepted)
while i < 10:
   msg = conn.recv()
   num=int(msg)
   time.sleep(1)
   print(num)
   time.sleep(1)
   random_string = conn.recv()  
   random_string=str(random_string)
   time.sleep(1)
   print(random_string)
   #if num == None :
   #conn.close()
   #break
   listener.close()