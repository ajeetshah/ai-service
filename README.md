# AI Service

# How to use app_cli?

```bash
$ source my-env/bin/activate # activate a virtual python env
$ pip install -r requirements.txt # install dependencies from requirements.txt
$ python app_cli.py -uc "Tell me a random but interesting fact" # feel free to change the prompt
```

# How to use app_rest?

```bash
$ source my-env/bin/activate # activate a virtual python env
$ pip install -r requirements.txt # install dependencies from requirements.txt
$ uvicorn app_rest:app --host 127.0.0.1 --port 8000 # feel free to change the host / port
```

and the api call:

```bash
GET http://127.0.0.1:8000/generate?userContent=Area of USA?

# or

curl http://127.0.0.1:8000/generate\?userContent=\"Hi there\?\"
```
