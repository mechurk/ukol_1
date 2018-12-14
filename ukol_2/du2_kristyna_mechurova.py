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


def calc_bbox(body):
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
    return (bbox)

#bbox=calc_bbox(body)




def processQuarter(body,box,cluster_id):
    pointsInThisBox = pointsInBox(body,box)
    print(pointsInThisBox)
    if (len(pointsInThisBox) < 50):
        for point in pointsInThisBox:
            point.append(int(cluster_id))
        return
    else :
        processQuarter(body,topLeft(box),cluster_id+"1")
        processQuarter(body,topRight(box),cluster_id+"2")
        processQuarter(body,bottomLeft(box),cluster_id+"3")
        processQuarter(body,bottomRight(box),cluster_id+"4")



def pointsInBox(body,bbox):
    return [point for point in body if bbox[0] <= point [1] < bbox[2] and bbox[1] <= point[2] < bbox[3] ]

def topLeft(box):
    stred = [(box[2] + box[0]) / 2, (box[3] + box[1]) / 2]
    qbox=[box[0], stred[1], stred[0], box[3]]
    return qbox
def topRight(box):
    stred = [(box[2] + box[0]) / 2, (box[3] + box[1]) / 2]
    qbox=[stred[0], stred[1], box[2], box[3]]
    return qbox
def bottomLeft(box):
    stred = [(box[2] + box[0]) / 2, (box[3] + box[1]) / 2]
    qbox=[box[0], box[1], stred[0], stred[1]]
    return qbox
def bottomRight(box):
    stred = [(box[2] + box[0]) / 2, (box[3] + box[1]) / 2]
    qbox=[stred[0], box[1],box[2], stred[1]]
    return qbox


box=calc_bbox(body)
processQuarter(body,box,"")
print (body)


