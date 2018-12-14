import geojson
import json

out_file = "body_adresy3.geojson"

with open("body_adresy.geojson", encoding='utf-8') as f:
    gj = geojson.load(f)

adress = gj['features'][0]
print(adress)

points = []
for issues in gj['features']:
    ID = issues['properties']['@id']
    coord = issues['geometry']['coordinates']
    points.append([ID, coord[0], coord[1]])

print(points)


def calc_bbox(points):
    minx = float("inf")
    miny = float("inf")
    maxx = float("-inf")
    maxy = float("-inf")
    for point in points:
        if point[1] < minx:
            minx = point[1] - 0.000000001
        if point[1] > maxx:
            maxx = point[1] + 0.000000001
        if point[2] < miny:
            miny = point[2] - 0.000000001
        if point[2] > maxy:
            maxy = point[2] + 0.000000001
    bbox = [minx, miny, maxx, maxy]
    print(minx, miny, maxx, maxy)
    return (bbox)


def processQuarter(points, box, cluster_id):
    pointsInThisBox = pointsInBox(points, box)
    if (len(pointsInThisBox) < 50):
        for point in pointsInThisBox:
            point.append(int(cluster_id))
        return
    else:
        processQuarter(points, topLeft(box), cluster_id + "1")
        processQuarter(points, topRight(box), cluster_id + "2")
        processQuarter(points, bottomLeft(box), cluster_id + "3")
        processQuarter(points, bottomRight(box), cluster_id + "4")


def pointsInBox(body, bbox):
    return [point for point in body if bbox[0] <= point[1] < bbox[2] and bbox[1] <= point[2] < bbox[3]]


def topLeft(box):
    middle = [(box[2] + box[0]) / 2, (box[3] + box[1]) / 2]
    qbox = [box[0], middle[1], middle[0], box[3]]
    return qbox


def topRight(box):
    middle = [(box[2] + box[0]) / 2, (box[3] + box[1]) / 2]
    qbox = [middle[0], middle[1], box[2], box[3]]
    return qbox


def bottomLeft(box):
    middle = [(box[2] + box[0]) / 2, (box[3] + box[1]) / 2]
    qbox = [box[0], box[1], middle[0], middle[1]]
    return qbox


def bottomRight(box):
    middle = [(box[2] + box[0]) / 2, (box[3] + box[1]) / 2]
    qbox = [middle[0], box[1], box[2], middle[1]]
    return qbox


box = calc_bbox(points)
processQuarter(points, box, "")
print(points)

for issue in gj['features']:
    for point in points:
        if issue['properties']['@id'] == point[0]:
            issue['properties']['cluster_id'] = point[3]
            # print(point)
            # print(point[3])

            break
with open(out_file, 'w') as out:
    json.dump(gj, out)
