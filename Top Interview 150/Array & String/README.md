# Arrays & String

## 27 - Remove Element
### Description: 
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to val. The remaining elements of `nums` are not important as well as the size of `nums`.
Return `k`.

**Examples:**

- Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

- Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

### Aproach: 
After reading the problem many times, and sketching out possible solutions in my notebook I tried to approach the problem by using two pointers, where each pointer would compare the pointer value to the `val` value, and if it matched then something would occur. I noticed that the order of the `nums` array did not matter neither what is left beyond `k` elements, this was important in figuring out the solution. Finally I realized that I could initialize a `head` pointer and `tail` pointer, `tail` would move closer to `head` whenever it pointed to an element equal to `val` and `head` would move closer to `tail` if `nums[head]` was not equl to `val`, each iteration when it encounters an element equal to `val` it would swap it with `tail` and set it to Null.

For `k` I set it to `len(nums)` and whenever `head` or `tails` was equal to `val`, k would deacrement.

### What I Learned: 
When dealing with two pointer problems it is best to use a while loop instead of a for loop, and the use of a clean up function is important.

### Challenges: 
Some cases when there were too many of the same number in a row equal to `val`, the `head` value would skip over some of those elements. I overcame this by adding a check at the end of the function to make sure that the head element was checked in case it was missed by the loop.

### Complexity: 
The time complexity is O(n) where n is each element in the array, and the space complexity is O(1) as the given array is the only thing that is used, there was no need for extra space.