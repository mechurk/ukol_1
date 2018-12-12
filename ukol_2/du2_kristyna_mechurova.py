import geojson

with open ("body_adresy.geojson",encoding='utf-8') as f:
    gj=geojson.load(f)

adresy=gj['features'][0]
print (adresy)

body=[]
for polozky in gj ['features']:
    ID= polozky['properties']['@id']
    souradnice=polozky ['geometry']['coordinates']
    body.append ([ID, souradnice[0], souradnice [1]])

print (body)


#def calc_bbox(body):
minx = float("inf")
miny = float("inf")
maxx = float("-inf")
maxy = float("-inf")
for bod in body:
    if bod [1] < minx:
        minx = bod [1]
    if bod [1]> maxx:
        maxx = bod [1]
    if bod [2]< miny:
        miny = bod [2]
    if bod [2] > maxy:
        maxy = bod [2]
bbox= [minx, miny,maxx, maxy]
print (minx,miny,maxx,maxy)
#return (bbox)



#bbox=calc_bbox(body)
print(bbox)

strx=((bbox[2]-bbox[0])/2)+bbox[0]
stry=((bbox[3]-bbox[1])/2)+bbox[1]
print (strx)
print (stry)
for bod in body:
    if bod [1] < strx and bod[2]> stry:
        ctvrtina =1
    elif bod [1] > strx and bod[2]> stry:
        ctvrtina =2
    elif bod [1] < strx and bod[2]< stry:
        ctvrtina =3
    elif bod[1] > strx and bod[2] < stry:
        ctvrtina = 4
    bod.append(ctvrtina)

print (body)