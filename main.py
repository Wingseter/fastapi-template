from fastapi import FastAPI
from routes.users import user_router

import uvicorn

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Welcome to the ToDo API"
    }

app.include_router(user_router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)