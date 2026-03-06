(a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),
           (d,f,7),(d,e,3),(e,g,1),(e,f,5),(f,g,2),(b,f,1))
GP = {}


def make_link(gp, node1, node2, cost):
    if node1 not in gp:
        gp[node1] = {}
    (gp[node1])[node2] = cost
    if node2 not in gp:
        gp[node2] = {}
    (gp[node2])[node1] = cost

def dijkstra(gp, base):
    dis = {}
    visited = []
    current = base
    current_cost = 0
    for next_node in gp[current]:
        # TODO
        

for (i,j,k) in triples:
    make_link(GP, i, j, k)
    
dist = dijkstra(GP, a)

for node in sorted(GP):
    print(f'{node}: {GP[node]}')
