web: python swapi/main.py
release: python swapi/db.py
web: sh build.sh && uvicorn swapi.main:app --host 0.0.0.0 --port $PORT workers 1
