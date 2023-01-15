# Full-stack Developer Recruitment Task 

This guide is for Linux systems only.

## Project setup (Fast API Backend)
Python version 3.10

Create python virtual environment and from the root directory run:
```
python -m venv venv
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run Fast API server
```
uvicorn main:app 
```
### Format code
```
black .
```

## Project setup (Vue Frontend)
From `/frontend` directory run:

### Install dependencies

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
