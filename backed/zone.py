import json

count = [0]
alpha = 'A0'
col = ['FF0000', 'FFCB00', '2E16B1', '00CC00']
img_url = ["url","url","url","url"]
colors = []


cen = [41.393226,2.151604]
pla = [41.382665,2.180443]
mon = [41.408162,2.128944]
cenizq = [41.373391,2.128258]
monizq = [41.38962,2.110062]
plaizq = [41.355096,2.154694]
monder = [41.431848,2.161217]
cender = [41.427214,2.196579]
plader = [41.413312,2.221985]

z1p = cen + mon + monizq + cenizq
z2p = cen + cender + monder + mon
z3p = cen + cenizq + plaizq + pla
z4p = cen + pla + plader + cender

for c in col:
    colors.append(alpha + c)

class Zone():
    
    def __init__(self, polyline):
        self.polyline = polyline
        self.id = count[0]
        self.group_id_rgb = colors[count[0]]
        self.group_img_url = img_url[count[0]]
        count[0] += 1


#z1 = Zone([41.38962,2.110062,41.373391,2.128258,41.393226,2.151604,41.408162,2.128944])
z1 = Zone(z1p)
z2 = Zone(z2p)
z3 = Zone(z3p)
z4 = Zone(z4p)

zones = [z1, z2, z3, z4]

print 'hola!'
#print z1.polyline
#print repr(z1)
#print json.dumps(z1.id)
#print json.dumps(z2.id)
#print json.dumps(z3.id)
#print json.dumps(z4.id)
#print json.dumps(z1.polyline)
#print json.dumps(z1.group_id_rgb)
#print json.dumps(z1.group_img_url)
#for z in zones:
#    print json.dumps(z.__dict__)





