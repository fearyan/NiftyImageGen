import unittest
from pathlib import Path
from app.utils.comfy_utils import ComfyUIWorkflow, ComfyUIClient

class TestComfyUIUtils(unittest.TestCase):
    def setUp(self):
        self.workflow_path = Path(__file__).parent.parent / "comfy_workflows" / "default.json"
        self.client = ComfyUIClient()

    def test_workflow_loading(self):
        """Test loading a workflow file"""
        workflow = ComfyUIWorkflow(str(self.workflow_path))
        self.assertIsNotNone(workflow.workflow_data)
        self.assertIn('nodes', workflow.workflow_data)

    def test_workflow_parameter_update(self):
        """Test updating workflow parameters"""
        workflow = ComfyUIWorkflow(str(self.workflow_path))
        test_params = {
            'width': 768,
            'height': 768,
            'steps': 30
        }
        workflow.update_workflow_params(test_params)
        workflow_data = workflow.get_workflow_data()
        
        # Check if parameters were updated
        empty_latent = workflow_data['nodes']['EmptyLatentImage']['inputs']
        self.assertEqual(empty_latent['width'], 768)
        self.assertEqual(empty_latent['height'], 768)

if __name__ == '__main__':
    unittest.main() 