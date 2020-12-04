from ntptime import settime
import utime
import _thread

def atualizador():
# Metodo usado para ficar atualizando o relogio local da esp
  while(True):
    try:
      settime()
      i= 0
      # usado para ficar no sleep durante 24 horas, com 1 sleep ficava 8 minutos somente
      while(i< 180):
        utime.sleep(480)
        i = i+1
    except KeyboardInterrupt:
      raise Exception("desligar")
    except Exception as e:
      # Da erro quando nao tiver internet      
      utime.sleep(5)
    
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('#erro404#', 'NET10net@')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())    
    
