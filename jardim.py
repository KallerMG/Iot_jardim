import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open('config.json', 'w') as config_file:
    json.dump(data,config_file)

with open('config.json', 'r') as config_file:
    dados = json.load(config_file)  

presidente = dados['president']
print(presidente['name'])