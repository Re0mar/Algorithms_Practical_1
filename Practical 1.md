## Seeing how many roads we can remove from Nijmegen without causing (to many) problems

---

Algorithms And Data Structures Practical One

Group: 
By:
- Daniël Groenendijk, **s1169129**
- Dirk

---

### Contents

1. Algorithm Explanation
2. Correctness Analysis
3. Complexity Analysis
4. Reflection

---

### 1. Algorithm Explanation

##### 1.1 Initialization
- Loop through all lines of the file, separating the first line as it contains total stage count
- All other lines get split up and added into an adjacency list

##### 1.2 Algorithm Logic
- Using the adjacency list we build an MST, where all stages are connected by at least one road
- MST creation can be configured for either bus or foot travel
- During MST creation we keep count of the amount of stages we've connected to the tree, comparing it to the total amount of stages in the end. In the case these numbers don't match we know not all stages were reached
- In the case this doesn't happen we return an adjacency list with all edges in the MST

##### 1.3 Returning the Answer
- Given the outcome of 1.2 we can either return a -1 if it failed or subtract the remaining edges from the former edges and give that as an answer

##### 1.4 Optimizations
- During initialization we count the total edges already, saving us from having to do it again
- During MST generation we already keep check of if we've reached all stages, saving us from having to do that again
	- Works because we don't care about going to particular places, only about going to **all** of them, which means we can just count

---

### 2. Correctness Analysis
- Proof that Initialization counts correctly should be easy
- Proof that an MST leaves only the minimum amount of edges necessary
- Proof that if all vertices are in the MST they can all be reached


---

### 3. Complexity Analysis
- Complexity of Initialization should just be $O(roads+1)$ due to file structure, little to be gained there
- Algorithm complexity is just that of making an MST, as we haven't done anything that increases that
- Total complexity would thus be those two combined


---

### 4. Reflection
- Finding MST solution was pretty easy as it's description is literally what we're searching for
- Further optimization could've been gained if we found a way to create the foot and bus MSTs as one
- Different way of solving could've been creating a list of all stages and which ones we've added to the network already, then looping through the file till we find a road that connects a new stage to the graph and repeat till all have been found, but this would be $O(stages\cdot roads)$, which would probably equal $O(n^2)$ or something
- The occasional wrong result from DOMjudge will probably be caused by errors in the input data, given that any and all sorts of validation for that were stripped in an effort to decrease runtime


---