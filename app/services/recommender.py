import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models/model.pkl"
ENCODER_PATH = BASE_DIR / "models/label_encoders.pkl"

DESTINATION_PATH = BASE_DIR / "data/raw/destinations.csv"
USER_HISTORY_PATH = BASE_DIR / "data/raw/user_history.csv"

# Load model & encoders once
model = pickle.load(open(MODEL_PATH, "rb"))
label_encoders = pickle.load(open(ENCODER_PATH, "rb"))

destinations_df = pd.read_csv(DESTINATION_PATH)
user_history_df = pd.read_csv(USER_HISTORY_PATH)

# Build collaborative filtering matrix
user_item_matrix = user_history_df.pivot(
    index="UserID",
    columns="DestinationID",
    values="ExperienceRating"
).fillna(0)

user_similarity = cosine_similarity(user_item_matrix)

FEATURES = [
    "Name",
    "State",
    "Type",
    "BestTimeToVisit",
    "Preferences",
    "Gender",
    "NumberOfAdults",
    "NumberOfChildren"
]

def collaborative_recommendation(user_id: int):
    similar_users = user_similarity[user_id - 1]
    
    similar_users_idx = np.argsort(similar_users)[::-1][1:6]
    
    similar_user_ratings = (
        user_item_matrix
        .iloc[similar_users_idx]
        .mean(axis=0)
    )
    
    recommended_ids = (
        similar_user_ratings
        .sort_values(ascending=False)
        .head(5)
        .index
    )
    
    recommendations = destinations_df[
        destinations_df["DestinationID"].isin(recommended_ids)
    ][[
        "DestinationID",
        "Name",
        "State",
        "Type",
        "Popularity",
        "BestTimeToVisit"       
    ]]
    
    return recommendations.to_dict(orient="records")


def predict_popularity(user_input: dict):
    
    encoded_input = {}
    
    for feature in FEATURES:
        if feature in label_encoders:
            encoded_input[feature] = (
                label_encoders[feature]
                .transform([user_input[feature]])[0]
            )
        else:
            encoded_input[feature] = user_input[feature]
            
    input_df = pd.DataFrame([encoded_input])
    
    prediction = model.predict(input_df)[0]

    return float(prediction)     
    