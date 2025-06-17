import json
import os
from typing import Dict, Any, Optional
import requests
from pathlib import Path
from requests.exceptions import RequestException

class ComfyUIError(Exception):
    """Base exception for ComfyUI related errors"""
    pass

class ComfyUIWorkflow:
    def __init__(self, workflow_path: str):
        self.workflow_path = workflow_path
        self.workflow_data = self._load_workflow()

    def _load_workflow(self) -> Dict[str, Any]:
        """Load workflow configuration from JSON file"""
        try:
            with open(self.workflow_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise ComfyUIError(f"Workflow file not found: {self.workflow_path}")
        except json.JSONDecodeError:
            raise ComfyUIError(f"Invalid JSON in workflow file: {self.workflow_path}")

    def update_workflow_params(self, params: Dict[str, Any]) -> None:
        """Update workflow parameters"""
        for node_name, node_data in self.workflow_data['nodes'].items():
            if 'inputs' in node_data:
                for input_name, input_value in params.items():
                    if input_name in node_data['inputs']:
                        node_data['inputs'][input_name] = input_value

    def get_workflow_data(self) -> Dict[str, Any]:
        """Get current workflow data"""
        return self.workflow_data

class ComfyUIClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8188"):
        self.base_url = base_url

    def queue_prompt(self, workflow_data: Dict[str, Any]) -> Dict[str, Any]:
        """Queue a prompt for processing"""
        try:
            response = requests.post(
                f"{self.base_url}/prompt",
                json={"prompt": workflow_data},
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise ComfyUIError(f"Failed to queue prompt: {str(e)}")

    def get_image(self, filename: str) -> bytes:
        """Get generated image by filename"""
        try:
            response = requests.get(
                f"{self.base_url}/view?filename={filename}",
                timeout=30
            )
            response.raise_for_status()
            return response.content
        except RequestException as e:
            raise ComfyUIError(f"Failed to get image: {str(e)}")

    def get_history(self) -> Dict[str, Any]:
        """Get generation history"""
        try:
            response = requests.get(
                f"{self.base_url}/history",
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise ComfyUIError(f"Failed to get history: {str(e)}")

def load_workflow(workflow_name: str) -> Optional[ComfyUIWorkflow]:
    """Load a workflow by name"""
    workflow_path = Path(__file__).parent.parent.parent / "comfy_workflows" / f"{workflow_name}.json"
    if workflow_path.exists():
        return ComfyUIWorkflow(str(workflow_path))
    return None

def save_generated_image(image_data: bytes, output_dir: str, filename: str) -> str:
    """Save generated image to disk"""
    try:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'wb') as f:
            f.write(image_data)
        return output_path
    except (OSError, IOError) as e:
        raise ComfyUIError(f"Failed to save image: {str(e)}") 