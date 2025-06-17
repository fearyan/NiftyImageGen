from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="NiftyImageGen API",
    description="A powerful image generation and adaptation platform built with ComfyUI",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ImageGenerationRequest(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = None
    model: str = "SDXL"
    workflow: str = "default"
    num_images: int = 1
    width: int = 512
    height: int = 512

class ImageAdaptationRequest(BaseModel):
    image_url: str
    style_prompt: str
    strength: float = 0.7
    model: str = "SDXL"

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to NiftyImageGen API"}

@app.get("/api/v1/models")
async def list_models():
    """List available base models"""
    return {
        "models": [
            {"id": "SDXL", "name": "Stable Diffusion XL"},
            {"id": "Flux.1", "name": "Flux 1.0"},
            {"id": "SD1.5", "name": "Stable Diffusion 1.5"}
        ]
    }

@app.get("/api/v1/workflows")
async def list_workflows():
    """List available ComfyUI workflows"""
    return {
        "workflows": [
            {"id": "default", "name": "Default Generation"},
            {"id": "style_transfer", "name": "Style Transfer"},
            {"id": "inpainting", "name": "Inpainting"}
        ]
    }

@app.post("/api/v1/generate")
async def generate_image(request: ImageGenerationRequest):
    """Generate images using ComfyUI workflows"""
    try:
        # TODO: Implement ComfyUI workflow execution
        return {
            "status": "success",
            "message": "Image generation request received",
            "request": request.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/adapt")
async def adapt_image(request: ImageAdaptationRequest):
    """Adapt existing images with style transfer"""
    try:
        # TODO: Implement image adaptation
        return {
            "status": "success",
            "message": "Image adaptation request received",
            "request": request.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 