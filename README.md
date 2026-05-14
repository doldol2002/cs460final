# The Torchbearer

**Student Name:** ______________JEremiah Cho_____________
**Student ID:** __________824840491_________________
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  _a single dijkstra run from entrnace provides only shortest distance to each relicc but cannot determine most efficient sequence to visit multiple required locations in one trip._

- **What decision remains after all inter-location costs are known:**
  _once point to point costs are precomputed, engine must decide optimal order to visit all relic chambers (M) before heading to exit (T)._

- **Why this requires a search over orders (one sentence):**
  _because the total fuel cost depends on sequence of stops, the problem needs to explore different ways of relic visits to find global minimum._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| _spawn_ | _to find shortest path from starting point to first relic in any possible seq_ |
| _relics_ | _to find shortest paths betw all relic pairs and from each relic to final exit_ |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | nested dictionary |
| What the keys represent | outer keys are source nodes; inner keys are detination nodes|
| What the values represent | minimum fuel cost to travel from source to destnation|
| Lookup time complexity | O(1)|
| Why O(1) lookup is possible | python dictionaires use hash tables to provide fast key retrieval|

### Part 2c: Precomputation Complexity

computation cost based on n nodes, m edges, and k relics
- **Number of Dijkstra runs:** _k+1 one for entrance, one for each k relic chamber_
- **Cost per run:** _O(mlogn) using binary heap_
- **Total complexity:** _O((k+1) x mlogn)_
- **Justification (one line):** _one standard dijkstra run for every node identified in source selction table_

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  _the engine has found the abosllue lowest possible fuel cost from srouce and no cheaper path will be discovered_

- **For nodes not yet finalized (not in S):**
  _currently stored cost represents the cheapest route found so far that only uses already finalized nodes as intermediate steps_

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  _before first iteration, only source node is known, which is 0, and all others are infiniity which satisfies starting conditions_

- **Maintenance : why finalizing the min-dist node is always correct:**
  _when minimum cost unvisited node is finalized, distance is guaranteed to be optimal bc/ nonnegative edge weights ensure that any alt path routing through univisited nodes only add more fuel cost, never reduce_

- **Termination : what the invariant guarantees when the algorithm ends:**
  _when algo ends. all reachable nodes have been finalized and makes sure that recorded distances represent tru shorterst paths across entire graph_

### Part 3c: Why This Matters for the Route Planner

_this matters bc/ if precomputed point to point distances are inc, subsequent search algo will evaluate route permutations using false fuel costs causing the torchbearer to choose a suboptimal path_

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** _greedy algo only looks at cheapest immediate next step and ignores how that choice can force the torchbearer into a dead end_
- **Counter-example setup:** _entrance s, relics r1 r2, exit T. costs S to R1 is 1, S to R23 is 2. r1 to r2 is 100 but r2 to r1 is 1. both relics connect to T for 1._
- **What greedy picks:** _greedy starts at s and picks r1 bc/ its the cheapest first step bc/ its cost is 1. then forced to go to r2 which is cost 100 and finally to T which is cost 1. total cost is 102._
- **What optimal picks:** _the optimal route starts at s, goes to r2 which is cost 2 and then r1 which is cost 1 then to T which is cost 1 for total cost 4. _
- **Why greedy loses:** _by saving a single uniit of fuel on the first step, the greedy aapproach trapped itself into a path that requried a 100 more units of fuel to finish_

### What the Algorithm Must Explore

- _to make sure of the minimum total fuel cost, the algo must explroe diff combination to find optimal order of relic visits before heading to exit_

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc|string | room is torchbearer is currently standing in |
| Relics already collected | relics_remaining | set| the unvisited relics that still need to be colelcted |
| Fuel cost so far |cost_so_far |float |total accumulated fuel cost of path taken up to this point |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | python set (for relics_remaining)|
| Operation: check if relic already collected | Time complexity: O(1)|
| Operation: mark a relic as collected | Time complexity: O(1)|
| Operation: unmark a relic (backtrack) | Time complexity: O(1)|
| Why this structure fits | sets use hashtables for instant membership testing which make sit efficient to check what relics are left to visit or remove them from remaining  pool wo/ iterating over a list|

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** _O(k!)_
- **Why:** _if every relic is conncted to every relic, the engine must evaluate every possible way of the k relic chamber_

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** _lowest total fuel cost across completed valid routes to exit_
- **When it is used:** _it is checked every recursive step before exploring deeper into dungeon_
- **What it allows the algorithm to skip:** _immediately leaves partial routes that have already built up more  fuel cost than best known successful route_

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** _the cost so far and precomputer short dditances to remaining relics_
- **What the lower bound accounts for:** _it calculates cost so far plus the abs minimum cost to reach nearest unvisited relic_
- **Why it never overestimates:** _bc/ it uses short path dijkstra distances, it is impossible for torchbearer to reach next required stop using less fuel than this estimate_

### Part 6c: Pruning Correctness

- _pruning is safe bc/ if the minimum possible lwoer boundof partial route is already greater or equal than to best found solution, no future choices_

---

## References

- _lecture notes + youtube_
