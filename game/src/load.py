import pygame, json, os

roomNameList = []
rooms = {}

for filename in os.listdir("assets/rooms"):
    if filename.endswith(".json"):
        roomNameList.append(filename)

for i in range(len(roomNameList)):
    with open("assets/rooms/" + roomNameList[i]) as json_file:
        instanceData = json.load(json_file)
        rooms[instanceData["name"]] = instanceData