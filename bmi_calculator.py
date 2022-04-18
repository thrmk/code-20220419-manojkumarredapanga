import pandas as pd

input_params = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

for i in range(len(input_params)):
    input_params[i]["BMI"] = input_params[i]["WeightKg"] / (input_params[i]["HeightCm"]/100)**2
    bmi = input_params[i]["BMI"]
    if bmi <= 18.4:
        input_params[i]["BMI Category"] = "Underweight"
        input_params[i]["Health risk"] = "Malnutrition risk"
    elif bmi >= 18.5 and bmi <=24.9:
        input_params[i]["BMI Category"] = "Normal weight"
        input_params[i]["Health risk"] = "Low risk"
    elif bmi >= 25 and bmi <=29.9:
        input_params[i]["BMI Category"] = "Overweight"
        input_params[i]["Health risk"] = "Enhanced risk"
    elif bmi >= 30 and bmi <=34.9:
        input_params[i]["BMI Category"] = "Moderately obese"
        input_params[i]["Health risk"] = "Medium risk"
    elif bmi >= 35 and bmi <=39.9:
        input_params[i]["BMI Category"] = "Severely obese"
        input_params[i]["Health risk"] = "High risk"
    elif bmi >= 40:
        input_params[i]["BMI Category"] = "Very severely obese"
        input_params[i]["Health risk"] = "Very high risk"

df = pd.DataFrame(input_params)
# print(df)
categories_list = list(df["BMI Category"].unique())

for x in categories_list:
    print("No. of '{}' people = ".format(x),len(df[df["BMI Category"]==x]))