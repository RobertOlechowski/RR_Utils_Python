# RR Utils for Python

## What is, the purpose of this project?
It is a set of useful classes, That I often reuse in my projects

## How to install:
```bash
pip install rr-utils
```

## How to use it?
### How to use InlineClass
```python
from InlineClass.InlineClass import InlineClass
config_dic =  {"aa": 123, 
               "bb": "abc", 
               "cc": {"a1": 1}
               }
config_obj = InlineClass(config_dic, deep=True)
print(config_obj.cc.a1)
```

### How to use ConsoleLogger
```python
def consolelogger_use_case():
    import sys
    from ConsoleLogger import ConsoleLogger
    logger = ConsoleLogger()
    sys.stdout = logger
    print("This will go to console")

    logger.add_log_file_destination("log1.txt")
    print("This will go to console and file: log1.txt")
    logger.remove_last_destination()

    with logger.add_log_file_destination("log2.txt"):
        print("This will go to console and file: log2.txt")
```

### How to use Constraints
```python
from Constraints.Constraints import Constraints
from Constraints.VersionChecker import VersionChecker, VersionToCheck
from Version.Version import Version

obj = Constraints()
obj.add(VersionChecker(Version("3.8"), VersionToCheck.Python))
obj.add(VersionChecker(Version("4.2"), VersionToCheck.OpenCV))
obj.add(VersionChecker(Version("1.18"), VersionToCheck.NumPy))
obj.check(terminate_on_error=False)
```

### How to use Version
```python
from Version.Version import Version
ver = Version("1.2.3")
print(ver)
print("Major version {}".format(ver.get_version()[0]))
```

### How to use CallOnce
Look to dedicated [page](https://github.com/RobertOlechowski/RR_Utils_Python/blob/master/doc/callonce/README.md). 


### How to use StopWatch
```python
def stopwatch_use_case_1():
    from StopWatch.StopWatch import StopWatch
    obj = StopWatch(auto_start=False)
    with obj as timer:
        import time
        #some code
        time.sleep(0.2)
    print(obj.get_elapsed_time())
```

```python
def stopwatch_use_case_2():
    from StopWatch.StopWatch import StopWatch
    obj = StopWatch(auto_start=True)
    import time
    #some code
    time.sleep(0.2)
    print(obj.get_elapsed_time())
```

### How to use TimeLimitGenerator
```python
def timelimitgenerator_use_case():
    def func(counter, elapsed_total, elapsed_prev):
        import time
        print(f"Time elapsed: {elapsed_total}")
        time.sleep(0.2)
        return counter

    for item in TimeLimitGenerator(2, func): #will run for 2 secounds
        print(item)
```




