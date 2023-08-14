import requests
import json

#variaveis
Api_key_IP = "API_KEY"
ip = input("Informe o seu Ip: ")
url = f"http://api.ipstack.com/{ip}?access_key={Api_key_IP}"




response = requests.get(url)
data = json.loads(response.content)
zip = str(data["zip"])
url2 = f"http://viacep.com.br/ws/{zip}/json"


print("===========///:Resultado:///========")
print("Continente: ", data["continent_name"])
print("Pais: ", data["country_code"])
print("Capital: ", data["location"]["capital"])
print("Regiao: ", data["region_name"])
print("Cidade: ", data["city"])
print("CEP: ", data["zip"])
print("Latitude: ", data["latitude"])
print("longitude: ", data["longitude"])
print("Bandeira do pais:", data["location"]["country_flag_emoji"])
print("Ip: ", data["ip"])

response2 = requests.get(url2) 
data2 = json.loads(response2.content)


print("====================================")
print("============://Resultado://=========")
print("====================================")
print("UF: ", data2["uf"])
print("Localidade: ", data2["localidade"])
print("Bairro: ", data2["bairro"])
print("logradouro: ", data2["logradouro"])
print("CEP: ", data2["cep"])
print("DD: ", data2["ddd"])