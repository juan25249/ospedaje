from database import SessionLocal, engine, test_connection
from api import *
# Dependencia

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)