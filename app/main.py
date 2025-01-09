from fastapi import FastAPI
# from app.routes.user_routes import user_router

app = FastAPI(title="FastAPI Example", version="1.0.0")

# Include routes
# app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}
