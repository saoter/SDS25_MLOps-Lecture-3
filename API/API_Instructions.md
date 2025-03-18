# 🚀 FastAPI Server Setup Guide (DEVELPOMENT)

This guide explains how to set up a FastAPI server, including creating a virtual environment, installing dependencies, writing the FastAPI app, and starting the server in the background.

---

## ✅ Step 1: Create a Virtual Environment
Create a virtual environment to keep the dependencies isolated:

```bash
python3 -m venv fastapi_env

source fastapi_env/bin/activate
```



## ✅ Step 2: Install Dependencies

```bash
pip install fastapi[all] uvicorn SQLAlchemy #api & supporting server & SQL toolkit
```

## ✅ Step 3: Write the FastAPI App (main.py)

#### 3.1 Create a project folder and app directory:

```bash
mkdir -p my_fastapi_project/app
cd my_fastapi_project/app
mkdir data  # here we will save our database
```


#### 3.2 Create main.py and add the following FastAPI app code:

Look at 'main_base.py' for details.


## ✅ Step 4: Run the server

```bash
#From folder 'app' run this command:
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 & #Start server in the background
```
