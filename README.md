# NiftyImageGen

A powerful image generation and adaptation platform built with ComfyUI and FastAPI, demonstrating advanced AI capabilities and modern web integration.

## Features

- ComfyUI workflow integration for image generation
- RESTful API endpoints for image generation and adaptation
- Support for multiple base models (SDXL, Flux.1)
- Image adaptation and style transfer capabilities
- Clean and maintainable codebase with comprehensive documentation

## Project Structure

```
NiftyImageGen/
├── app/
│   ├── api/            # API endpoints
│   ├── core/           # Core functionality
│   ├── models/         # Data models
│   └── utils/          # Utility functions
├── comfy_workflows/    # ComfyUI workflow definitions
├── tests/             # Test suite
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```
5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once the server is running, visit `http://localhost:8000/docs` for interactive API documentation.

### Key Endpoints

- `POST /api/v1/generate`: Generate images using ComfyUI workflows
- `POST /api/v1/adapt`: Adapt existing images with style transfer
- `GET /api/v1/models`: List available base models
- `GET /api/v1/workflows`: List available ComfyUI workflows

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 