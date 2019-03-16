# comparative
Implement comparison magic methods in one line!


## Usage
```python
from comparative import compare_by

@compare_by("hour", "minute", "second")
class Clock:

    def __int__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = mintue
        self.second = second

    def __repr__(self):
        return ("Clock(h={0.hour:}, m={0.minute:02d}, "
                "s={0.second:02d})").format(self)

    def __str__(self):
        return "{0.hour:02d}:{0.minute:02d}:{0.second:02d}".format(self)
```


## Just Add Water
```python
>>> clock1 = Clock(8, 0, 0)
>>> clock2 = Clock(8, 0, 1)
>>> clock3 = Clock(8, 0, 0)
>>> clock1 < clock2
True
>>> clock1 == clock2
False
>>> clock1 == clock3
True
```
t@o55bhDr%