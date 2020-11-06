import urequests as requests
import ujson 
import network
import time

#função pegar prev do tempo
def prev_temp():
        while True: 
            with open('config.json', 'r') as config_file:
                dados = ujson.load(config_file)

            cidade = dados['cidade']
            api_key = dados['API_Key']
            print(cidade)
            print(api_key)
            res = requests.get(url= str("http://api.weatherapi.com/v1/forecast.json?key=" + api_key +"&q=" + cidade +"&days=1"))
            dados = res.json()
            with open('clima_t.json', 'w') as clima:
                json.dump(dados,clima)
            clima.close()
            print("clima atualizado")
            time.sleep(600)


