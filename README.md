# algorithm-vault: Algorithms and Data Structures

This repository provides Python implementations of fundamental algorithms and data structures as studied in university-level courses. It is organized into various categories, each focusing on specific types of algorithms and data structures.

## Repository Structure

### Static Data Structures
- **Queue**: Implements a FIFO (First In, First Out) data structure.
- **Stack**: Implements a LIFO (Last In, First Out) data structure.

### Lists
- **Linked List**: A linear data structure where each element points to the next node in the sequence.
- **Doubly Linked List**: An extension of the linked list with nodes that point to both the next and previous nodes.
- **Circular Linked List**: A linked list where the last node points back to the first node.
- **Circular Doubly Linked List**: A combination of doubly linked list and circular linked list, where the last node points to the first node and each node points to both the next and previous nodes.

### Priority Queue
- **Heap**: A binary tree-based data structure that maintains the heap property, either max-heap or min-heap.
- **D-ary Heap**: A generalization of a binary heap where each node has `d` children.

### String Algorithms
- **Searching**
  - **Naive**: A straightforward substring search algorithm.
  - **Boyer-Moore-Horspool (BMH)**: An efficient string search algorithm that skips unnecessary comparisons using heuristics.
  - **Knut-Morris-Pratt (KMP)**: An efficient search algorithm utilizing a partial match table to avoid redundant comparisons.

- **Similarity**
  - **Hamming Distance**: Measures the number of positions at which two strings of equal length differ.
  - **Levenshtein Distance**
    - **Using Bottom Up**: Computes the minimum number of edit operations required to transform one string into another using dynamic programming.
    - **Using Top Down**: An alternative approach to compute the Levenshtein distance using memoization.

- **Compression**
  - **Huffman Compression**: A lossless compression algorithm that assigns variable-length codes to characters based on their frequencies.

### Trees
- **Binary Tree**: A hierarchical data structure in which each node has at most two children.
- **Restore Trees**: Algorithm to reconstruct binary trees from given preorder and inorder traversals.
- **Binary Search Tree**: A binary tree where each node’s left child contains a value less than the node, and the right child contains a value greater.
- **Segment Tree**: A data structure that allows efficient querying and updating of intervals or segments.
- **Trie**: A tree-like data structure used for efficient retrieval of keys in a set of strings.

### Graphs
- **Graph Representation**: Includes implementations for adjacency matrix and adjacency list representations.
- **DFS (Depth-First Search)**: A traversal algorithm that explores as far down a branch as possible before backtracking.
- **BFS (Breadth-First Search)**: A traversal algorithm that explores all nodes at the present depth level before moving on to nodes at the next depth level.
- **Best-First Search**: A search algorithm that uses heuristics to prioritize nodes towards the goal.
- **A-Star Search (A\*)**: An informed search algorithm that finds the shortest path from a start node to a goal node using a heuristic function.
- **Knights Tour Problem**: A problem where the objective is to move a knight on a chessboard to visit each square exactly once.
- **N Queens Problem**: A problem where the objective is to place `n` queens on a chessboard such that no two queens can attack each other.
- **Union Find**: A data structure for tracking and merging disjoint sets.
- **Minimum Spanning Trees**
  - **Kruskal's Algorithm**: Finds the minimum spanning tree of a graph by sorting and adding edges based on their weights.
  - **Prim's Algorithm**: Constructs a minimum spanning tree by expanding the tree from an initial vertex.

## Getting Started

To use any of the algorithms or data structures provided in this repository, navigate to the corresponding folder and refer to the Python files for the specific implementations.

Contributions are welcome. Feel free to submit pull requests or open issues if you have questions or suggestions.
