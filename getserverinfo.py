from rustplus import RustSocket
import asyncio

#reading info from server
with open("./serverInfo.txt", "r") as f:
    info = list(f)
IP = info[0]
PLAYERTOKEN = int(info[1])
STEAMID = int(info[2])
f.close()

#getting all the info from the server
async def getserverinfo(ip,playertoken,steamid):
    socket = RustSocket(ip, "28082", playertoken, steamid)
    socket.connect()
    serverinfo = socket.get_info()
    socket.disconnect()
    return serverinfo

#additional information in the form of other functions that may be useful
def getplayercount(serverinfo):
    return serverinfo.players, serverinfo.max_players

def getmapsize(serverinfo):
    return serverinfo.size

asyncio.run(getserverinfo(IP,PLAYERTOKEN,STEAMID)) #ERROR HERE HELPPPP