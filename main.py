import json
#json filemizi load edirik
def getDataFromDb(_fileName):
    with open(_fileName, "r") as f:
        return json.load(f)

cup = getDataFromDb("playersinformation.json")

#simple funksiya ile json filellarda emeliyyatlar apaririq
def playersStats(year):
  for stat in cup['fifacup']:
    if stat['year'] < year:
        print(f"{stat['player']} | {stat['country']}")


you = int(input("Please write your footballer year: "))
playersStats(you)
