import random
random_number = random.randint(1, 7)
random_number2 = random.randint(1, 7) #I am inserting another random.randint function so I may use the random mondule twice in this program.
print("WELCOME TO RANDOM FOOD RECIPE GENERATOR")

#I defined a function here because I will need to call this same code again when generating the second recipe.
def generateRecipe(action):
  while True:
    decision = input(f"Are you ready to generate the {action} random recipe? ")
    decision = decision.lower()
    if decision == "yes" or decision == "yeah" or decision == "yup" or decision == "sure":
      print(f"\nGreat! Here is the {action} recipe.")
      break
    elif decision == "no" or decision == "nope" or decision == "nah":
      print("\nThat's too bad. Maybe next time.")
      exit("Participant did not want to generate the recipe.")
      # program will end here if answer is "no, nope, or nah", is inputted.
    else:
      print("\nYou've made an error")
      print("To continue, enter yes, yeah, yup, or sure.")
      print("To end the program, enter no, nope, or nah.")
      continue

generateRecipe("first")

#All recipes all put into a dictionary; the key being the name of the recipe, as well as the value being the ingredients.
tuscanChicken = {"\nTuscan Chicken Mac and Cheese": " 2 skinless boneless chicken breasts, salt, 1/2 teaspoon paprika, 1/2 teaspoon dried parsley, 1 tablespoon oil, 2 tablespoons butter, 1 yellow onion, 6 cloves garlic, 1/3 cup white wine or chicken broth, 250g sun dried tomato strips in oil, 3 level tablespoons flour, 2 cups chicken broth, 3 cups milk, 2 teaspoons dried italian herbs, 300g elbow macaroni, 1 cup parmesan cheese, 3/4 up mozzarella cheese, 1/2 cup grated cheese, 2 tablespoons fresh parsley"}
teryakiBowl = {"\nTeryaki Chicken Bowl": " 0.7 lb chicken breast, 4 cups broccoli, 3/4 cups rice, 2 tsp avocado oil, 2 tbsp mirin, 2 tbsp sake, 2 tbsp soy sauce, 1 tbsp honey, 1 garlic clove, 1 tsp ginger, 2 tbsp cornstarch, 4 tbsp water"}
santaFe = {"\nSanta Fe Baked Chicken": " 4 boneless skinless chicken breasts, salt, pepper, 4 tsp taco seasoning, 15 oz can black beans, 2 cups corn kernels, 1 1/2 cups salsa, 1/4 cup cilantro, 1 cup mexican cheese blend, 4 oz can green chilies, sour cream"}
ranchWrap = {"\nRanch Chicken Wrap": " 2 cups chicken breasts, 1/4 cup ranch, 1/2 cup mozzarella cheese, 1/4 cup cilantro, 1 avocado, 2 tbsp lemon juice, lettuce, 4 tortillas, hot sauce"}
garlicBaked = {"\nGarlic Butter Oven Baked Tilapia": " 4 tilapia fillets, salt, black pepper, 1/2 tsp paprika, 1/2 tsp dried thyme, 1/2 tsp dried oregano, 4 tbsp butter, 4 garlic cloves, 2 tbsp lemon juice, 1/4 tsp lemon zest, 1 lemon, red pepper flakes, fresh parsley, sliced lemons"}
honeySalmon = {"\nHoney Sriracha Salmon": " 2 salmon fillets, salt, pepper, 1 tsp avocado oil (or vegeatable oil), 1 garlic clove, tbsp sriracha, 1 tbsp lime juice, 3 tbsp hobey, 1/2 tbsp olive oil, 1 1/2 tbsp soy sauce, 1 1/2 tbsp water"}
thaiBurgers = {"\nThai Turkey Burgers with Crunch Asain Slaw": " 1 lb ground turkey, 3 tbsp shallot (diced, or red onion), 1 1/2 tsp ginger (fresh grated or chopped), 2 garlic cloves (finely minced or 1 tsp granulated garlic), 1 tbsp lemongrass (finely chopped), 2 tbsp thai basil (chopped, or cilantro), 1 tsp lime zest, 1 scallion (chopped), 0.5 jalapeño (seeded, finely chopped, or 1 tbsp sriracha), 1 tbsp fish sauce (or sub soy sauce), 1 tsp sugar, 1/4 tsp white pepper, 1 cup carrots (grated), 1 cup purple cabbage (shredded), 1 scalion (thinly sliced), 2 tbsp lime juice (or rice wine vinegar), 1 tbsp olive oil, 1/4 tsp salt, 1/4 tsp pepper 1/4 mayo (vegan mayo or tarter sauce), 1 tbsp sriracha (or chilli garlic sauce)"}

#I defined a function that will be used to call in on the recipes in dictionaries.
def recipeList(recipe):
  for title, details in recipe.items():
    print(title)
  detailList = details.split(",")
  for liSt in detailList:
    print(liSt)

print("\nHere is your first random recipe:")
#I defined a function to pretty much tag the recipes with a number, so when a random number is generated, then the recipe corresponding to that number will print
def randomRecipe(num):
  if num == 1:
    recipeList(tuscanChicken) #I am calling my defined function for the recipes that are dictionaries and using them as a parameter for when a random number is generated.
  elif num == 2:
    recipeList(teryakiBowl)
  elif num == 3:
    recipeList(santaFe)
  elif num == 4:
    recipeList(ranchWrap)
  elif num == 5:
    recipeList(garlicBaked)
  elif num == 6:
    recipeList(honeySalmon)
  elif num == 7:
    recipeList(thaiBurgers)

#I call my defined function here with the parameter being one of the random number so that a recipe will generate randomly.
randomRecipe(random_number)

generateRecipe("second")
print("\nOk, here is the second recipe:")

#I use the same defined function to call a random number again, but using the random number variable that saved the second random.randit function
randomRecipe(random_number2)
print("\nYour two recipes have been randomly genrerated. Enjoy!")
