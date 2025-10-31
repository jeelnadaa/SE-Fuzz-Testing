# SE-Fuzz-Testing
---
## Pre-Requisites:
- pytest
- hypothesis
```
pip install -r requirements.txt
```
---
## Methodology:
- First run the processor.py(This file is completely fine if you give correct input but it cannot handle wrong input which we have to fix).
```
python processor.py
```
- Now You have to complete the boilerplate code in test_processor.py which I already completed.
- Now then after completing run the test file.
```
pytest test_processor.py
```
- You can see that processor.py is failing the tests for buggy code.
- So guess what we will fix that. and again which I already gave you in fixed_processor.py(rename as processor.py or in test_processor.py change the import statement).
- now then you can run the test again and see what happens.
```
pytest test_processor.py
```
- Now no errors. Hurray we did it. Go now submit the assignment. Your welcome hehe.
---
## Collaborators:
- Jeel Nada - PES2UG23CS357