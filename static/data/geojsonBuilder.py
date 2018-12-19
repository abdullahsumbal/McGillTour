from geojson import Point, Feature, FeatureCollection, dump, LineString
import json


features = []


with open('points_and_edges.json') as f:
    data = json.load(f)

for name, coordinates in data["Points"].items():
    point = Point(coordinates)
    features.append(Feature(geometry=point, properties={"name": name}))



# add more features...
# features.append(...)

feature_collection = FeatureCollection(features)

with open('points.geojson', 'w') as f:
   dump(feature_collection, f)


features = []
for name, adjList in data["Edges"].items():
    for adj in adjList:
        features.append(Feature(geometry=LineString(coordinates = [data["Points"][name], data["Points"][adj]])))

feature_collection = FeatureCollection(features)

with open('edges.geojson', 'w') as f:
   dump(feature_collection, f)
