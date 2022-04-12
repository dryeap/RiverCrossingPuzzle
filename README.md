# RiverCrossingPuzzle (*DFS/BFS*) 🚣‍♀

## Puzzle description 🛶

There are 3 priests and 3 devils on a river shore, and they must all make it across the river using a boat. The boat
carries 2 people at most, and it can't cross the river on its own.

Here's the catch: if a priest is left outnumbered by devils (on shore), you lose.

## Compare solving this puzzle using DFS or BFS

Between Depth and Breadth-first search, which would you choose to solve this problem?

Check the implementation and how both methods fare against each other.

<details>
  <summary>Open for analysis</summary>

### DFS

Depth-first Search iterates the decision tree using a **Stack** - Last In First Out (LIFO)

Reaches the deeper elements in the decision tree faster. Since in this puzzle we have to get to an end state deep(ish)
in the decision tree, this method is preferred.

### BFS

Breadth-first Search iterates the decision tree using a **Queue** - First In First Out (FIFO)

Takes a long time reaching the deeper nodes in the decision tree because it searches all nodes in a given level before
moving on to the next one. The fastest solution to this puzzle isn't located in the first levels of the decision tree,
this method is worse.

<p align="center">
  <img src="/output/queue_size_over_time.png"  alt="Queue size over time graph"/>
</p>

</details>

## Attempt to solve it on your own 🤔

If you get stuck, try checking the [solution](solution) for hints or for the complete solve!

## Sample Execution

<p align="center">
  <img src="/output/sample_execution.mkv" alt="Sample execution video"/>
</p>

