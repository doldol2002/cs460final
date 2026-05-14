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

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
