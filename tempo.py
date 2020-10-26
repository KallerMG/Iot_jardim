import urequests as requests
import ujson as  json
import network

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('conectando')
        sta_if.active(True)
        sta_if.connect('#erro404#', 'NET10net@')
        while not sta_if.isconnected():
            pass
    print('Config da rede:', sta_if.ifconfig())

do_connect()

res = requests.get(url='http://api.weatherapi.com/v1/forecast.json?key=abeef68b3988478abca200752202010&q=Pelotas&days=1')
dados = res.json()

with open('clima_t.json', 'w') as clima:
    json.dump(dados,clima)
