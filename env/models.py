from pydantic import BaseModel

class Observation(BaseModel):
    logs: str
    disk_usage: int
    service_status: str
    logs_cleaned: bool

class Action(BaseModel):
    action_type: str  # clean_logs | restart_service | check_status

class Reward(BaseModel):
    score: float