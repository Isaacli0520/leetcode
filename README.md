# leetcode

## Main
1. Linked List
    - [021. Merge Two Sorted Lists](code/0021_merge_two_sorted_lists.py)
    - [023. Merge k Sorted Lists](code/0023_merge_k_sorted_lists.py)
    - [019. Remove Nth Node From End of List](code/0019_remove_nth_node_from_end_of_list.py)
    - [876. Middle of the Linked List](code/0876_middle_of_the_linked_list.py)
2. Dynamic Programming
    - [053. Maximum Subarray](code/0053_maximum_subarray.py)
    - [509. Fibonacci Number](code/0509_fibonacci_number.py)
    - [322. Coin Change](code/0322_coin_change.py)
    - [300. Longest Increasing Subsequence](code/0300_longest_increasing_subsequence.py)
    - [354. Russian Doll Envelopes](code/0354_russian_doll_envelopes.py)
    - [055. Jump Game](code/0055_jump_game.py)
    - [931. Minimum Falling Path Sum](code/0931_minimum_falling_path_sum.py)
    - [064. Minimum Path Sum](code/0064_minimum_path_sum.py)
3. Greedy
    - [045. Jump Game II](code/0045_jump_game2.py)

## To-do
- 0010 regular expression matching

## Misc

### Python map() function
`map()` applies the function to all the items in the input iterable and returns an iterator
```python
>>> list(map(lambda x: x + 1, [1, 2, 3])) 
[2, 3, 4]

>>> list(map(lambda x, y: x + y, [1, 2, 3], [3, 4, 5])) 
[4, 6, 8]
```

### Python filter() function
`filter()` extracts elements fron an iterable for which a function returns `True`
```python
>>> list(filter(lambda x:x % 2 == 0, [1, 2, 3, 4]))
[2, 4]
```


