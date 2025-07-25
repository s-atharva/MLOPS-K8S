from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model = joblib.load("iris_model.pkl")


@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})


@app.post("/", response_class=HTMLResponse)
def form_post(request: Request,
              sepal_length: float = Form(...),
              sepal_width: float = Form(...),
              petal_length: float = Form(...),
              petal_width: float = Form(...)):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    return templates.TemplateResponse("form.html", {
        "request": request,
        "result": prediction,
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    })
