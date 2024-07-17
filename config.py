import json
import os

# Initial configuration
initial_config = {
    "email": {
        "smtp_server": "smtp.yourserver.com",
        "smtp_port": 587,
        "username": "no-reply@senecaglobal.com",
        "password": "password"
    },
    "teams": {
        "webhook_url": "https://outlook.office.com/webhook/your_webhook_url"
    },
    "slack": {
        "webhook_url": "https://hooks.slack.com/services/your_webhook_url"
    },
    "scheduling": {
        "week_1_guy": "anmol.dhage@senecaglobal.com",
        "week_2_guy": "karanveer.singh.@senecaglobal.com",
        "week_3_guy": "sreekanth.pogula@senecaglobal.com",
        "responsibilities": [
            "1. Acknowledge",
            "2. Go through the debug steps and get in a call",
            "3. Provide the analysis we did at offshore to onshore"
        ]
    }
}


def save_config(config, filename="current_config.json"):
    with open(filename, "w") as file:
        json.dump(config, file, indent=4)


def load_config(filename="current_config.json"):
    with open(filename, "r") as file:
        return json.load(file)


# Save the initial configuration if the file does not exist
if not os.path.exists("current_config.json"):
    save_config(initial_config)
