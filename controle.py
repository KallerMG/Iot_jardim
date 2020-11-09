import sensores
import ujson

print(sensores.sensor_temp())


 
        
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
        
        if int(prev_chuva) >= 90:
            if sensores.sensor_temp() > 31
            print("bombear")
        else:
            print("Não bombear")
        
        