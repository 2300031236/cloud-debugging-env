import requests

BASE_URL = "http://localhost:7860"


def run_episode():
    # Reset environment
    res = requests.post(f"{BASE_URL}/reset")
    obs = res.json()

    done = False
    final_score = 0.0

    # Step 1: clean logs if needed
    if obs["disk_usage"] >= 80:
        res = requests.post(f"{BASE_URL}/step", json={
            "action_type": "clean_logs"
        })
        result = res.json()

        if "error" in result:
            print("Error:", result["error"])
            return 0.0

        obs = result["observation"]
        done = result["done"]
        final_score = result["info"]["final_score"]

        if done:
            return final_score

    # Step 2: restart service if needed
    if obs["service_status"] == "down":
        res = requests.post(f"{BASE_URL}/step", json={
            "action_type": "restart_service"
        })
        result = res.json()

        if "error" in result:
            print("Error:", result["error"])
            return 0.0

        obs = result["observation"]
        done = result["done"]
        final_score = result["info"]["final_score"]

        if done:
            return final_score

    # If still not done → partial or failure
    return final_score


if __name__ == "__main__":
    scores = []

    for i in range(3):
        score = run_episode()
        scores.append(score)
        print(f"Episode {i+1} Score: {score}")

    avg_score = sum(scores) / len(scores)

    print("\nFinal Results")
    print("Scores:", scores)
    print("Average:", avg_score)

    # Show success vs failure clearly
    if avg_score == 1.0:
        print("✅ All tasks solved successfully")
    elif avg_score >= 0.5:
        print("⚠️ Partial success — some issues not fully resolved")
    else:
        print("❌ Agent failed to solve tasks properly")