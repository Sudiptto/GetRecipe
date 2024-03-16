import openai
from passwords import *


openai.api_key = key
openai.api_base = base 
openai.api_type = api_type
openai.api_version = "2023-03-15-preview"
OPENAI_MODEL = "gpt-35-turbo"

# generate instructions on how to make a dish given a list of ingredients 
def instructions_gen(txt_prompt,ing_list):
  response = openai.ChatCompletion.create(
    engine=OPENAI_MODEL,
    messages=[
      {
        "role": "system",
        "content": "You are a top level chef and you ONLY want to create a numbered list of instrunctions without a title on how to make a classic version of a dish with the ingredients you are given. You only want to say the instructions, nothing else extra." 
      },
      {
        "role": "user",
        "content": txt_prompt
      },
    ])
  generated_text = response['choices'][0]['message']['content']
  instructions = generated_text.split("\n") # turn string to a list
  for i in range(len(instructions)):
    instructions[i] = instructions[i][3:]

  return instructions

# return an array/list of ingredients that are needed for the dish
def ingredients_gen(txt_prompt):
  response = openai.ChatCompletion.create(
    engine=OPENAI_MODEL,
    messages=[
      {
        "role": "system",
        "content": "You are a chef that wants to list as little ingredients as possible that are NOT OPTIONAL to make the a classic version of a dish. List each ingredient(ONLY the ingredient) without additional text on its own line and number it." #You will create one list in python for the ingredients, and then generate another string with instrunctions on how to make the dish with given ingredients."
      },
      {
        "role": "user",
        "content": txt_prompt
      },
    ])
  generated_text = response['choices'][0]['message']['content']
  ingredients = generated_text.split("\n")
  for i in range(len(ingredients)):
    ingredients[i] = ingredients[i][3:]
      
  
  return ingredients

def getRecipe(foodPrompt):
    recipe=[ingredients_gen(foodPrompt),instructions_gen(foodPrompt,ingredients_gen(foodPrompt))]
    return recipe


#print(ingredients_gen('bengali biryani'))
food = "cookies and cream ice cream"
#print(instructions_gen(food,ingredients_gen(food)))
print(getRecipe(food))

