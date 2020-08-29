import json
#imple crud system yaradiriq

def getDataFromDb(_fileName):
    with open(_fileName, "r") as f:
        return json.load(f)

cup = getDataFromDb("db.json")

def getDataFromUser():
    name = input("Player: ")
    year = int(input("Year: "))
    country = input("Country: ")
    player_status = int(input("Player status: "))
    players = {
        "player": name,
        "year": year,
        "country":country,
        "active_player_status": player_status
     }
    cup['fifacup'].append(players)  #yeni oyuncunu json file a elave edirik
    with open("db.json", "w") as f:
        json.dump(cup, f)


user = getDataFromUser()