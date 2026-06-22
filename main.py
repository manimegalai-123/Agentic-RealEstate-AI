from fastapi import FastAPI
from database.database import engine
from database.models import Base
from routes.property_routes import router as property_router
from routes.image_routes import router as image_router
from routes.classification_routes import router as classification_router
from routes.prediction_routes import router as prediction_router
from routes.pipeline_routes import router as pipeline_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.interest_routes import router as interest_router
from routes.poster_routes import router as poster_router
from routes.approve_routes import router as approve_router

app = FastAPI()

app.mount(
    "/posters",
    StaticFiles(directory="posters"),
    name="posters"
)




app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(property_router)

app.include_router(image_router)

app.include_router(classification_router)

app.include_router(prediction_router)

app.include_router(pipeline_router)

app.include_router(interest_router)

app.include_router(poster_router)

app.include_router(approve_router)

@app.get("/")
def home():
    return {"message": "Backend Running"}