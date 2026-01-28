from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json


app = FastAPI(title="Know Me Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent


def load_json(filename: str):
    path = BASE_DIR / filename

    if not path.exists():
        raise HTTPException(
            status_code=500,
            detail=f"{filename} not found on server"
        )

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid JSON format in {filename}"
        )


@app.get("/")
async def get_me():
    return load_json("me.json")


@app.get("/projects")
async def get_projects():
    return load_json("projects.json")


@app.get("/projects/{project_id}")
async def get_project_by_id(project_id: int):
    data = load_json("projects.json")

    for project in data.get("projects", []):
        if project.get("id") == project_id:
            return project

    raise HTTPException(
        status_code=404,
        detail=f"Project with id {project_id} not found"
    )


@app.get("/blogs")
async def get_blogs():
    return load_json("blogs.json")


@app.get("/blogs/{blog_id}")
async def get_blog_by_id(blog_id: int):
    data = load_json("blogs.json")

    for blog in data.get("blogs", []):
        if blog.get("id") == blog_id:
            return blog

    raise HTTPException(
        status_code=404,
        detail=f"Blog with id {blog_id} not found"
    )
