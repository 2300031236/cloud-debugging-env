TASKS = [
    {
        "id": "easy",
        "state": {
            "logs": "Disk usage 100%. No space left.",
            "disk_usage": 100,
            "service_status": "running",
            "logs_cleaned": False
        }
    },
    {
        "id": "medium",
        "state": {
            "logs": "Service crashed unexpectedly.",
            "disk_usage": 50,
            "service_status": "down",
            "logs_cleaned": False
        }
    },
    {
        "id": "hard",
        "state": {
            "logs": "Disk full. Service crashed.",
            "disk_usage": 100,
            "service_status": "down",
            "logs_cleaned": False
        }
    }
]