# Machine learning requirements

## Install python environment :
1. Create environment
``` bash
python3 -m venv .venv
```

2. Run environment 
```
source .venv/bin/activate
```

3. Run .py file 
```
python file_name.py
```
--- 

## Les listes 

- Declare a list 
```
list = [0, 1.5, 'abcd']
```

### 4 important methods 

#### range()
- The range() function returns a sequence of numbers, starting 
from 0 by default, and increments by 1 (by default), and stops before a specified number.
- The advantages is that don't create a list, just an iterator so very few memory is used by 
this method. 

- Syntax :
``` python
# Only the first arg is require
range(start, stop, step)
```

- Exemple :
```
range_ten = range(10)
for i in range_ten:
    print(i)
```
> output :
```
0
1
2
3
4
5
6
7
8
9
```
