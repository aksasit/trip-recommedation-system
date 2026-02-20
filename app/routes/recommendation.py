from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.recommender import (
    collaborative_recommendation,
    predict_popularity
)

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/recommendation", response_class=HTMLResponse)
async def recommendation_page(request: Request):
    return templates.TemplateResponse(
        "recommendation.html",
        {"request": request}
    )
    
@router.post("/recommend", response_class=HTMLResponse)
async def recommend(
    request: Request,
    user_id: int = Form(...),
    name: str = Form(...),
    type: str = Form(...),
    state: str = Form(...),
    best_time: str = Form(...),
    preferences: str = Form(...),
    gender: str = Form(...),
    adults: int = Form(...),
    children: int = Form(...)   
):
    user_input = {
        "Name": name,
        "Type": type,
        "State": state,
        "BestTimeToVisit": best_time,
        "Preferences": preferences,
        "Gender": gender,
        "NumberOfAdults": adults,
        "NumberOfChildren": children,
    }
    
    recommendations = collaborative_recommendation(user_id)
    predicted_popularity= predict_popularity(user_input)
    
    return templates.TemplateResponse(
        "recommendation.html",
        {
            "request": request,
            "recommended_destinations": recommendations,
            "predicted_popularity": predicted_popularity
        }
    )