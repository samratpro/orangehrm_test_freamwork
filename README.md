## how to use
### clone
```bash
git clone https://github.com/samratpro/orangehrm_test_freamwork.git
```
### install and activate virtual env
#### windows
```bash
python -m venv env
source env/scripts/activate
```
#### Mac/Linux
```bash
python3 -m venv env
source env/bin/activate
```
### Install library (pip3 for mac/linux)
```bash
pip install -r requirements.txt
pip3 install -r requirements.txt
```

### How to run Login Test
```bash
pytest tests/test_login.py
pytest -m login
```
