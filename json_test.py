import ujson

    
with open('clima_t.json', 'r') as config_file:
    dados = ujson.load(config_file)  


prev = dados['forecast']
prev_d = prev['forecastday']
prev_dia = prev_d[0]
previ = prev_dia['day']
prev_temp = previ['avgtemp_c']
prev_umidade = previ['avghumidity']
prev_chuva = previ['daily_chance_of_rain']

print(prev_chuva)




