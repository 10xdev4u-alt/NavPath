from fastapi import FastAPI
app = FastAPI()

@app.post("/robots/register")
def register_robot(robot_id: str):
    return {"status": "registered", "id": robot_id}
