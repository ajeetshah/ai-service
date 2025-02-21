# AI Service

## Which LLM model does this project use?

Llama-3.2-1B-Instruct by Meta

## Do I need to download the LLM model first?

Check https://www.llama.com/docs/getting-the-models/hugging-face/.

You need to obtain the model by filling the form available at https://huggingface.co/meta-llama and requesting the authors for the model (https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) used in this project.

Once authors accept your request, you need to generate a HuggingFace token from your HF account and login from the terminal/CLI using command `huggingface-cli login`. This will enable downloading of the model automatically used in the project when the application runs.

## How to use app_cli?

```bash
$ python -m venv ai-env # Create a python virtual env if not done already
$ source ai-env/bin/activate # activate a virtual python env
(ai-env) $ pip install -r requirements.txt # install dependencies from requirements.txt
(ai-env) $ python app_cli.py -uc "Who are you?" # feel free to change the prompt
(ai-env) $ python app_cli.py -uc "Tell me a random but interesting fact" # feel free to change the prompt
```

## How to use app_rest?

```bash
$ python -m venv ai-env # Create a python virtual env if not done already
$ source ai-env/bin/activate # activate a virtual python env
(ai-env) $ pip install -r requirements.txt # install dependencies from requirements.txt
(ai-env) $ uvicorn app_rest:app --host 127.0.0.1 --port 8000 # feel free to change the host / port
```

and the api call:

- Enter something like this in the browser bar:
  - `http://127.0.0.1:8000/generate?uc=Who are you?`
  - `http://127.0.0.1:8000/generate?uc=Tell me a random but interesting fact`
- Or use the `curl`:

```bash
curl http://127.0.0.1:8000/generate\?uc\=Who%20are%20you\?
curl http://127.0.0.1:8000/generate?uc=Tell%20me%20a%20random%20but%20interesting%20fact
```

## Where are rest API docs?

After start the rest API server application. Visit http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc.

## How to increase the response length?

If you need larger response text and your machine can supprot it, change value of `max_new_tokens=100` in the python script. Check this - https://www.prompthub.us/models/llama-3-2-1b or other resources. Maximum possible value `2048` but keep it as low as possible.

## Todo

- Create a Dockerfile
- Try to use the model by downloading directly from meta site. So that one does not need HF account.
