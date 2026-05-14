# Development Log – The Torchbearer

**Student Name:** _____________Jeremiah Cho______________
**Student ID:** __________824840491_________________

---

## Entry 1 – [5-13-26]: Initial Plan

_my first priority is to implement dijkstras algorithm to precompute fuel costs betw/ the entrance, exit and relic chambers. i expect recursive search with pruning in explore() to be challenging and will test my logic with the concrete illustration to ensure to find minimum fuel cost of 4._

---

## Entry 2 – [5-13-26]: [resolving part 5b state discrepancy]

_Like a classmate, I also noticed an inconsistnecy in the assignment instructions where the README asks to document the data strucutre for visited relics but the explroe function in torchbearer asked for relics remaining. after seeing the clarification in the discord, I decided to design my state around relics remaining. I will use a python set for this bc/ removing an item and chechking if set is empty are both O(1) operations, which is ideal for knowing when to head to exit._

---

## Entry 3 – [5-13-26]: [git network timeout]

_while pushing my precomputation code for part 2, my terminal threw a fatal failed to connect to github.com port 443 error. At first, I thought I messed up my git branch strucutre and later realized my wifi  was givign off fake signal and had to reconfigure. Then i just git push and it synced wo/ force push command._

---

## Entry 4 – [5-14-26]: Post-Implementation Reflection

_torchbearer engine completed. with more time,I would upgrade the recursive serach to use memorization. right now the worst case search space is O(k!). By caching the min fuel costs of prev explored subsets of relics, the engine could look up those values instead of recalculating them. this would speed up search in dungeons w/ a high number of relics._
---

## Final Entry – [5-14-26]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.5 |
| Part 2: Precomputation Design | 2.5 |
| Part 3: Algorithm Correctness | 0.5 |
| Part 4: Search Design | 0.5 |
| Part 5: State and Search Space | 1 |
| Part 6: Pruning | 1|
| Part 7: Implementation | 2.5|
| README and DEVLOG writing | 1|
| **Total** | 9.5|
