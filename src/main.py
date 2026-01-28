from fastapi import FastAPI, HTTPException
import os
import json
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI()

# CORS (safe for portfolio)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent

@app.get("/")
async def me():
    try:
       with open('me.json',mode='r') as me_json:
            data = json.load(me_json)
    except FileNotFoundError:
        print(f"Error: The file was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file {me_json}.")
    return data

@app.get("/projects")
async def project():
    try:
       with open('projects.json',mode='r') as proj_json:
            data = json.load(proj_json)
    except FileNotFoundError:
        print(f"Error: The file was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file {proj_json}.")
    return data
@app.get("/projects/{id}")
async def project(id: int):
    try:
        with open("projects.json", "r") as proj_json:
            data = json.load(proj_json)

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="projects.json not found")

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON format")

    for project in data["projects"]:
        if project["id"] == id:
            return project

    raise HTTPException(status_code=404, detail=f"Project with id {id} not found")

    
@app.get("/blogs")
async def blog():
    try:
       with open('blogs.json',mode='r') as blog_json:
            data = json.load(blog_json)
    except FileNotFoundError:
        print(f"Error: The file was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file {blog_json}.")
    return data

@app.get("/blogs/{id}")
async def blog(id: int):
    try:
       with open('blogs.json',mode='r') as blog_json:
            data = json.load(blog_json)
    except FileNotFoundError:
        print(f"Error: The file was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file {blog_json}.")
    for blog in data["blogs"]:
        if blog["id"] == id:
            return blog

    raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")


@app.get("/{any_thing}")
async def not_avail(any_thing: str):
    return {"message":f"404 {any_thing} not found"} 


