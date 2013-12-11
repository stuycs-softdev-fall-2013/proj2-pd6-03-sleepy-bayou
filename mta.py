def distance(a,b):
    print a
    #return int(((int(a[0])-int(b[0]))*(int(a[0])-int(b[0])) + (int(a[1])-int(b[1]))*(int(a[1])-int(b[1]))))
    return 1

def getTrips(stopid):
    ans = []
    f = open('google_transit/stop_times.txt')
    yolo = f.read()
    f.close()
    lines = yolo.split('\n')
    stops = []#[0][0]
    i = 0
    for l in lines:
        a = l.split(",")
        if len(a) > 1:
            stops.append(a)
    #    for l in lines:
        #        stops.append([])
        #        stop[i] = l.split(',')
        #        i+=1
    for li in stops:
        if li[3] == stopid:
            if not (li[0] in ans):
                ans.append(li[0])
    return ans

def getLan(stop):
    ans = []
    f = open('stops.txt')
    yolo = f.read()
    f.close()
    lines = yolo.split('\n')
    stops = [0][0]
    i = 0
    for l in lines:
        stops.append([])
        stop[i] = l.split(',')
        i+=1
    for i in stop:
        for l in i:
            if l[0] == stop:
                return l[4]

def getLon(stop):
    ans = []
    f = open('stops.txt')
    yolo = f.read()
    f.close()
    lines = yolo.split('\n')
    stops = [0][0]
    i = 0
    for l in lines:
        stops.append([])
        stop[i] = l.split(',')
        i += 1
    for i in stop:
        for l in i:
            if l[0] == stop:
                return l[5]

def getStops(tripid):
    ans = []
    f = open('google_transit/stop_times.txt')
    yolo = f.read()
    f.close()
    lines = yolo.split('\n')
    stops = []#[0][0]
    for l in lines:
        a = l.split(",")
        if len(a) > 0:
            stops.append(a)

    for li in stops:
        if li[0] == tripid:
            if not (li[3] in ans):
                ans.append(li[3])
    return ans

def getRoute(trip):
    ans = []
    f = open('google_transit/trips.txt')
    yolo = f.read()
    f.close()
    lines = yolo.split('\n')
    stops = []#[0][0]
    for l in lines:
        a = l.split(",")
        if len(a) > 1:
            stops.append(a)
    for li in stops:
        if li[2] == trip:
            return li[1]

def getRoutes(stop):
    tps = getTrips(stop)
    rs = getTrips(stop)
    for i in range(len(tps)):
        rs[i] = getRoute(tps[i])
    ans = []
    for i in rs:
        if not (i in ans):
            ans.append(i)
    return ans

def getTripsFromRoute(route):
    ans = []
    f = open('google_transit/trips.txt')
    yolo = f.read()
    f.close()
    lines = yolo.split('\n')
    stops = []#[0][0]
    for l in lines:
        a = l.split(",")
        if len(a) > 1:
            stops.append(a)

    for li in stops:
        if li[1] == route:
            if not (li[0] in ans):
                ans.append(li[0])
    return ans

def getStopsFromRoute(route):
    tps = getTripsFromRoute(route)
    ans = []#[0][0]
    for i in tps:
        ans.append(getStops(i))
    return ans

def getStopLocations(s,e):
    print("POOP")
    f = open('google_transit/stops.txt')
    yolo = f.read()
    f.close()
    lines = yolo.split('\n')
    stops = []
    for l in lines:
        if len(l) > 1:
            stops.append(l.split(','))

    distance1 = 10000
    stop1 = "0"
    stop1loc = [0,0]
    distance2 = 10000
    stop2 = "0"
    stop2loc = [0,0]
    aa = [0,0]
    for k in stops:
        aa[0] = k[4]
        aa[1] = k[5]
        if distance(s,aa) < distance1:
            distance1 = distance(s,aa)
            stop1 = k[0]
            stop1loc = [k[4],k[5]]
        if distance(s,aa) < distance2:
            distance2 = distance(s,aa)
            stop2 = k[0]
            stop2loc = [k[4],k[5]]

    locs = [stop1loc,stop2loc]

    route1 = []
    route1.append(getRoutes(stop1))
    route2 = []
    route2.append(getRoutes(stop2))
    crp = []
    
    while(True):
        for i in route2:
            for a in i:
                for op in route1:
                    if a in op:
                        crp.append(a)
                    break

    fty = []
    for iii in crp[0]:
        fty.append(iii.getStopsFromRoute(crp[0]))

    final = [0][0]

    for xiz in fty:
        final.append([getLan(xiz), getLon(xiz)])

    return final

   
        
        
    
    
