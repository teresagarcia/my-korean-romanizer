# My Korean Romanizer
Korean romanizer based on the Revised Romanization of Korean.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install My Korean Romanizer.

```bash
pip install mykoreanromanizer
```

## Usage
```python
from mykoreanromanizer import Romanizer

r = Romanizer()

r.romanize("안녕하세요")  # returns  "annyeonghaseyo"
r.romanize("안녕이란 말 hello hello") # returns  "annyeongiran mal hello hello"
```
