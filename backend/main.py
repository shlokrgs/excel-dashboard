from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import file_routes

app = FastAPI()

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(file_routes.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Excel Dashboard API is live!"}
