import requests 

token = 'da986fac164bfe37ceb5c6dc8334d78d'
url = 'https://api.pokemonbattle.me:9104'

"""response = requests.post (f'{url}/pokemons', json = {
    "name": "unterweg",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    }, headers = {'Content-Type': 'application/json',
                  'trainer_token': token})

print(response.text)"""

"""response = requests.put (f'{url}/pokemons', json = {
    "pokemon_id": "21446",
    "name": "unterweggg",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"}, 
    headers = {'Content-Type': 'application/json',
               'trainer_token': token})
print (response.text)"""

response = requests.post (f'{url}/trainers/add_pokeball', json = {"pokemon_id": "21446"}, 
    headers = {'Content-Type': 'application/json',
               'trainer_token': token})
print (response.text)

                                            
                                            


                          