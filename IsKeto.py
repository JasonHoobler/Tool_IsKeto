# Simple app that determines if a food item is macronutriently keto.
# Fat 60 - 75%
# Carb 5 - 10%
# Pro 15 - 35%

grams_of_fat = 0
cals_of_fat = 0
percent_of_cals_from_fat = 0
grams_of_carbs = 0
cals_of_carbs = 0
percent_of_cals_from_carbs = 0
grams_of_protein = 0
cals_of_protein = 0
percent_of_cals_from_protein = 0
total_cals = 0
is_keto = True
output_offending_macro = ""

grams_of_fat = int(input("Please enter grams of fat: "))
grams_of_carbs = int(input("Please enter grams of carbohydrates: "))
grams_of_protein = int(input("Please enter grams of protein: "))

cals_of_fat = grams_of_fat * 9
cals_of_carbs = grams_of_carbs * 4
cals_of_protein = grams_of_protein * 4
total_cals = cals_of_fat + cals_of_carbs + cals_of_protein

percent_of_cals_from_fat = cals_of_fat / total_cals * 100
if percent_of_cals_from_fat < 60:
    is_keto = False
    output_offending_macro = output_offending_macro + "Fats are too low.  Calories form fat should be between 60 - 75%.  This food item contains " + str(round(percent_of_cals_from_fat)) + "%."
elif percent_of_cals_from_fat > 75:
    is_keto = False
    output_offending_macro = output_offending_macro + "Fats are too high.  Calories from fat should be between 60 - 75%.  This food item contains " + str(round(percent_of_cals_from_fat)) + "%."

percent_of_cals_from_carbs = cals_of_carbs / total_cals * 100
if percent_of_cals_from_carbs > 10:
    is_keto = False
    output_offending_macro = output_offending_macro + "Carbohydrates are too high. Calories from carbs should be less than 10%.  This food item contains " + str(round(percent_of_cals_from_carbs)) + "%."

percent_of_cals_from_protein = cals_of_protein / total_cals * 100
if percent_of_cals_from_protein < 15:
    is_keto = False
    output_offending_macro = output_offending_macro + "Proteins are too low.  Calories from protein should be between 15 - 30%.  This food item contains " + str(round(percent_of_cals_from_protein)) + "%."
elif percent_of_cals_from_protein > 30:
    is_keto = False
    output_offending_macro = output_offending_macro + "Proteins are too high.  Calories from protein should be between 4815 - 30%.  This food item contains " + str(round(percent_of_cals_from_protein)) + "%."

if is_keto:
    print("\nYay!  It's keto friendly!")
else:
    print("\nNo good.  Don't eat it.")
    print(output_offending_macro)
    print("This food items:")
    print("    Fat: ", int(round(percent_of_cals_from_fat)), "\b%        Goal: 60 - 75%")
    print("  Carbs: ", int(round(percent_of_cals_from_carbs)), "\b%        Goal: < 10%")
    print("Protein: ", int(round(percent_of_cals_from_protein)), "\b%        Goal: 15 - 30%")