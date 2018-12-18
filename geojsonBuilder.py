from geojson import Point, Feature, FeatureCollection, dump
import json


features = []


with open('edges.json') as f:
    data = json.load(f)

for name, coordinates in data["Points"].items():
    point = Point(coordinates)
    features.append(Feature(geometry=point, properties={"name": name}))



# add more features...
# features.append(...)

feature_collection = FeatureCollection(features)

with open('myfile.geojson', 'w') as f:
   dump(feature_collection, f)
