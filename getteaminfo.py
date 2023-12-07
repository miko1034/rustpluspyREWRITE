import asyncio
from rustplus import RustSocket

with open("./serverInfo.txt", "r") as f:
    info = list(f)

IP = info[0]
PLAYERTOKEN = int(info[1])
STEAMID = int(info[2])

f.close()

socket = RustSocket()