import pandas as pd 
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from spellchecker import SpellChecker


brands=pd.read_csv('brands.csv')
categorys=pd.read_csv('category.csv')
colors=pd.read_csv('color.csv')
genders=pd.read_csv('gender.csv')
materials=pd.read_csv('material.csv')
brands=brands.iloc[:,0]
brands=brands.tolist()
categorys=categorys.iloc[:,0]
categorys=categorys.tolist()
colors=colors.iloc[:,0]
colors=colors.tolist()
genders=genders.iloc[:,0]
genders=genders.tolist()
materials=materials.iloc[:,0]
materials=materials.tolist()

brands=[str(item) for item in brands]
categories=[str(item) for item in categorys]
colors=[str(item) for item in colors]
genders=[str(item) for item in genders]
materials=[str(item) for item in materials]









# List of brand names, categories, colors, and genders


# Initialize spell checker
spell_checker = SpellChecker(language="en")

# Function to generate training data
def generate_training_data(brands, categories, colors, genders):
    training_data = []
    for brand in brands:
        for category in categories:
            for color in colors:
                for gender in genders:
                    searched_product = f"{color} {category} from {brand} for {gender}"
                    result_product = f"{color} {category} from {brand} for {gender}"
                    relevance = 4  # Perfect
                    training_data.append((searched_product, result_product, relevance))
                    result_product = f"{color} {category} from {np.random.choice(brands)} for {gender}"
                    relevance = 2  # Good
                    training_data.append((searched_product, result_product, relevance))
                    result_product = f"{color} {category} from {np.random.choice(brands)} for {np.random.choice(genders)}"
                    relevance = 1  # Fair
                    training_data.append((searched_product, result_product, relevance))
                    result_product = f"{np.random.choice(colors)} {np.random.choice(categories)} from {np.random.choice(brands)} for {np.random.choice(genders)}"
                    relevance = 0  # Poor
                    training_data.append((searched_product, result_product, relevance))
    return training_data



# Generate training data
training_data = generate_training_data(brands, categories, colors, genders)
df = pd.DataFrame(training_data, columns=["Searched Product", "Result Product", "Relevance"])




df.to_csv('generated_data.csv')