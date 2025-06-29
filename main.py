from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS (allow requests from any origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or replace "*" with ["http://127.0.0.1:5500"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to load JSON file
def load_json(file_name):
    with open(file_name, encoding='utf-8') as f:
        return json.load(f)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the English Learning API"}

# Route for Basic level questions
@app.get("/basic")
def get_basic():
    data = load_json("basic.json")
    return JSONResponse(content=data)

# Route for Beginner level questions
@app.get("/beginner")
def get_beginner():
    data = load_json("beginner.json")
    return JSONResponse(content=data)

# Route for Intermediate level questions
@app.get("/intermediate")
def get_intermediate():
    data = load_json("Intermediate.json")
    return JSONResponse(content=data)

# Route for Fluent level questions
@app.get("/fluent")
def get_fluent():
    data = load_json("Fluent.json")
    return JSONResponse(content=data)

# Dynamic route by file name
@app.get("/level/{level_name}")
def get_level(level_name: str):
    file_name = f"{level_name}.json"
    try:
        data = load_json(file_name)
        return JSONResponse(content=data)
    except FileNotFoundError:
        return JSONResponse(content={"error": "File not found"}, status_code=404)
