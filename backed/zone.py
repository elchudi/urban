import json
from itertools import izip, count


count = [0]
alpha = '#50'
#amarillo,azul,verde,red
col = ['808080','FFCB00', '2E16B1','00CC00','FF0000',]
img_url = ["","url","url","url","url"]
colors = []


cen =    ["41.393226","2.151604"]
pla =    ["41.382665","2.180443"]
mon =    ["41.408162","2.128944"]
cenizq = ["41.373391","2.128258"]
monizq = ["41.38962","2.110062"]
plaizq = ["41.355096","2.154694"]
monder = ["41.431848","2.161217"]
cender = ["41.427214","2.196579"]
plader = ["41.413312","2.221985"]

z1p = cen + mon + monizq + cenizq
z2p = cen + cender + monder + mon
z3p = cen + cenizq + plaizq + pla
z4p = cen + pla + plader + cender

for c in col:
    colors.append(alpha + c)


 

class Zone():

    def __init__(self, po, group_id=0):
        pairs = zip(po[::2], po[1::2])
        self.polyline = []
        for p in  pairs:
            self.polyline.append({"x":p[0],"y":p[1]})
        self.id = count[0]
        #self.group_id_rgb = colors[group_id]
        #self.group_img_url = img_url[group_id]
        self.group_id_rgb = ""
        self.group_img_url = ""
        self.group_votes = [0, 0, 0, 0]
        count[0] +=  1

#z1 = Zone([41.38962,2.110062,41.373391,2.128258,41.393226,2.151604,41.408162,2.128944])
z1 = Zone(z1p,1)
z2 = Zone(z2p,0)
z3 = Zone(z3p,0)
z4 = Zone(z4p,2)
zones = [z1, z2, z3, z4]

def updateZone(videos):
    for z in zones:
        for r in range(4):
            z.group_votes[r] = 0
        for v in videos:
            if v.zone_id == z.id:
                z.group_votes[v.group_id] = z.group_votes[v.group_id] + v.vote_up
        l = z.group_votes
        m = max(l)
        index = [ i for i,v in enumerate(l) if v==m ]
        print 'zone id:', z.id
        print 'index :', index
        print 'votes', l
        if len(index) > 1:
            z.group_id_rgb = colors[0]
            z.group_img_url = img_url[0]
        else:
            z.group_id_rgb = colors[index[0]]
            z.group_img_url = img_url[index[0]]
            
    return 

#print 'hola!'
#print z1.polyline
#print repr(z1)
#print json.dumps(z1.id)
#print json.dumps(z2.id)
#print json.dumps(z3.id)
#print json.dumps(z4.id)
#print json.dumps(z1.polyline)
#print json.dumps(z1.group_id_rgb)
#print json.dumps(z1.group_img_url)
for z in zones:
    print json.dumps(z.__dict__)





