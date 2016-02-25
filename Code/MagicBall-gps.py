import microstacknode.hardware.gps.l80gps as mst
from geopy.distance import vincenty
from time import sleep
gps = mst.L80GPS()
while True:
    sleep(10)
    
    coords = gps.get_gpgll()
    lat = coords ['latitude']
    lon = coords ['longitude']
    pos1 = (lat,lon)
    print(lat,lon)
    sleep(10)
    coords2 = gps.get_gpgll()
    lat2 = coords2 ['latitude']
    lon2 = coords2 ['longitude']
    pos2 = (lat2,lon2)
    print(lat,lon)
    print(vincenty(pos1,pos2).km)




