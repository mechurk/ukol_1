import geojson

with open ("body_adresy.geojson",encoding='utf-8') as f:
    gj=geojson.load(f)

adresy=gj['features'][0]
print (adresy)


def calc_bbox(data):
    minx = float("inf")
    miny = float("inf")
    maxx = float("-inf")
    maxy = float("-inf")
    for p in data ['features']::
        if p['geometry']['coordinates'][0] < minx:
            minx = ['geometry']['coordinates'][0]
        if p['geometry']['coordinates'][0]> maxx:
            maxx = ['geometry']['coordinates'][0]
        if p['geometry']['coordinates'][0] < miny:
            miny = ['geometry']['coordinates'][1]
        if p['geometry']['coordinates'][0] > maxy:
            maxy = ['geometry']['coordinates'][1]
    bbox= [minx, miny,maxx, maxy]
    print (minx,miny,maxx,maxy)
    return (minx,miny,maxx,maxy)



