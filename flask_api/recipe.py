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
# modify based on the ingredients 
def instructions_gen(ingredients, food_prompt):
    print('Activated OPENAI INSTRUCTIONS')
    response = openai.ChatCompletion.create(
      engine=OPENAI_MODEL,
      messages=[
        {
          "role": "system",
          "content": "You are a top level chef and you ONLY want to create a numbered list of instrunctions without a title on how to make a classic version of a dish with the ingredients you are given. You only want to say the instructions, nothing else extra." 
        },
        {
          "role": "user",
          "content": ingredients
        },
        {
          "role": "system",
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
      
    # remove all '' empty strings 
    finalIngredients = []
    for i in range(len(ingredients)):
        if ingredients[i] != '' and ingredients[i] != None:
            finalIngredients.append(ingredients[i])
    return finalIngredients

#this will use the api for the meal website
#if a food doesnt exist, it will return false 
#
def ingredients_gen(food_prompt):
        hasFood= foodExists(food_prompt)
        if hasFood:
            print('Activated mealDB')
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food_prompt}"
            response = requests.get(url)
            data ={"key1": "value1","key2":"value2"} # data to send
            response = requests.post(url,data=data) #update data 
            response_data = response.json()
            mealInfo = response_data["meals"][0] # return the information for the meal 
            ingredients = []
            index=0
            for key in mealInfo:
                if 'strIngredient' in key:
                    # check for empty keys and don't append them 
                    if mealInfo[key] != "" and mealInfo[key] != None:
                        ingredients.append(mealInfo[key])
                    #print(mealInfo[key])
                    index+=1
            #print(ingredients)
            return ingredients
        else:
            print('Activated OpenAI')
            return openAI_ingredients(food_prompt)


def getRecipe(foodPrompt):
    # Note:  ingredients_gen(foodPrompt) is a list 
    ingredientList = ingredients_gen(foodPrompt)
    # turn ingredient list into a string for food prompt (because it's a list and can't be used for OpenAi api -> Content invalid)
    ingredientString = " ".join(ingredientList)
    recipe=[ingredientList, instructions_gen(ingredientString, foodPrompt)]
    return recipe

def foodExists(food_prompt):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food_prompt}"
    data = requests.get(url)
    data2= data.json()
    mealInfo = data2["meals"]
    if mealInfo == None:
        return False
    return True

#print(getRecipe("pizza"))

