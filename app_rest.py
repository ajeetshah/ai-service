import torch
from transformers import pipeline
from fastapi import FastAPI

model = "meta-llama/Llama-3.2-1B-Instruct"
max_new_tokens=100

app = FastAPI()

def getGenerator():
  device = "cuda" if torch.cuda.is_available() else "cpu"
  return pipeline(model=model, device=device, torch_dtype=torch.bfloat16)

generator = getGenerator()

def formatPrompt(userContent, systemContent):
  prompt = [
    {"role": "user", "content": userContent}
  ]
  if systemContent != "" and systemContent is not None:
    prompt.append({"role": "system", "content": systemContent})
  return prompt

def getGeneratedText(prompt):
  generation = generator(prompt, do_sample=False, temperature=1.0, top_p=1, max_new_tokens=max_new_tokens)
  return generation[0]['generated_text']

def isAssistantRole(generatedTextItem):
  if generatedTextItem["role"] == "assistant":
    return True
  return False

def filterByAssistantRole(generatedText):
  return list(filter(isAssistantRole, generatedText))

@app.get("/generate")
async def generate(uc: str, sc: str | None = None):
  if uc == "" or uc is None:
    return {"response": "Please provide the user content of Prompt"}
  else:
    prompt = formatPrompt(uc, sc)
    generatedText = getGeneratedText(prompt)
    filtered = filterByAssistantRole(generatedText)
    assistantContent = filtered[0]["content"]
    return {"response": assistantContent}
  
@app.get("/hello")
def hello():
  return "Hello, World!"
