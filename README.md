# MLOPS-K8S
**Iris Prediction App** – MLOps Deployment with Docker & Kubernetes
This project demonstrates deploying a simple Iris flower classification app using:

1. FastAPI for model serving
2. Docker for containerization
3. Kubernetes (GKE) for orchestration on the cloud
4. HTML templates for Frontend
5. Logistic Regression as Model

**API Request**

* POST /predict

         {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
          }
* Response

        {
          "prediction": "setosa"
        }
