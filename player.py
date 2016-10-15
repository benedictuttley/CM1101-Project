#This has the player information and stats
from map import rooms
current_room = rooms["Room 1"]
player_stats = {"strength": 5,"defence": 5, "health": 100, "alive": True, "weapon":None, "experience": 0, "level": 1}
weapons = {"stick": (10, 15), None:(1,10), "knife":(10,20), "gun":(30,40)}