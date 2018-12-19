from flask import Flask , redirect, render_template, url_for, request
from dijkistra import Graph
import json
from math import sin, cos, sqrt, atan2, radians
app = Flask(__name__)
graph = None
data = None

@app.route('/')
def index():
    return redirect(url_for('mcgilltour'))

@app.route('/mcgilltour', methods=['GET'])
def mcgilltour():

    # get all the point and coordinates
    with open('static/data/points_and_edges.json') as f:
        data = json.load(f)
    nodes = data["Points"]

    # calcualte the distance and put everything in following formate [("node1", "node2", distance)]
    graphList = []
    for name, adjNodes in data["Edges"].items():
        for adjNode in adjNodes:
            R = 6373.0
            lat1 = radians(nodes[name][1])
            lon1 = radians(nodes[name][0])
            lat2 = radians(nodes[adjNode][1])
            lon2 = radians(nodes[adjNode][0])

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c * 1000
            graphList.append((name, adjNode, distance))

    # put in local data structure to apply graph algo
    graph = Graph(graphList)

    # get start and end point defined by user
    start = request.args.get('start')
    end = request.args.get('end')
    #default case
    if(start == None and end == None):
        start = "Trottier"
        end = start

    # find shortest path
    pointNames, totalDistance = graph.dijkstra(start, end)
    startCoord = [data["Points"][start][1], data["Points"][start][0]]
    endCoord = [data["Points"][end][1], data["Points"][end][0]]

    # get all points in path
    connectingCoord = []
    for pointName in pointNames:
        coordinate = data["Points"][pointName]
        connectingCoord.append([coordinate[1],coordinate[0]])

    locations = ["Trottier", "McConnell", "Arts", "Mclennan_Library", "Bronfman", "SSMU"]
    return render_template('mcgilltour.html', coordinates=connectingCoord, distance=int(totalDistance), locations=locations, start=start, end=end,
    startCoord=startCoord, endCoord=endCoord)

if __name__ == '__main__':
   app.run(debug = True)
