from fastapi import FastAPI
app = FastAPI()

@app.get("/v2/fleet/status")
def fleet_status():
    return {"status": "all systems go"}
