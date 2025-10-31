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
- Looping through the file to build up a list of roads
- Road is {Starting point, End point, Type}

During the initialization fase the algorithm takes the given input file and loops through its lines, keeping the first line separate as it's a bit special.
The only thing of use that this line contains is the total amount of stages after all, while the total number of roads between them is instead retrieved in the next part.

In this section of the initialization the remaining lines of the file are counted and transformed into an array of integers, 
where entry 0 and 1 represent the origin and destination while entry 2 represents the type of road that it is, or the type thing that is able to use it more accurately.
During the remaining execution of the algorithm the acquired count of roads is used and preferred over the one given on the first line due to the fact that this number is certain to be accurate, 
while this can't always be said for the given number.

##### 1.2 Algorithm Logic

- Algorithm forms two disjoint sets, one for foot and one for bus, both containing all stages
- After this we loop through all roads depending on their type
  - For each iteration we add the road to the disjoint sets of those that can use it
  - In the set the total amount of 

During the execution state of the algorithm the usage of the disjoint set data structure is employed, where one is used for each user of the road network, leaving one for buses and one for pedestrians.
These sets each contain the total amount of stages present in the input file and are each used to figure out which stages weren't already reached if so to speak, where the lack of weight or a requirement for the shortest path ensures that once a path is found it is correct.

This finding or testing of paths is done in two loops, 
where one is used on all the roads that allow both modes of transportation and one on those that don't. 
In each loop it is checked if adding any of the roads looped through actually adds another previously unreachable stage to the network, 
which when it does means that the road will be used and the count of used roads is increased by one.
On the other hand, if a road doesn't benefit our network of stages, it means that no benefit is derived from it at all, meaning that we don't need it and thus don't need to count it.

Once both loops have finished a final check is done on the disjunction sets, 
to see if both of them still have the full number of stages reachable.


##### 1.3 Returning the Answer

For formulating the final answer the combination of the total amount of roads and the used amount of roads is used, 
where the latter is subtracted from the former to get the total amount of roads that could be removed from the road network.
This is based on the fact that the difference between the total roads and used roads must be the roads we didn't need to use, 
which thus could be removed.

One exception to the above explanation happens when the final check mentioned in chapter 1.2 fails,
as this signals that not all stages are reachable anymore. 
In the event that this happens the algorithm instead returns a minus one to signal this failure.

##### 1.4 Optimizations
- During initialization we keep 2 lists, one for each kind of loop
  - Ensures that type 2 loop doesn't touch type 0 or 1 and inverse
  - Reduces runtime from O(2*roads) to O(roads)
- Checking double roads first optimises efficiency but is needed anyway for correctness

While the cornerstone of this algorithm relies on keeping a number of disjoint sets equal to the types of road users,
a process that is by design already pretty optimized due to how relatively simple this data structure makes it to check if using a road has a benefit,
some optimizations were still made in an attempt to improve performance.

The first is the simplest, and also needed in part for always attaining correctness,
but by looking through the types of roads that allow multiple users first a larger number of stages is reached with lesser roads,
meaning that subsequent loops over the remaining roads don't need to find as many stages as they'd otherwise need to.
This is of course also needed for finding the optimal number of roads to remove, 
as otherwise a combination of a bus and pedestrian road might be used where one that allowed both would've sufficed as well,
but it is still a minor reduction to average runtime.

Second comes an optimization that is a bit more 'hacky' if so to speak, 
born from the realisation that all roads are looped through during initialization and that their types are already known here.
Combined with how the disjoint set loops each only care about the respective types of roads that they're using looking for,
so-called twin roads and single roads respectively, it is then possible to separate roads into different sets during initialization.
By doing this the algorithm then only has to loop through those subsets of roads once,
instead of going through the full set multiple times and only applying their logic to the roads that it applies to.

This second optimization has a much bigger impact, where it's effect can best be described as reducing that respective part's runtime from
$O(\text{Road Types}\cdot \text{Roads})$ down to just $O(\text{Roads}), which is very impactful when additional types of roads would be added or the number of roads increases.





---

### 2. Correctness Analysis
- Proof that comparing the roots of two nodes in disjoint set shows whether a new node is found
  - Since set can be seen as tree of sorts, both roots should eventually come down to the same node
  - This will only not happen if one of the two nodes isn't in the set already, in which case it'll be its own root
  - In that case the rootless node will get the rooted one as root, and the total number of nodes is decreased by one
- Proof that checking each road ensures maximum number is removed
  - Since the given way from node to node doesn't matter any route can be taken
  - Since no way is better than the other in terms of weight or length, the first one found is as good as all others
  - Once a route to a node is found, all other routes to that node are no longer needed and may thus be removed
  - By first checking what we can achieve with the roads that allow the most types of travelers we ensure that the minimal number of roads is used in the end
- Proof that subtracting the used roads from the total roads the remainder is the roads that were removed
  - If this doesn't hold we have a major problem


---

### 3. Complexity Analysis
- Complexity of disjoint list unknown
- Use 2 disjointsets total in a 2 loops that have a combined runtime of the number of edges
- Init is runtime of file length
- Total probably something like $O(roads+roads\cdot(disjointSet\cdot2))$


---

### 4. Reflection
- Disjoint set wasn't mentioned as much in lectures compared to other data structs, so it took a while to come up with this one and how it could be used here 
- The lack of weights made this practical easier although solving that could possibly be done by ordering the road lists in increasing order, 
which would've made it work pretty alright, although learning when the combined weight of typed roads is lesser than that of the generic one could've posed a challenge
- Submitting to DomJudge was pretty hard/irritating as no clear guide as to what or how it calls is easily found,
requiring multiple attempts at submitting just to figure out how it tests the code...


---