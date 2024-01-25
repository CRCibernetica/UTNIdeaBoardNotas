import espnow
import struct

e = espnow.ESPNow()
packets = []

while True:
    if e:
        packet = e.read()
        temp, humedad = struct.unpack("fi", packet.msg)
        print(temp, humedad)