from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import pickle
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model
model_path = os.path.join(os.path.dirname(__file__), "iris_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)


@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
def form_post(
        request: Request,
        sepal_length: float = Form(...),
        sepal_width: float = Form(...),
        petal_length: float = Form(...),
        petal_width: float = Form(...)
):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    species = ['setosa', 'versicolor', 'virginica'][prediction]
    return templates.TemplateResponse("form.html", {"request": request, "result": species})
