### To run the app -

1. Create a virtual environment -
```
python -m venv venv
```

2. Activate the virtual environment - 
```
source venv/bin/activate
```

3. Install dependencies -
```
pip install -r requirements.txt
```

4. Run the flask application - 
```
flask --app app --debug run
```

5. Run tests -
```
pytest tests/address_validation.py
```