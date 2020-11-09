from machine import Pin, ADC
import ujson

def sensor_temp():
    with open('config.json', 'r') as config_file:
        dados = ujson.load(config_file)  
    pino_temp_sensor = dados['temp_sensor']
    sensor = ADC(Pin(int(pino_temp_sensor)))
    sensor.atten(ADC.ATTN_11DB)  #3.3v maximo
    valor_sensor = sensor.read()
    return (((valor_sensor *3.3 / 4095) *200))


def sensor_umi():
    with open('config.json', 'r') as config_file:
        dados = ujson.load(config_file)  
    pino_temp_sensor = dados['umi_sensor']
    sensor = ADC(Pin(int(pino_temp_sensor)))
    sensor.atten(ADC.ATTN_11DB)  #3.3v maximo
    valor_sensor = sensor.read()
    return (valor_sensor)


def sensor_ldr():
    with open('config.json', 'r') as config_file:
        dados = ujson.load(config_file)  
    pino_temp_sensor = dados['ldr_sensor']
    sensor = ADC(Pin(int(pino_temp_sensor)))
    sensor.atten(ADC.ATTN_11DB)  #3.3v maximo
    valor_sensor = sensor.read()
    return (valor_sensor)
