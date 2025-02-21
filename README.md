# AI Service

# How to use app_cli?

```bash
$ source ai-env/bin/activate # activate a virtual python env
(ai-env) $ pip install -r requirements.txt # install dependencies from requirements.txt
(ai-env) $ python app_cli.py -uc "Who are you?" # feel free to change the prompt
(ai-env) $ python app_cli.py -uc "Tell me a random but interesting fact" # feel free to change the prompt
```

# How to use app_rest?

```bash
$ source ai-env/bin/activate # activate a virtual python env
(ai-env) $ pip install -r requirements.txt # install dependencies from requirements.txt
(ai-env) $ uvicorn app_rest:app --host 127.0.0.1 --port 8000 # feel free to change the host / port
```

and the api call:

- Enter something like this in the browser bar:
  - `http://127.0.0.1:8000/generate?userContent=Who are you?`
  - `http://127.0.0.1:8000/generate?userContent=Tell me a random but interesting fact`
- Or use the `curl`:

```bash
curl http://127.0.0.1:8000/generate\?userContent\=Who%20are%20you\?
curl http://127.0.0.1:8000/generate?userContent=Tell%20me%20a%20random%20but%20interesting%20fact
```
