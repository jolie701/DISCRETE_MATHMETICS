# Discrete Mathematics and Graph Theory Assignments

This repository contains Python implementations of course assignments exploring core concepts in Discrete Mathematics and Computational Graph Theory. The projects focus on algebraic polynomial evaluation, graph representation data structures, and network optimization algorithms.

---

## Assignment Directory

| Assignment | Topic | Description | Core Concepts |
| :--- | :--- | :--- | :--- |
| **HW1** | Polynomial Evaluator | Reads polynomial coefficients from a file, formats and prints the mathematical expression dynamically, and evaluates $f(x)$ for user-inputted values until terminated. | Algebraic Expressions, Functional Evaluation |
| **HW2** | Graph Representations | Parses network configuration files and stores directed graphs using both Adjacency Matrices and Adjacency Lists. Outputs incident edges for requested source vertices. | Graph Theory, Adjacency Matrix, Adjacency List |
| **HW3** | Dijkstra's Shortest Path | Implements a point-to-point (1-1) Dijkstra's algorithm optimized with a Binary Min-Heap to find the shortest path and distance between an origin and destination. | Network Optimization, Min-Heap, Greedy Algorithms |

---

## Technical Specifications

### HW1: Polynomial Evaluation Formatting
* **Parsing:** Dynamically drops zero-coefficient terms.
* **Formatting:** Standardized spacing around operators (`+` and `-`) and terms (e.g., `x^2`, `x^3`).
* **Execution:** Continuous evaluation loop until the input value of $x$ equals `0`.

### HW2: Network Storage & Queries
* **File Format Supported:** DIMACS-like network formats parsing `p` (program), `n` (nodes), `a` (arcs), `t` (title), and `c` (comments).
* **Matrix Storage:** Generates an $n \times n$ connectivity matrix $A$ and an arc-length cost matrix $C$.
* **List Storage:** Implements an array of lists tracking forward and backward incident arcs to handle large, sparse networks efficiently.

### HW3: Shortest Path Optimization
* **Data Structure Requirement:** Strictly utilizes Adjacency Lists to accommodate multi-graphs and parallel edges.
* **Priority Queue:** Built using a Binary Min-Heap to optimize the Vertex Selection (VS) and Distance Update (DU) phases.
* **Early Termination:** Stopping criteria is met immediately once the target destination node is scanned.

---

## Environment & Requirements

* **Language:** Python 3.x
* **External Libraries:** Built entirely using Python standard libraries to demonstrate low-level algorithmic mastery.
* **Input File Restrictions:** Input text files must strictly adhere to the designated syntax constraints outlined in the respective homework descriptions.
