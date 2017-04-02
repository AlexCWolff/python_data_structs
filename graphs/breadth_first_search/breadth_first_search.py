from .vertex import Vertex
from .graph import Graph
from .queue import Queue


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.start() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getconnections():
            if nbr.getcolor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


traverse(g.getVertex('sage'))
