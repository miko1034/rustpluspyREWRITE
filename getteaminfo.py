from rustplus import RustSocket
import asyncio


with open("./serverInfo.txt", "r") as f:
    info = list(f)

IP = info[0]
PLAYERTOKEN = int(info[1])
STEAMID = int(info[2])

f.close()

async def getteaminfo(ip,playertoken, steamid):
    socket = RustSocket(ip, "28082", playertoken, steamid)
    socket.connect()
    info = await socket.get_team_info()
    teammembernames = []
    for i in range(len(info.members)):
        teammembernames.append(info.members[i].name)
    socket.disconnect()
    return teammembernames

names =  getteaminfo(IP, PLAYERTOKEN, STEAMID)

await print(names)