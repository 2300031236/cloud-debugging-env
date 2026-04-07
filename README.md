# Cloud System Debugging Environment (OpenEnv)

## 🚀 Overview
This project simulates a real-world cloud debugging scenario where an AI agent learns to diagnose and fix system issues such as disk overflow and service failures.

## 🎯 Objective
Train and evaluate an AI agent to:
- Identify system issues from logs
- Take corrective actions
- Restore system to a healthy state

## ⚙️ Environment Design

### State (Observation)
- logs: system error messages
- disk_usage: percentage usage
- service_status: running / down
- logs_cleaned: boolean flag

### Actions
- clean_logs
- restart_service
- check_status

### Goal
System is considered healthy when:
- disk_usage < 80
- service_status == running

## 🧪 Tasks
- Easy: Disk full issue
- Medium: Service failure
- Hard: Combined issues

## 🏆 Reward System
- +0.5 for fixing disk issue
- +0.5 for restoring service
- penalties for incorrect actions
- final_score ∈ [0.0, 1.0]

## 🤖 Inference & Evaluation
The agent runs multiple episodes and calculates:
- individual scores
- average performance

Example:Scores: [1.0, 1.0, 1.0]
Average: 1.0

## 📦 Deployment
- FastAPI backend
- Docker containerized
- Compatible with Hugging Face Spaces

## 💡 Key Insight
This project focuses on decision-making rather than execution — simulating how AI agents can reason about system failures in real-world environments.