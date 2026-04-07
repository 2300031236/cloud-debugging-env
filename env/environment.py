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
        self.state["steps"] = 0
        return Observation(**self.state)

    def step(self, action: Action):
        self.state["steps"] += 1

        reward_value = 0.0

        # Apply actions
        if action.action_type == "clean_logs":
            self.state["disk_usage"] -= 50
            self.state["logs_cleaned"] = True
            reward_value += 0.5

        elif action.action_type == "restart_service":
            if self.state["disk_usage"] < 80:
                self.state["service_status"] = "running"
                reward_value += 0.5
            else:
                reward_value -= 0.2

        # Goal condition
        done = (
            self.state["disk_usage"] < 80 and
            self.state["service_status"] == "running"
        )

        # Failure condition
        if self.state["steps"] >= 5 and not done:
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

        final_score = grade(self.state)

        return (
            Observation(**self.state),
            Reward(score=reward_value),
            done,
            {"final_score": final_score}
        )

    def state_view(self):
        return self.state