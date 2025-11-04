[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fDpdMSPx)
# HW02 — Parking Spaces: Minimum Spots Needed

**Story intro (new theme):**  
A small **parking lot** has cars arriving and leaving at set times. You must find the **minimum number of parking spots** so no car waits.

**Technical description**  
- **Input:** a list of intervals `[(start, end), ...]` with `start < end`, integers.  
- **Output:** an integer: minimal number of spots required.  
- **Rule:** If a car leaves at time `t` and another arrives at time `t`, the same spot can be reused.  
- **Expected complexity:** **Time** `O(n log n)` with a **min-heap** of end-times; **Space** `O(n)`.

---

## 8 Steps scaffold
**Steps 1–5 (explicit)**
1. **Read & Understand:** We need the peak number of cars parked at once.  
2. **Re-phrase:** Track **earliest leaving** car. If the next car arrives **after or at** that time, reuse the spot.  
3. **Inputs/Outputs/Vars:** Input intervals, output spots, vars: `heap_of_end_times`, `rooms`.  
4. **Break down:** Sort by start. For each interval: pop ends ≤ start; push current end; update max size.  
5. **Pseudocode:**
```
sort intervals by start
heap = []
rooms = 0
for (s, e) in intervals:
while heap and heap[0] <= s:
heappop(heap)
heappush(heap, e)
rooms = max(rooms, len(heap))
return rooms
```

**Steps 6–8 (hints)**
- 6. **Code:** Use `heapq`.  
- 7. **Debug:** Print heap for small inputs.  
- 8. **Optimize:** Sorting once; each interval enters/leaves heap once.

---

## Hints
- Sort intervals by **start**.  
- Pop from heap while the **smallest end** ≤ current start.  
- Reuse a spot when times touch: `end <= start`.

---

## How to run tests
python -m pytest -q

markdown
Copy code

---

## FAQ
- **Q:** Closed or open intervals? **A:** Treat as `[start, end)`. End time frees the spot.  
- **Q:** Empty input? **A:** Return `0`.  
- **Q:** Can times repeat? **A:** Yes. Use the ≤ rule to reuse a spot.  
- **Q:** Complexity? **A:** `O(n log n)` time, `O(n)` space.  
- **Q:** stdin? **A:** No. Implement a function that tests import.  
- **Q:** Reading test failures? **A:** Check which case failed; compare expected vs actual.  
- **Q:** Grading? **A:** We run the tests. Passing earns full credit.
