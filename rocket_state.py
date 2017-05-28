import uostar
import json

import pprint
from datetime import datetime

def parse(accel, gps, baro):
    x = uostar.Coords(3,4)
    data = {
    "Acceleration":accel,
    "GPS":gps,
    "pressure":baro,
    "Time": str(datetime.now())
    }    
    output = json.dumps(data)
    return output
