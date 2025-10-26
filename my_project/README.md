# My Python Project

### project structure:
```markdown
my_project/
├── usecases/
│   ├── __init__.py
│   ├── main.py
├── tests/
│   └── test_main.py
├── setup.py
└── README.md
```
### Start executing this project

Option1:
```bash
cd ./my_project
pip3 install -e .
my_project
```

Option2:
```bash
cd ./my_project
python3 -m usecases.main
```


### To run a tests
```bash
cd ./python_example
pytest
```