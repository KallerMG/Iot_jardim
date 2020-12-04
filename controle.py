import sensores
import ujson
import utime
from time import sleep



 
        
def inicializar():
    while True:
        with open('clima_t.json', 'r') as config_file:
            dados = ujson.load(config_file)  


        prev = dados['forecast']
        prev_d = prev['forecastday']
        prev_dia = prev_d[0]
        previ = prev_dia['day']
        prev_temp = previ['avgtemp_c']
        prev_umidade = previ['avghumidity']
        prev_chuva = previ['daily_chance_of_rain']
        ano, mes, dia, hora, minuto, segundos, ms, x  = utime.localtime()
        if int(prev_chuva) >= 90:
            temp = sensores.sensor_temp()
            if temp > 31:
                if (hora - 3) >= 18 :
                    print("bombear")
                else:
                    print("Não bombear")
            
            else:
                print("Não bombear")
        
        else:
            print("Não bombear")
        sleep(5)
        
        