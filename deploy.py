import os

# Code for deploying the FastAPI service on Truefoundry
# ...

if __name__ == "__main__":
    # Code to start the FastAPI service
    os.system("uvicorn app:app --host 0.0.0.0 --port 8000")
