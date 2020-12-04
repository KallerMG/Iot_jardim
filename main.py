import wifimgr
from time import sleep
import machine
import _thread
import mqtt_controle
import tempo
import data
import controle
try:
  import usocket as socket
except:
  import socket

led = machine.Pin(2, machine.Pin.OUT)

wlan = wifimgr.get_connection() # criar o wifi-manager 
if wlan is None:
    print("Não foi possível inicializar a conexão.")
    while True:
        pass  

# codigo do do controle  apartir daqui.


t1 =_thread.start_new_thread(mqtt_controle.inicializar,())
t2 =_thread.start_new_thread(tempo.prev_temp,())

sleep(2)

t3 =_thread.start_new_thread(data.atualizador,())

sleep(5)
import utime
date = utime.localtime()
print(date)

t4 =_thread.start_new_thread(controle.inicializar,())



