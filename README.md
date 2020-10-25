# DSA
This repo consists of all codes related to DSA --guide to DSA interview prep
- https://blog.pramp.com/how-to-succeed-in-data-structures-and-algorithms-interview-2ad1a28041b6
- https://www.educative.io/blog/coding-interivew-preparation-bootcamp

### Important Algorithms
- https://www.youtube.com/watch?v=r1MXwyiGi_U
- https://www.youtube.com/watch?v=zHczhZn-z30
#### Depth First Search 
   - Stack
   - Go completely to the root and come back
### Breadth First Search - Queue
   - Queue
   - Go level by level
### Matching Paranthesis
  - Stack - simple solution
  - IF stack not empty then false in the end
### Use of hash tables
  - Visit a 2D array
  - Cache a number/Keep track here
  - DP
### Use multiple pointers and manipulate them
   - Longest palindromic substring : Traverse string and use 2 pointers 
### Reverse a linked list
   - Use previous, current, next 
   - Cycle in a linked list
   - Remove duplicates in a linked list (for sorted direct, for unsorted use hash table)

### Sorting Algorithms
   - Selection
   - Insert
   - Bubble
   - Heap
   O(NLOGN)
   - Merge
   - Quick
Dont really have to implement, runtimes are important

### Recursion
- hates or loves :(
- Rarely used, but tested a lot - TREES
- Not very practical
- stack calls that is how u implemented it

### Constuct a Data Structure/choosing the correct one

### U might need OOPs

### Binary SEARCH :)
 - logn complexity - Keeps reducing to 1/2 every time - So log base 2, that's the logic
 - quicksort implemented on similar lines

----------------------------------------------------------------------------------------------------------
## Complexity and Big O, Big Theta and Big Omega

https://www.youtube.com/watch?v=0oDAlMwTrLo
- Basically Big O notation is an upper bound that limits or always is greater than the function taken into consideration 
#### Big O is FOR WORST TIME
- Big Omega is the best time complexity, that is the least time the algorithm would take to execute
#### Big Omega is FOR BEST TIME
- Big Omega is for AVERAGE time complexity, that is the (least time + worst time) / 2 , the algorithm would take to execute
#### Big Theta is FOR AVERAGE TIME

We talk about Big O most commonly which is used as we are mostly interested in the performance of the algorithm given the worst circumstances

- Big O, small o what and why
https://cathyatseneca.gitbooks.io/data-structures-and-algorithms/content/analysis/notations.html

DP in python
- http://justinbois.github.io/bootcamp/2020/lessons/l33_algorithmic_complexity.html

Complexity of itertools.permutation in O(n!)
### Kadanes algorithm ###

- Used for max subarray
- Complexity is O(n)
- https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
- Link to understand better
- https://www.youtube.com/watch?v=2MmGzdiKR9Y Back to SWE - From CUBIC to QUADRATIC to LINEAR 


TOWER OF HANOI

https://www.youtube.com/watch?v=0u7g9C0wSIA
Very easy recursion question................................

## Consecutive letters ##
All can be done in O(n) complexity but the brute force approach will be O(n**3)

https://medium.com/@poitevinpm/leetcode-1446-consecutive-characters-bbba426cf2cc

Most of the questions that need you to find the miniumum or maximum subseq or strings in an array can be done in time O(n) rather than O(n**3)


Binary search, recursive algo and iterative, both have time complexity of the order O(log(n)) but for recursive the space is o(logn) but iterative is o(1)
https://iq.opengenus.org/binary-search-iterative-recursive/#:~:text=The%20major%20difference%20between%20the,the%20iterative%20version%20is%20efficient.

### bisect in python for binary search,  in_sort to insert an element to the correct position in a sorted array ###
bisect_right will get the position of insertion of an element into a sorted array from the right
bisect_left will get the position of insertion of an element into a sorted array from the left
https://www.youtube.com/watch?v=mqaf7vj1AdA

### Longest I subsequence ###
https://cp-algorithms.com/sequences/longest_increasing_subsequence.html 

### Catalan numbers ###

These numbers can be used to represent the seq 1,1,2,5,42.......

given as (2n)!/(n+1)!n! where n is the nth term

### Sieve of eratosthenes ###
Primes between a range in O(sqrt(n)*log(log(n)) and space is O(n)


##Use the remove function to remove elements from a list in python ##
### Max product subsequence ##
https://www.youtube.com/watch?v=vtJvbRlHqTA
On the lines of Kadane, keep track of the maximum and minimum product


### This can be used to do the longest increasing subsequence using bisect in python ##

https://leetcode.com/problems/longest-increasing-subsequence/

### GEEKS for GEEKS
about DP
https://www.geeksforgeeks.org/dynamic-programming/

### Manacher's algorithm
Find the longest palindromic substring in linear time

### Dynamic sliding window
- https://www.youtube.com/watch?v=fYgU6Bi2fRg
- The time complexity is O(size of alphabet * length of string
- this is O(n) as opposed to a brute force solution in O(nm)
- Maximum value of subarrays 
   - https://www.youtube.com/watch?v=BVWxlcxW9Ww
### Trees Traversal and height 
- https://www.youtube.com/watch?v=AWIJwNf0ZQE
