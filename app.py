from fastapi import FastAPI
from env.environment import CloudEnv
from env.models import Action

app = FastAPI()

env = CloudEnv()

@app.get("/")
def home():
    return {"status": "Cloud Debugging Environment running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.model_dump()

@app.post("/step")
def step(action: Action):
    try:
        obs, reward, done, info = env.step(action)

        return {
            "observation": obs.model_dump(),
            "reward": reward.score,
            "done": done,
            "info": info
        }

    except Exception as e:
        return {"error": str(e)}

@app.get("/state")
def state():
    return env.state_view()