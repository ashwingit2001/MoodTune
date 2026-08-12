## Goal

Prepare specifically for the **45-minute Google coding screen** using **C++**.

Given the limited time available on workdays:

* **Weekdays:** 2–3 serious problems
* **Weekends:** 5–7 problems + mock
* **~70–75% Medium**
* **~15% Easy**
* **~10–15% Hard**
* Hards are primarily **stretch/reasoning exercises**
* Prioritize solving, explaining, and coding cleanly over accumulating problem counts

---

# Day 1 — Arrays + Hashing

### Warm-up

* [x] Two Sum — Easy

### Core Mediums

* [x] Group Anagrams — Medium
* [ ] Product of Array Except Self — Medium
* [ ] Longest Consecutive Sequence — Medium

### Stretch

* [ ] First Missing Positive — Hard

Do the Hard only if the Mediums go reasonably well.

### C++ refresh

```cpp
vector<int>
unordered_map<int, int>
unordered_set<int>
sort(...)
```

### Patterns to understand

* Lookup tables
* Frequency maps
* Using sets to avoid repeated work
* Prefix/suffix computation
* Trading additional memory for better time complexity

---

# Day 2 — Two Pointers

### Warm-up

* [ ] Valid Palindrome — Easy

### Core Mediums

* [ ] Two Sum II — Medium
* [ ] 3Sum — Medium
* [ ] Container With Most Water — Medium

### Stretch Hard

* [ ] Trapping Rain Water — Hard

This is a very useful Hard because it teaches deeper two-pointer reasoning.

### Make sure you understand

Why can moving one pointer be proven safe?

Don't memorize:

```text
if left < right:
    move left
```

Understand **why the opposite pointer cannot improve the answer**.

---

# Day 3 — Sliding Window

### Core Mediums

* [ ] Longest Substring Without Repeating Characters — Medium
* [ ] Longest Repeating Character Replacement — Medium
* [ ] Permutation in String — Medium

### Stretch Hard

* [ ] Minimum Window Substring — Hard

This is one of the highest-value sliding-window Hards.

### Pattern

```cpp
int left = 0;

for (int right = 0; right < n; right++) {

    // incorporate right

    while (windowIsInvalid()) {
        // remove left
        left++;
    }

    // update result
}
```

But understand that some problems instead require:

> shrink while the window **remains valid**

Minimum Window Substring is particularly useful for learning that distinction.

---

# Day 4 — Stack + Monotonic Stack

### Warm-up

* [ ] Valid Parentheses — Easy

### Core Mediums

* [ ] Min Stack — Medium
* [ ] Daily Temperatures — Medium
* [ ] Car Fleet — Medium

### Stretch Hard

* [ ] Largest Rectangle in Histogram — Hard

Don't worry if Largest Rectangle is difficult.

The important learning objective is understanding **monotonic stacks**.

Ask:

> What information remains useful as I scan left → right?

> Why can I permanently discard an element when I pop it?

---

# Day 5 — Binary Search

### Warm-up

* [ ] Binary Search — Easy

Do this quickly from memory.

### Core Mediums

* [ ] Search in Rotated Sorted Array — Medium
* [ ] Find Minimum in Rotated Sorted Array — Medium
* [ ] Koko Eating Bananas — Medium

### Extra Medium

* [ ] Search a 2D Matrix — Medium

### Stretch Hard

* [ ] Median of Two Sorted Arrays — Hard

Median of Two Sorted Arrays is **optional**.

Don't sacrifice your entire evening to it.

The most important problem here is actually **Koko Eating Bananas**, because it teaches:

# Binary search on the answer

Learn to recognize:

```text
Can X work?

If X works, will every larger X also work?
```

If yes, there's often a binary search hiding there.

---

# Day 6 — Saturday

# Linked Lists + Trees

Heavy day.

---

## Linked Lists

### Warm-up

* [ ] Reverse Linked List — Easy

### Core Mediums

* [ ] Remove Nth Node From End of List — Medium
* [ ] Reorder List — Medium
* [ ] Add Two Numbers — Medium

### Stretch

* [ ] Merge K Sorted Lists — Hard

Merge K Lists also introduces heaps/divide-and-conquer, so it's especially useful.

---

# Trees — Part I

### Warm-up

* [ ] Maximum Depth of Binary Tree — Easy

### Core Mediums

* [ ] Binary Tree Level Order Traversal — Medium
* [ ] Validate Binary Search Tree — Medium
* [ ] Kth Smallest Element in a BST — Medium

### Extra

* [ ] Lowest Common Ancestor of a Binary Tree — Medium

Notice that I prefer the **general binary-tree LCA** problem rather than only the easier BST version.

---

# Day 7 — Sunday

# Trees Deep Dive + Mock Interview

### Core Mediums

* [ ] Binary Tree Right Side View — Medium
* [ ] Construct Binary Tree from Preorder and Inorder Traversal — Medium
* [ ] Count Good Nodes in Binary Tree — Medium
* [ ] Path Sum II — Medium

### Stretch Hard

* [ ] Binary Tree Maximum Path Sum — Hard

This is an excellent recursion/tree-DP problem.

You should understand the distinction between:

> What value does my recursive function return to its parent?

and

> What globally valid answer can be calculated at this node?

That distinction appears constantly in tree problems.

---

# Mock #1

After the tree session:

* [ ] Pick one **unseen Medium**
* [ ] Set timer to **45 minutes**
* [ ] No hints
* [ ] Speak everything aloud

Follow:

1. Clarify
2. Examples
3. Brute force
4. Optimization
5. Complexity
6. Code
7. Test
8. Edge cases

Don't choose a problem you've previously seen.

---

# Day 8 — Graphs

This is one of the highest-priority days.

### Core Mediums

* [ ] Number of Islands — Medium
* [ ] Clone Graph — Medium
* [ ] Rotting Oranges — Medium
* [ ] Pacific Atlantic Water Flow — Medium

### Extra Medium

* [ ] Max Area of Island — Medium

### Stretch Hard

* [ ] Word Ladder — Hard

Focus on recognizing:

```text
Grid → graph

Objects connected to other objects → graph

Minimum number of transitions → potentially BFS
```

You should be able to write BFS and DFS without looking anything up.

---

# Day 9 — Graphs + Heaps

## Graphs

### Core Mediums

* [ ] Course Schedule — Medium
* [ ] Course Schedule II — Medium
* [ ] Graph Valid Tree — Medium

Understand:

* adjacency lists
* directed vs undirected graphs
* cycle detection
* DFS state
* indegree
* Kahn's algorithm
* topological sorting

---

## Heaps

### Core Mediums

* [ ] Kth Largest Element in an Array — Medium
* [ ] Top K Frequent Elements — Medium
* [ ] K Closest Points to Origin — Medium

### Stretch Hard

* [ ] Find Median from Data Stream — Hard

This Hard is particularly useful because it tests whether you can combine:

```text
max heap + min heap
```

into a larger invariant.

---

# Day 10 — Backtracking + DP

## Backtracking

### Core Mediums

* [ ] Subsets — Medium
* [ ] Permutations — Medium
* [ ] Combination Sum — Medium
* [ ] Word Search — Medium

### Stretch Hard

* [ ] N-Queens — Hard

N-Queens is optional.

It's mostly there to test whether you truly understand backtracking rather than memorizing templates.

---

# Basic Dynamic Programming

If time remains:

### Core

* [ ] House Robber — Medium
* [ ] Coin Change — Medium

### Optional

* [ ] Longest Increasing Subsequence — Medium

I would **not prioritize advanced DP before the coding screen** unless everything else feels comfortable.

---

# Day 11+ — If You Have More Time Before the Interview

Now stop progressing topic-by-topic.

Start mixing problems.

## Session A

* [ ] Unseen Medium
* [ ] Unseen Medium
* [ ] Redo previously failed problem

## Session B

* [ ] Unseen Medium
* [ ] One Tree/Graph Medium
* [ ] One Hard stretch

## Session C

* [ ] Full 45-minute mock
* [ ] Review mistakes
* [ ] Reimplement solution cleanly

Repeat.

---

# Additional Mediums Worth Doing

If you finish the main list earlier than expected, choose from here.

## Arrays / Hashing

* [ ] Encode and Decode Strings — Medium
* [ ] Sort Colors — Medium
* [ ] Subarray Sum Equals K — Medium

## Two Pointers

* [ ] 4Sum — Medium
* [ ] Boats to Save People — Medium

## Sliding Window

* [ ] Minimum Size Subarray Sum — Medium
* [ ] Find All Anagrams in a String — Medium
* [ ] Max Consecutive Ones III — Medium

## Stack

* [ ] Decode String — Medium
* [ ] Asteroid Collision — Medium
* [ ] Remove K Digits — Medium

## Binary Search

* [ ] Find Peak Element — Medium
* [ ] Capacity To Ship Packages Within D Days — Medium
* [ ] Time Based Key-Value Store — Medium

## Linked Lists

* [ ] Copy List with Random Pointer — Medium
* [ ] LRU Cache — Medium
* [ ] Swap Nodes in Pairs — Medium

## Trees

* [ ] Zigzag Level Order Traversal — Medium
* [ ] Path Sum III — Medium
* [ ] House Robber III — Medium
* [ ] Delete Node in a BST — Medium

## Graphs

* [ ] Accounts Merge — Medium
* [ ] Evaluate Division — Medium
* [ ] Network Delay Time — Medium
* [ ] Minimum Height Trees — Medium

## Heaps

* [ ] Task Scheduler — Medium
* [ ] Reorganize String — Medium

## Backtracking

* [ ] Palindrome Partitioning — Medium
* [ ] Letter Combinations of a Phone Number — Medium

## Intervals

* [ ] Merge Intervals — Medium
* [ ] Insert Interval — Medium
* [ ] Non-overlapping Intervals — Medium
* [ ] Meeting Rooms II — Medium

## Greedy

* [ ] Jump Game — Medium
* [ ] Jump Game II — Medium
* [ ] Gas Station — Medium

## DP

* [ ] Decode Ways — Medium
* [ ] Partition Equal Subset Sum — Medium
* [ ] Longest Common Subsequence — Medium
* [ ] Unique Paths — Medium

---

# Hard Problems I Actually Want You to Attempt

Don't randomly pick LeetCode Hards.

These are useful because each reinforces an important interview pattern:

* [ ] **First Missing Positive** — arrays/index manipulation
* [ ] **Trapping Rain Water** — two pointers
* [ ] **Minimum Window Substring** — sliding window
* [ ] **Largest Rectangle in Histogram** — monotonic stack
* [ ] **Median of Two Sorted Arrays** — binary search
* [ ] **Merge K Sorted Lists** — heap/divide and conquer
* [ ] **Binary Tree Maximum Path Sum** — recursive tree reasoning
* [ ] **Word Ladder** — BFS
* [ ] **Find Median from Data Stream** — two heaps
* [ ] **N-Queens** — backtracking

You do **not** need to finish all ten before the interview.

I'd aim for **4–6 of them**.

---

# How Long to Spend on Each Difficulty

## Easy

Maximum:

**10–15 minutes**

These should mostly be syntax/pattern refreshers.

---

## Medium

Target:

**25–35 minutes**

If you haven't solved it by ~30 minutes but are making progress, continue a little longer.

If you're completely stuck, study the solution.

Then:

**close the solution and code it yourself.**

---

## Hard

Give yourself:

**30–40 minutes maximum**

The objective is not necessarily:

> I solved the Hard independently.

The objective is:

> I pushed my reasoning until I found the missing insight.

If stuck after that:

1. Read only the core insight.
2. Close the explanation.
3. Try again.
4. Implement it yourself.
5. Revisit it 2–3 days later.

---

# Difficulty Distribution

Across this plan, aim approximately for:

```text
Easy       10–15%
Medium     70–75%
Hard       10–15%
```

That's much better for your situation than grinding dozens of Easies.

---

# Priority Ranking If the Interview Suddenly Gets Scheduled Earlier

If you only have **5–6 days**, prioritize in this order:

### Priority 1

* [ ] Two Sum
* [ ] Group Anagrams
* [ ] Product of Array Except Self
* [ ] 3Sum
* [ ] Container With Most Water
* [ ] Longest Substring Without Repeating Characters
* [ ] Longest Repeating Character Replacement

### Priority 2

* [ ] Daily Temperatures
* [ ] Search in Rotated Sorted Array
* [ ] Koko Eating Bananas
* [ ] Reverse Linked List
* [ ] Reorder List

### Priority 3

* [ ] Binary Tree Level Order Traversal
* [ ] Validate BST
* [ ] Lowest Common Ancestor
* [ ] Kth Smallest in BST
* [ ] Binary Tree Maximum Path Sum

### Priority 4

* [ ] Number of Islands
* [ ] Rotting Oranges
* [ ] Clone Graph
* [ ] Course Schedule
* [ ] Course Schedule II

### Priority 5

* [ ] Kth Largest Element
* [ ] Top K Frequent Elements
* [ ] Subsets
* [ ] Combination Sum
* [ ] House Robber
* [ ] Coin Change

---

# Most Important Rule

Don't measure preparation using:

> "I solved 45 questions."

Measure it using:

> "If you give me a new Medium, can I figure out the underlying structure within 10–15 minutes?"

For every problem you finish, record only:

```text
Problem:
Pattern:
Key insight:
What I initially missed:
Time complexity:
Would I solve it again unaided? Yes / No
```

Any problem marked **No** gets repeated 2–3 days later.

By the final few days, the majority of your time should shift from **learning new problems** to **solving unseen Mediums under a 45-minute interview constraint**.
