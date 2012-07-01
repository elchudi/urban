from bottle import route, run, get, request, post
import zone
import os
import json
import video

zone.updateZone(video.videos)

@get('/video')
def videoGet():
    
    #x1 = int(request.params.get('x1'))
    #y1 = int(request.params.get('y1'))
    #x2 = int(request.params.get('x2'))
    #y2 = int(request.params.get('y2'))

    toRet = ""
    for z in video.videos:
        toRet += json.dumps(z.__dict__)
        toRet += ','
    toRet = toRet[:-1] 
    toRet = '{"video_array":['+ toRet  + ']}'
    print toRet
    return toRet

@get('/hello/:name')
def index(name='World'):
    print dir(request)
    return '<b>Hello %s!</b>' % name


@get('/map')
def map():
    
    #x1 = int(request.params.get('x1'))
    #y1 = int(request.params.get('y1'))
    #x2 = int(request.params.get('x2'))
    #y2 = int(request.params.get('y2'))

    toRet = ""
    for z in zone.zones:
        toRet += json.dumps(z.__dict__)
        toRet += ','
    toRet = toRet[:-1] 
    toRet = '{"zone_array":['+ toRet  + ']}'
    print toRet
    return toRet
    #return '%s' % json.dumps(zone.zones[0].__dict__)

@get('/json')
def jsonstruct():
    json = ['zone.json','video.json','user.json']
    toRet = ""
    savedPath = os.getcwd()
    os.chdir('/home/xa/Works/urban')
    print 'hola'
    for j in json:
        for l in open(j).readlines():
            toRet += l
    os.chdir( savedPath )
    return toRet

@get('/vote') # or @route('/login', method='POST')
def vote():
    idstr = request.params.get('id')
    id = int(idstr)
    video.videos[id-1].vote_up = video.videos[id-1].vote_up + 1 
    zone.updateZone(video.videos)
    return ""

    


run(host='192.168.1.168', port=8080)
