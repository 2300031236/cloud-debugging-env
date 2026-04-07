def grade(state):
    score = 0.0

    if state["disk_usage"] < 80:
        score += 0.5

    if state["service_status"] == "running":
        score += 0.5

    return round(score, 2)