import json
from google import genai
from pydantic import BaseModel, Field
import config

# Initialize the Gemini client
client = genai.Client(api_key=config.GEMINI_API_KEY)

class BookRecommendation(BaseModel):
    title: str = Field(description="The title of the book")
    author: str = Field(description="The author of the book")
    genre: str = Field(description="The primary genre of the book")
    synopsis: str = Field(description="A brief 2-3 sentence synopsis of the book")
    why_it_fits: str = Field(description="A personalized 1-2 sentence explanation of why this book matches the user's specific mood")

class RecommendationList(BaseModel):
    books: list[BookRecommendation]

def get_book_recommendations(mood, pacing, setting, familiarity, recent_favorite):
    prompt = f"""
    You are an elite, highly empathetic AI librarian. Based on the following user preferences, 
    recommend exactly 3 books that perfectly match their current vibe.

    User Profile:
    1. Emotional State: {mood}
    2. Desired Pacing: {pacing}
    3. Desired Setting: {setting}
    4. Familiarity vs. Unconventional: {familiarity}
    5. Recent Favorite: {recent_favorite}

    Analyze these inputs deeply and provide 3 tailored book recommendations. 
    """

    try:
        # Attempt the live API call
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": RecommendationList,
            }
        )
        # Return the parsed data, and False (meaning it is NOT a fallback)
        return response.parsed, False  
        
    except Exception as e:
        print(f"API Error encountered: {e}") # Logs to your terminal for debugging
        
        # GTM Fallback: Load static JSON if the AI fails
        with open("data/fallback_books.json", "r", encoding="utf-8") as file:
            fallback_data = json.load(file)
            
        # Parse the raw JSON into our Pydantic model so the UI doesn't break
        # Return the parsed fallback data, and True (meaning it IS a fallback)
        return RecommendationList(**fallback_data), True