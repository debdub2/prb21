import math


divider = 60.0
lat1 = 60.051584
lon1 = 30.300509
r = 6371000
dist = 25.0
time_start = []
time_end = []


def _openfile():
    _data = open('nmea.log', 'rt')
    return _data


def checkstr(_str):
    def checkstr(_str):
    jj = True
    if (_str.find('$GPGGA') != -1) and (_str.find('M') != -1) and (_str.find('*') != -1) \
            and (_str.find('N') != -1 or _str.find('S') != -1) and (_str.find('E') != -1 or _str.find('W') != -1):
        ii = True
    else:
        ii = False
    try:
        float(line.split(',')[1])
        float(line.split(',')[2])
        float(line.split(',')[4])
    except:
        jj = False
    return(ii*jj)


def countlat(str):
    _line = str.split(',')
    latdegr = float(_line[2][:2])
    latmin = float(_line[2][2:])
    latminfl = latmin / divider
    if (_line[3] == 'N'):
        latitude = latdegr + latminfl
    else:
        latitude = -(latdegr + latminfl)
    return latitude


def countlon(str):
    _line = str.split(',')
    londegr = float(_line[4][:3])
    lonmin = float(_line[4][3:])
    lonminfl = lonmin / divider
    if (_line[5] == 'E'):
        longitude = londegr + lonminfl
    else:
        longitude = -(londegr + lonminfl)
    return longitude


def countdist(_lat, _lon):
    fi1 = math.radians(_lat)
    fi2 = math.radians(lat1)
    d_latitude = math.radians(lat1 - _lat)
    d_longitude = math.radians(lon1 - _lon)
    distance = 2*r*math.asin(math.sqrt(math.pow(math.sin(d_latitude/2), 2)+math.cos(fi1)*math.cos(fi2)*math.pow(math.sin(d_longitude/2), 2)))
    return distance


def time(_line, _dist, _i):
    if _dist < dist and _i == 0:
            _i = 1
            time_start.append(_line.split(',')[1])
    else:
        if _dist > dist and _i == 1:
            _i = 0
            time_end.append(_line.split(',')[1])
    return _i


def output(_ts, _te):
    print('Расстояние от положения катамарана до заданной точки было меньше 25 м в промежутках:')
    for i in range(len(_ts)):
        print(' {0}) с {1}:{2}:{3} до {4}:{5}:{6};'.format(i+1, _ts[i][:2], _ts[i][2:4], _ts[i][4:], _te[i][:2], _te[i][2:4], _te[i][4:]))


if __name__ == '__main__':
    i = 0
    input_data = _openfile()
    for line in input_data:
        if checkstr(line) == 1:
            i = time(line, countdist(countlat(line), countlon(line)), i)
    output(time_start, time_end)
