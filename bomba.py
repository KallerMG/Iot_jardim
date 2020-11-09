from machine import Pin
import ujson
from time import sleep

def ligar_bomba():
    p0 = Pin(2, Pin.OUT)   
    with open('config.json', 'r') as config_file:
        dados = ujson.load(config_file)  
    tempo = dados['tempo_irri']
    p0.on()                 # ligar bomba
    sleep((int(tempo)*60))
    p0.off()