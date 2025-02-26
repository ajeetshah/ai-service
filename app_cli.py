import argparse
import torch
from transformers import pipeline

model = "meta-llama/Llama-3.2-1B-Instruct"
max_new_tokens=500

def getGenerator():
  device = "cuda" if torch.cuda.is_available() else "cpu"
  return pipeline(model=model, device=device, torch_dtype=torch.bfloat16)

generator = getGenerator()

def getPromptContent():
  parser = argparse.ArgumentParser(
    prog='AI Service',
    description='Get your queries answered by AI',
    epilog='Thanks for using AI Service'
  )
  parser.add_argument("-uc", "--user-content", help="User Content of prompt. Required.", type=str, required=True)
  parser.add_argument("-sc", "--system-content", help="System Content of prompt. Optional.", type=str, required=False)
  args = parser.parse_args()
  return (args.user_content, args.system_content)

def formatPrompt(userContent, systemContent = ""):
  prompt = [
    {"role": "user", "content": userContent}
  ]
  if systemContent != "":
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

if __name__ == "__main__":
  userContent, systemContent = getPromptContent()
  if userContent != "" and userContent is not None :
    prompt = formatPrompt(userContent, systemContent)
    generatedText = getGeneratedText(prompt)
    filtered = filterByAssistantRole(generatedText)
    assistantContent = filtered[0]["content"]
    print(f"generatedContent: {assistantContent}")
  else:
    print("Enter the user content of Prompt.")
