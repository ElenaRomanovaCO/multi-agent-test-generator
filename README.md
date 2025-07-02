# Simple FastAPI Project

A minimal FastAPI application with basic CRUD operations.

## Files Structure

- `main.py` - Main FastAPI application
- `config.py` - Configuration settings
- `requirements.txt` - Python dependencies
- `run.sh` - Quick start script
- `README.md` - This file

## Quick Start

### Option 1: Local Development

```bash
# Make run script executable
chmod +x run.sh

# Run the application
./run.sh
```

### Option 2: Direct Python

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 3: With Uvicorn directly

```bash
# Install dependencies
pip install -r requirements.txt

# Run with uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Configuration

You can customize the application using environment variables:

- `HOST` - Server host (default: 0.0.0.0)
- `PORT` - Server port (default: 8000)
- `DEBUG` - Enable debug mode (default: true)

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /items` - List all items
- `GET /items/{id}` - Get specific item
- `POST /items` - Create new item
- `PUT /items/{id}` - Update item
- `DELETE /items/{id}` - Delete item

## Access the API

- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## Example Usage

```bash
# Create an item
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{"name": "Widget", "description": "A useful widget", "price": 19.99}'

# Get all items
curl http://localhost:8000/items

# Get specific item
curl http://localhost:8000/items/1
```
