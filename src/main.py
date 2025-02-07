"""from config.server.instance import server
from config.db.connection import create_connection
from modules.registration.register import api as register_api
from flask import request

app, api = server.app, server.api
# Create the database connection
connection = create_connection()
# Add the connection to the request context
@app.before_request
def before_request():
    request.connection = connection

# Register the routes
api.add_namespace(register_api)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()"""


from fastapi import FastAPI
from modules.register.routes import router
from dotenv import load_dotenv
import uvicorn

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="User Registration API",
    description="API for user registration using FastAPI, Pandas, and MySQL",
    version="1.0.0"
)

"""routers = [router1, router2, router3, ..., router100]
for router in routers:
    app.include_router(router)"""

app.include_router(router, prefix="/api")

@app.get("/", summary="Root Endpoint", description="Welcome message for the FastAPI application")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

if __name__ == "__main__":
    uvicorn.run("src:main:app", host="0.0.0.0", port=8000, reload=True)