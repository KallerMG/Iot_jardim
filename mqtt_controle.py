import ujson
import urequests as requests
import network
from umqtt.simple import MQTTClient
import machine 
import time
from time import sleep
import _thread


global led1 
global led2
def rotina_led(pino,valor):
   led = machinePin(pino,Pin.OUT)
   while True:
       led.value(not led.value())
       sleep(valor)

def mqtt_cidade(): #função para confirgutar o led 2 através dos dados obtidos via mqtt
    ledd = "led1"+".txt"
    while True:
        f = open(ledd)
        print("Led1: " +"Valor:" +f.read())
        f = open(ledd)
        oi =f.read()
        sleep(int(oi))
     
def led_on_2(): #função para confirgutar o led 2 através dos dados obtidos via mqtt
    ledd = "led2"+".txt"
    while True:
        f = open(ledd)
        print("Led2: " +"Valor:" +f.read())
        f = open(ledd)
        oi =f.read()
        sleep(int(oi))
     

def sub_cb(topic, msg):
    with open('config.json', 'r') as config_file:
        dados = ujson.load(config_file)
    mqtt = dados['MQTT']
    topico = mqtt['topico']
    id = dados['ID']
    top = str(topico + "/" + id)
    
    if(str(topic,'utf-8') == str(top + "/cidade")): #topico para o controle da cidade
        dados['cidade'] = str(msg,'utf-8')
        arquivo = open("config.json", "w")
        ujson.dump(dados, arquivo)
        arquivo.close()
        print("cidade chegou")
    elif(str(topic,'utf-8') == str(top + "/led2")): #topico para o controle do led 2
        f = open('led2.txt','w')
        f.write(str(msg,'utf-8'))
        f.close()
        print("leddd 2 chegou")
    else:
        print("invalido")
        

        
def inicializar():
    #leitura json
    with open('config.json', 'r') as config_file:
        dados = ujson.load(config_file)

    mqtt = dados['MQTT']
    usuario_mqtt = mqtt['usuario']
    senha_mqtt = mqtt['senha']
    topico = mqtt['topico']
    id = dados['ID']
    top = str(topico + "/" + id)
    
    #dados do broker mqtt (nome do dispositivo, broker, usuario, senha, e porta)
    client = MQTTClient("esp-kaller", "ioticos.org",user= usuario_mqtt, password=senha_mqtt, port=1883) 
    client.set_callback(sub_cb) 
    client.connect()
    client.subscribe(topic= str(top + "/cidade"))
    client2 = client
    client2.subscribe(topic= str(top + "/led2"))
    def estou_conectado():
        while True: 
            client.publish(topic=top + "/conectado", msg="conectado")
            time.sleep(15)
    #t =_thread.start_new_thread(mqtt_cidade,())
    #t2 =_thread.start_new_thread(led_on_2,())
    t =_thread.start_new_thread(estou_conectado,())

    while True: 
        client.wait_msg()
        time.sleep(1)
        client2.check_msg()
        time.sleep(1)






