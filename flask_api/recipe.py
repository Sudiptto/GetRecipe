import openai
import requests
from passwords import *


openai.api_key = key
openai.api_base = base 
openai.api_type = api_type
openai.api_version = "2023-03-15-preview"
OPENAI_MODEL = "gpt-35-turbo"

#url to get info for meal 
url = "https://www.themealdb.com/api/json/v1/1/search.php?s="

# generate instructions on how to make a dish given a list of ingredients 
def instructions_gen(food_prompt,ing_list):
    response = openai.ChatCompletion.create(
    engine=OPENAI_MODEL,
    messages=[
      {
        "role": "system",
        "content": "You are a top level chef and you ONLY want to create a numbered list of instrunctions without a title on how to make a classic version of a dish with the ingredients you are given. You only want to say the instructions, nothing else extra." 
      },
      {
        "role": "user",
        "content": food_prompt
      },
    ])
    generated_text = response['choices'][0]['message']['content']
    instructions = generated_text.split("\n") # turn string to a list
    for i in range(len(instructions)):
        instructions[i] = instructions[i][3:]

    return instructions

# return an array/list of ingredients that are needed for the dish
def openAI_ingredients(food_prompt):
    response = openai.ChatCompletion.create(
    engine=OPENAI_MODEL,
    messages=[
      {
        "role": "system",
        "content": "You are a chef that wants to list as little ingredients as possible that are NOT OPTIONAL to make the a classic version of a dish. List each ingredient(ONLY the ingredient) without additional text on its own line and number it." #You will create one list in python for the ingredients, and then generate another string with instrunctions on how to make the dish with given ingredients."
      },
      {
        "role": "user",
        "content": food_prompt
      },
    ])
    generated_text = response['choices'][0]['message']['content']
    ingredients = generated_text.split("\n")
    for i in range(len(ingredients)):
        ingredients[i] = ingredients[i][3:]
      
  
    return ingredients

#this will use the api for the meal website
#if a food doesnt exist, it will return false 
#
def ingredients_gen(food_prompt):
        hasFood= foodExists(food_prompt)
        if hasFood:
            instructions =[]
            url += food_prompt
            response = requests.get(url)
            data ={"key1": "value1","key2":"value2"} # data to send
            response = requests.post(url,data=data) #update data 
            response_data = response.json()
            mealInfo = response_data["meals"][0] # return the information for the meal 
            instructions = mealInfo["strInstructions"]
            ingredients = []
            index=0
            for key in mealInfo:
                if 'strIngredient' in key:
                    ingredients.append(mealInfo[key])
                    index+=1
            return ingredients
        else:
            return openAI_ingredients(food_prompt)


def getRecipe(foodPrompt):
    recipe=[ingredients_gen(foodPrompt),instructions_gen(foodPrompt,ingredients_gen(foodPrompt))]
    return recipe

def foodExists(food_prompt):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food_prompt}"
    data = requests.get(url)
    data2= data.json()
    mealInfo = data2["meals"]
    if mealInfo == None:
        return False
    return True



