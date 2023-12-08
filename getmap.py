from rustplus import RustSocket
import asyncio

#reading info from server
with open("./serverInfo.txt", "r") as f:
    info = list(f)
IP = info[0]
PLAYERTOKEN = int(info[1])
STEAMID = int(info[2])
f.close()

async def getmap(ip,playertoken,steamid):
    socket = RustSocket(ip, "28082", playertoken, steamid)
    socket.connect()
    map = socket.get_map(True)
    #carry on here with saving the map if needed etc