import espnow
import time
import struct

e = espnow.ESPNow()
peer = espnow.Peer(mac=b'\x08:\x8d\x8e5\x90')
e.peers.append(peer)

temp = 25.46
humedad = 63

paquete = struct.pack("fi", temp, humedad)

while True:
    e.send(paquete)
    time.sleep(1.0)


