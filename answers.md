# CMPS 2200 Recitation 10## Answers

**Name:**_____Tony Shen____________________
**Name:**__Sean Hall_______________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** We are checking visited one time for every node in the graph, giving us a work complexity of O(n^2),but the optimal work complexity should be O(N+M). 

- **4)** The reachable function is only called once because the graph is undirected. If the graph is directed, it will most likely be called more than once. However, because it is undirected, any node can travel to any other node within the graph (assuming connected).

- **5)** Because connected calls reachable once, it will have work complexity of O(n^2). Checking the length of the two will be constant O(1). Thus the work is O(n^2 + 1) or simply O(n^2)

- **7)** If we switched the graph to an adjacency matrix, the work would still be O(n^2) and would not change the overall work. 
