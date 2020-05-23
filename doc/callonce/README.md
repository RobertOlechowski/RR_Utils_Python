# CallOnce

## What is, the purpose of this project?
Python decorator that gives ability to execute given function/method only once and cache results. The data can be stored not only in memory, but also on disk and remains persistent between application runs. 

## How to use:
Look to test directory to get idea.

### Simple example
```python
import CallOnce
from CallOnce.Enums import ArgumentsMode


@CallOnce.CallOnce(args_mode=ArgumentsMode.SERIALIZE_AND_HASH)
def plus_one(value):
    print ("Function invoked for {}".format(value))
    return value + 1
    
print(plus_one(5))
print(plus_one(5))
print(plus_one(10))

# Function invoked for 5
# 6
# 6
# Function invoked for 10
# 11
```

### Example with TTL
```python
from datetime import timedelta
import CallOnce

@CallOnce.CallOnce(ttl=timedelta(milliseconds=100))
def plus_one(value):
    print ("Function invoked for {}".format(value))
    return value + 1
    
print(plus_one(5))
print(plus_one(5))
from time import sleep
sleep(0.5)
print(plus_one(5))
print(plus_one(5))

# Function invoked for 5
# 6
# Function invoked for 5
# 6
```


## What are arguments of decorator?
##### args_mode
* ArgumentsMode.SERIALIZE_AND_HASH - Arguments of invocation are hashed 
* ArgumentsMode.IGNORE - Arguments are ignored and result of first invocation is cashed (Default)

##### hash_mode
* HashFunction.PYTHON - Standard Python Hash function is in use (Default)
* HashFunction.MD5 - MD5

##### ttl
Object of type datetime.timedelta that defines for how long given result should be cache. If None than we will remember it forever. 
Default is None


## ToDo:
* Improve tests for dictionary mode
* Add Serialisation and persistent storage on hard drive




