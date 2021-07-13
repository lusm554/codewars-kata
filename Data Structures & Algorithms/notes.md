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

