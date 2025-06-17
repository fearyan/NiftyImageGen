from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_list_models():
    """Test the models endpoint"""
    response = client.get("/api/v1/models")
    assert response.status_code == 200
    assert "models" in response.json()
    models = response.json()["models"]
    assert len(models) > 0
    assert all("id" in model and "name" in model for model in models)

def test_list_workflows():
    """Test the workflows endpoint"""
    response = client.get("/api/v1/workflows")
    assert response.status_code == 200
    assert "workflows" in response.json()
    workflows = response.json()["workflows"]
    assert len(workflows) > 0
    assert all("id" in workflow and "name" in workflow for workflow in workflows)

def test_generate_image():
    """Test the image generation endpoint"""
    test_request = {
        "prompt": "a beautiful sunset over mountains",
        "model": "SDXL",
        "workflow": "default",
        "num_images": 1,
        "width": 512,
        "height": 512
    }
    response = client.post("/api/v1/generate", json=test_request)
    assert response.status_code == 200
    assert "status" in response.json()
    assert response.json()["status"] == "success" 