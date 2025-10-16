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

During the initialization phase of the algorithm it translates the input into a modified adjacency list, which houses both the vertex a vertex is connected to and the type of connection between them.
The data structure can be visualised as followed, with each row of the list being filled by $n$ times ``[adjacent_vertex, connection_type]``.

To create this adjacency list the usage of a for loop is employed, which loops through each line of the file to place an adjacency between the first number and the second, with the type of the third. 
During this the amount of generated connections is kept to be compared to the supposed number of connections that is provided on the file's first line. 
In the event that these don't match the input data is wrong, something that can be used later to check if the full algorithm did it's job correctly.


##### 1.2 Algorithm Logic
- Using the adjacency list we build an MST, where all stages are connected by at least one road
- MST creation can be configured for either bus or foot travel
- During MST creation we keep count of the amount of stages we've connected to the tree, comparing it to the total amount of stages in the end. In the case these numbers don't match we know not all stages were reached
- In the case this doesn't happen we return an adjacency list with all edges in the MST
- Mention that we keep count of the total amount of edges in the MST, this part seems to malfunction in the algorithm at the moment...
  - The error should be that we're counting the type 2 edges double... perhaps only count them during bus MST? Otherwise we might have to look into running just one MST...

##### 1.3 Returning the Answer
- Given the outcome of 1.2 we can either return a -1 if it failed or subtract the remaining edges from the former edges and give that as an answer

The formulation of the final answer is done by first checking if both MST's have a vertex count equal to that of the full adjacency list, to asure that no stages were somehow left unreachable due to there for example being two subgraphs provided for the input.
In the event that this count doesn't match the $-1$ is returned, signaling that not all vertices could be reached.
Seeing as the original graph was undirected, this also makes it so that choosing a different starting vertex wouldn't change the outcome.

Given that the check succeeds the actual answer can be formulated, where the amount of edges in both MSTs are subtracted from the total edges in the original graph.
Since both MSTs have each only removed type $0$ or $1$ edges and type $2$ edges were only counted once, it is guaranteed that none were counted double and that the two of them combined is thus the minimum number of edges required to connect everything.
Subtracting that number from the total number of edges thus leaves the amount of unnecessary edges, which is returned as answer. 

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