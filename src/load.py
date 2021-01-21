import pygame, json, os

roomNameList = []
rooms = {}
playerStats = {}


with open("assets/player.json") as json_file:
    instanceData = json.load(json_file)
    for i in instanceData:
        playerStats[i] = instanceData[i]

for filename in os.listdir("assets/rooms"):
    if filename.endswith(".json"):
        roomNameList.append(filename)

for i in range(len(roomNameList)):
    with open("assets/rooms/" + roomNameList[i]) as json_file:
        instanceData = json.load(json_file)
        rooms[instanceData["name"]] = instanceData
