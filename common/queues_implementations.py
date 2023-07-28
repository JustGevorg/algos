from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque()
search_queue += graph["you"]

while search_queue:
    person: str = search_queue.popleft()
    if person.endswith("m"):
        print(f"{person} is mango seller")
    else:
        search_queue.append(graph[person])
