import heapq

routes = {
    "Hyd": [("chennai", 40), ("mumbai", 70)],
    "chennai": [("bengaluru", 20)],
    "mumbai": [("pune", 25)],
    "bengaluru": [("pune", 30)],
    "pune": []
}

pq = [(0, "Hyd", ["hyd"])]

while pq:
    cost, city, path = heapq.heappop(pq)

    if city == "pune":
        print("cheapest route:", "->".join(path))
        print("cost:", cost)
        break

    for nxt, w in routes[city]:
        heapq.heappush(pq, (cost + w, nxt, path + [nxt]))