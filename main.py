from app import app

from views.user_view import router as user_router


app.include_router(user_router)

@app.get("/")
def home():
    return "Home Page"
