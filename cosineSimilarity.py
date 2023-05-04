import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

def getAPIResponse(data):


    df_preprocessed = pd.read_csv('./preprocessedDataV1.csv')

    df = df_preprocessed[['TranslatedIngredients', 'TranslatedInstructions','TranslatedRecipeName']].copy()

    # Preprocess the data
    df['TranslatedIngredients'] = df['TranslatedIngredients'].apply(lambda x: ' '.join(str(x).lower().split()))
    df['TranslatedInstructions'] = df['TranslatedInstructions'].apply(lambda x: ' '.join(x.lower().split()))

    # Convert each recipe's ingredients and instructions into a single string
    df['text'] = df['TranslatedIngredients'] + ' ' + df['TranslatedInstructions']

    # Tokenize each string
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['text'])

    # Compute the cosine similarity between the new list of ingredients and each recipe's list of ingredients
    new_ingredients = data

    new_text = ' '.join(new_ingredients)
    new_X = vectorizer.transform([new_text])
    similarity_scores = cosine_similarity(new_X, X)[0]

    # Rank the recipes based on their similarity score and select the top 5
    top_1_indices = similarity_scores.argsort()[::-1][:1]

    top_1_recipes_instruction = df.iloc[top_1_indices]['TranslatedInstructions']
    top_1_recipes_ingridient = df.iloc[top_1_indices]['TranslatedIngredients']
    top_1_recipes_recipe = df.iloc[top_1_indices]['TranslatedRecipeName']

    
    return {
        "instruction":list(top_1_recipes_instruction),
        "recipeName":list(top_1_recipes_recipe),
        "ingredients":list(top_1_recipes_ingridient)
    }
