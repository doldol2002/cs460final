# Development Log – The Torchbearer

**Student Name:** _____________Jeremiah Cho______________
**Student ID:** __________824840491_________________

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

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

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
