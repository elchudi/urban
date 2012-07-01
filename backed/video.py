import json

#amarillo,azul,verde,red

class Video():
    def __init__(self, id, x, y, group_id, url, zone, vote_up=0):
        self.x = x
        self.y = y
        self.id = id
        self.group_id = group_id
        self.url = url
        self.vote_up = vote_up
        self.vote_down = 0
        self.zone_id = zone

#z1 = Zone([41.38962,2.110062,41.373391,2.128258,41.393226,2.151604,41.408162,2.128944])
v1 = Video(1,"41.423001","2.169456",1,"http://commonsware.com/misc/test2.3gp",1)
v2 = Video(2,"41.410256","2.154522",2,"http://commonsware.com/misc/test2.3gp",1)
v3 = Video(3,"41.390556","2.131176",1,"http://commonsware.com/misc/test2.3gp",0,10)
v4 = Video(4,"41.411415","2.197437",2,"http://commonsware.com/misc/test2.3gp",3,10)

videos = [v1, v2, v3, v4]

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
for z in videos:
    print json.dumps(z.__dict__)





