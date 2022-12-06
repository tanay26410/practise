from collections import deque
class Graph:
    def __init__(self, Xdges, n):
        self.adjList = [[] for _ in range(n)]
        for (Source, destination) in Xdges:
            self.adjList[Source].append(destination) 
def isReachable(gr, Source, destination, dis, pa): 
    dis[Source] = True
    pa.append(Source)
    if Source == destination:
        return True
    for i in gr.adjList[Source]:
        if not dis[i]:
            if isReachable(gr, i, destination, dis, pa):
                return True
    pa.pop()
    return False
if __name__ == '__main__':
  A = int(input())
  Xdges = []
  for i in range(A):
    s = list(map(int,input().split(" ")))
    for j in s:
      Xdges.append((i,j-1))
  gr = Graph(Xdges, A)
  dis = [False] * A
  (Source, destination) = map(int,input().split(" "))
  Source = Source- 1
  destination = destination - 1
  pa = deque()
  if isReachable(gr, Source, destination, dis, pa):
      print(len(list(pa))-1,end="")
  else:
      print(-1,end="")
