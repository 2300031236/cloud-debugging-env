from env.models import Observation, Action, Reward
from env.tasks import TASKS
from env.grader import grade
import random

class CloudEnv:

    def __init__(self):
        self.state = None

    def reset(self):
        task = random.choice(TASKS)
        self.state = task["state"].copy()
        return Observation(**self.state)

    def step(self, action: Action):

        if self.state is None:
            raise ValueError("Call reset() first")

        reward_value = 0.0

        # Action: clean_logs
        if action.action_type == "clean_logs":
            if self.state["disk_usage"] >= 80:
                self.state["disk_usage"] = 50
                self.state["logs_cleaned"] = True
                reward_value += 0.5
            else:
                reward_value -= 0.2

        # Action: restart_service
        elif action.action_type == "restart_service":
            if self.state["service_status"] == "down":
                self.state["service_status"] = "running"
                reward_value += 0.5
            elif self.state["service_status"] == "running":
                reward_value -= 0.2

        # Action: check_status
        elif action.action_type == "check_status":
            reward_value += 0.1

        else:
            raise ValueError("Invalid action_type")

        # Goal condition
        done = (
            self.state["disk_usage"] < 80 and
            self.state["service_status"] == "running"
        )

        final_score = grade(self.state)

        return (
            Observation(**self.state),
            Reward(score=round(reward_value, 2)),
            done,
            {"final_score": final_score}
        )
        # Goal condition
done = (
    self.state["disk_usage"] < 80 and
    self.state["service_status"] == "running"
)

# Failure condition (too many steps)
if self.state.get("steps", 0) >= 5 and not done:
    return (
        Observation(**self.state),
        Reward(score=-1.0),
        True,
        {
            "final_score": 0.0,
            "status": "failed",
            "reason": "max steps exceeded"
        }
    )

    def state_view(self):
        return self.state