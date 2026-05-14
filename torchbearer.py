"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: __________Jeremiah Cho_________________
Student ID:   ____________824840491_______________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns a string analysis of problem strucutre. 
    -------
    """

    return (
        "single dijkstra from S only finds distance to ind nodes and doesnt account for seq needed to visit all relics. after precomputing inter location costs, engine must determine optimal order of relic visits to minimize total cost. therefore, this probme requires a search over all possible orders to find minimum total fuel cost to visit all relicx and reach exit."
    )
    


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    returns list of nodes used as sources for dijkstra. no duplicates. order doesnt matter

    """
    #combine spawn point and relics into one set to remove any potential dupiicates then return as list and ensure map starting point for every leg of path
    sources = set([spawn] + relics) 
    return list(sources)


def run_dijkstra(graph, source):
    """
    returns minimum cost from srouce to every node in graph. unreachable nodes map to float
    """
    #initialize distances to infinity for all nodes in graph
    distances = {node: float('inf') for node in graph}
    distances[source]=0

    #init pq w/ starting node
    pq= [(0,source)]

    while pq:
        curr_cost, curr_node = heapq.heappop(pq)

        #if pull older expensive path off heap, skip it
        if curr_cost > distances[curr_node]:
            continue

        #explore neigbor
        for neighbor, weight in graph[curr_node]:
            new_cost = curr_cost + weight

            #if found cheaper path to neighbor, update and push to heap
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(pq, (new_cost,neighbor))
    return distances



def precompute_distances(graph, spawn, relics, exit_node):
    """
    returns nested strucutre supporting dist table[u][v] lookups
    """
    dist_table={}
    sources = select_sources(spawn, relics, exit_node)

    #run sdijkstra fgor every source and store resulting dictionary
    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    returns part 3 readme anssers as string
    """
    return (
        "3a: finalized nodes have their abs min fuel cost locked in. non-finalizzed nodes store cheapest path found so far using finalized nodes."
        "3b: at init, source is 0 and others are infinity. during mainteneacnce , finalizign the min dist node is correct bc/ nonnegative edge weights make surealt paths through unvisited nodes can only be more expensive.at termination, all reachable nodes have shortest paths determined."
        "3c: correct precomputed dists are important bc/ if wrong, the serach engine will eval permuations using false cost and select suboptimal route"
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    returns part 4 README answers as a string
    """
    return (
        "greedy fails bc/ choosing the immediate cheapest step can force the torchbearer into an expensive path later. for example, starting with a cost 1 step to r1 mgiht require a cost 100 step to reach r2, whereas starting w/ a cost 2 step to r2 might allow a cost 1 step to r1 saving 98 fuel. therefore, the algo must explore diff ways to  evaluate the total cost of every valid order of relic visits "
    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    sets up the init stage and triggers the recursive search
    """
    #best tracjks with lowest cost and optimal relic order
    best = [float('inf'), []]

    #set up init state based on readme design
    relics_remaining = set(relics)
    relics_visited_order =[]

    #start recursive search from spawn
    _explore(dist_table, spawn, relics_remaining, relics_visited_order, 0.0, exit_node, best)
    
    #after recursion, if best[0] is still inf then that means no path exists
    if best[0] == float('inf'):
        return float('inf'), []
    
    #retur min cost and ordered relic list
    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    recursive helper w/ backtracking and pruning
    """
    #prune if already spent more fuel than best known route
    if cost_so_far >= best[0]:
        return
    
    #lower bound estimation pruning
    if relics_remaining:
        min_relic_dist = min(dist_table[current_loc][relic] for relic in relics_remaining)

    #required comment answer
    #this pruning is safe bc/ dijkstra dist provide the abs true shortest paths. since mathematiccally impossible to reach next relic using less fuel than this min bound there is no way to accidentally miss the optimal solx
    if cost_so_far + min_relic_dist >= best[0]:
        return
    
    #base case: if no relics remain, head to exit
    if not relics_remaining:
        cost_to_exit = dist_table[current_loc][exit_node]
        total_cost = cost_so_far + cost_to_exit

        #if this route beats prev best then update tracker
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = list(relics_visited_order)
        return
    
    #recursive step: iterate list copy so no change to set while loop
    for next_relic in list(relics_remaining):
        step_cost = dist_table[current_loc][next_relic]

        #apply choice
        relics_remaining.remove(next_relic)
        relics_visited_order.append(next_relic)

        #go deepr into dungeon
        _explore(dist_table, next_relic, relics_remaining, relics_visited_order, cost_so_far+step_cost, exit_node, best)

        #bacltrack to try next change
        relics_remaining.add(next_relic)
        relics_visited_order.pop()

# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    master fucntion to precompute dists and run the search
    """
    # precompute all point to point cost
    dist_table = precompute_distances(graph, spawn, relics, exit_node)

    #run baktracking search
    best_cost, best_route = find_optimal_route(dist_table, spawn, relics, exit_node)

    return best_cost, best_route


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
