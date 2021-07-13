# Part Ⅰ: Built-in Data Structures
So, data structures allow us to organize, store, and manage data for efficient access and modification.

Python include four types of built-in ds:
- list
- tuple
- set
- dictionary

### List
The list is mutable and ordered. It can contain a mix of differnt data types.

```python
nums = [1, 2, 3, 4, 5]
print(nums[0])   # 1
print(nums[1:4]) # 2, 3, 4
nums[0] = 6
print(nums[0])   # 6
```

### Tuple
It is a data type for immutable ordered sequences of items. Immutable means that u can't add and remove items from tuples.

```python
length, width, height = 7, 3, 1 # assign multiple varibles in one shot
print(length, width, height)    # 7, 3, 1
```

### Set
Set is a mutable and unordered collection of unique items.

```python
nums = [5, 1, 2, 3, 3, 4, 5]
u_nums = set(nums)
print(u_nums) # {1, 2, 3, 4, 5}

fruits = {'Apple', 'Orange', 'Cherry'}
print('Kiwi' in fruits) # False
fruits.add('Kiwi')
```

### Dictionary
Dictionary is a mutable and unordered data structure. It allow us to store pair of items (i.e. key - value).

```python
user = {
  'name': 'Nikita',
  'github': 'lusm554',
  'linkedin': 'lusm554',
  'inst': 'lusm554',
}
print(user['name']) # Nikita
```

# Part II: User-Defined Data Structures
Three user-defined data structures: queues, stack and tree.

#### Stack using arrays
The stack is a linear data structure where items are arranged sequentially. It follows the mechanism L.I.F.O which means last in firt out.
- Push - inserting item into stack
- Pop - deleting an item from stack

Conditions to check:
- overflow - occurs when we try to put one more item into stack that already having max items.
- underflow - occurs when we try to delete item from an empty stack.

Checkout `stack.py`.
