# Main
1. Linked List
    - [021. Merge Two Sorted Lists](code/0021_merge_two_sorted_lists.py)
    - [023. Merge k Sorted Lists](code/0023_merge_k_sorted_lists.py)
    - [083. Remove Duplicates from Sorted List](code/0083_remove_duplicates_from_sorted_list.py)
    - [019. Remove Nth Node From End of List](code/0019_remove_nth_node_from_end_of_list.py)
    - [876. Middle of the Linked List](code/0876_middle_of_the_linked_list.py)
    - [141. Linked List Cycle](code/0141_linked_list_cycle.py)
    - [142. Linked List Cycle II](code/0142_linked_list_cycle2.py)
    - [160. Intersection of Two Linked Lists](code/0160_intersection_of_two_linked_lists.py)
    - [206. Reverse Linked List](code/0206_reverse_linked_list.py)
    - [092. Reverse Linked List II](code/0092_reverse_linked_list2.py)
    - [234. Palindrome Linked List](code/0234_palindrome_linked_list.py)
2. Array
    - Double Pointers
        - [026. Remove Duplicates from Sorted Array](code/0026_remove_duplicates_from_sorted_array.py)
    - Prefix Sum Array
        - [303. Range Sum Query](code/0303_range_sum_query.py)
        - [304. Range Sum Query 2D](code/0304_range_sum_query_2d.py)
        - [560. Subarray Sum Equals K](code/0560_subarray_sum_equals_k.py)
    - Difference Array
        - [1094. Car Pooling](code/1094_car_pooling.py)
        - [1109. Corporate Flight Booking](code/1109_corporate_flight_bookings.py)
3. Dynamic Programming
    - [053. Maximum Subarray](code/0053_maximum_subarray.py)
    - [509. Fibonacci Number](code/0509_fibonacci_number.py)
    - [322. Coin Change](code/0322_coin_change.py)
    - [300. Longest Increasing Subsequence](code/0300_longest_increasing_subsequence.py)
    - [354. Russian Doll Envelopes](code/0354_russian_doll_envelopes.py)
    - [055. Jump Game](code/0055_jump_game.py)
    - [931. Minimum Falling Path Sum](code/0931_minimum_falling_path_sum.py)
    - [064. Minimum Path Sum](code/0064_minimum_path_sum.py)
4. Greedy
    - [045. Jump Game II](code/0045_jump_game2.py)
5. Misc
    - [Sliding Window](#sliding-window)
        - [076. Minimum Window Substring](code/0076_minimum_window_substring.py)
        - [567. Permutation in String](code/0567_permutaion_in_string.py)
        - [438. Find All Anagrams in a String](code/0438_find_all_anagrams_in_a_string.py)
        - [003. Longest Substring Without Repeating Characters](code/0003_longest_substring_without_repeating_characters.py)

# To-do
- 0010 regular expression matching

# Basic Code
## Sliding Window
```python
def sliding_window(s):
    # [left, right)
    left, right = 0, 0
    while right < len(s):
        # char added to the window
        c = s[right]
        right += 1

        # Update window and corresponding vars

        while window needs shrink:
            # If window meets requirement, save 
            # current best result

            # char removed from the window
            c = s[left]
            left += 1

            # Update window and corresponding vars


```

# Misc

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


