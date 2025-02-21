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

def formatPrompt(userContent):
  prompt = [
    {"role": "user", "content": userContent}
  ]
  return prompt

def getGeneratedText(prompt):
  generation = generator(prompt, do_sample=False, temperature=1.0, top_p=1, max_new_tokens=max_new_tokens)
  return generation[0]['generated_text']

@app.get("/generate")
async def generate(uc: str):
  if uc == "" or uc is None:
    return {"response": "Please provide the prompt"}
  else:
    prompt = formatPrompt(uc)
    generatedText = getGeneratedText(prompt)
    generatedContent = generatedText[1]["content"]
    return {"response": generatedContent}