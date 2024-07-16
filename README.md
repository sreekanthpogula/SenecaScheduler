### SenecaScheduler

**SenecaScheduler** is a Python-based automation tool designed to streamline the scheduling and notification of weekly responsibilities within a team. The application ensures that specific tasks are assigned to individuals on a recurring basis, and automated alerts are sent out to keep everyone informed and accountable.

#### Features
- **Automated Scheduling**: Automatically assigns weekly responsibilities to team members based on predefined rules. The first week's individual is re-assigned for the fourth week of the month.
- **Email Notifications**: Sends detailed email alerts outlining responsibilities using the Senecaglobal email system.
- **Teams and Slack Integration**: Delivers automated notifications to Microsoft Teams and Slack, ensuring that team members receive alerts through their preferred communication channels.
- **Customizable Configurations**: Easily configurable settings for email, Teams, and Slack integration, allowing seamless adaptation to your team's requirements.

#### Getting Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/SenecaScheduler.git
   cd SenecaScheduler
   ```

2. **Install Dependencies**:
   Ensure you have the necessary Python libraries installed:
   ```bash
   pip install requests
   ```

3. **Configuration**:
   Update the `config.py` file with your SMTP server details, email credentials, and webhook URLs for Teams and Slack:
   ```python
   config = {
       "email": {
           "smtp_server": "smtp.yourserver.com",
           "smtp_port": 587,
           "username": "your_email@senecaglobal.com",
           "password": "your_password"
       },
       "teams": {
           "webhook_url": "https://outlook.office.com/webhook/your_webhook_url"
       },
       "slack": {
           "webhook_url": "https://hooks.slack.com/services/your_webhook_url"
       },
       "scheduling": {
           "week_1_guy": "week1_guy@senecaglobal.com",
           "week_2_guy": "week2_guy@senecaglobal.com",
           "week_3_guy": "week3_guy@senecaglobal.com",
           "responsibilities": [
               "Acknowledge",
               "Go through the debug steps and get in a call",
               "Provide the analysis we did at offshore to onshore"
           ]
       }
   }
   ```

4. **Run the Script**:
   Execute the script to start sending notifications:
   ```bash
   python scheduler.py
   ```

#### Future Enhancements
- **Dynamic Configuration Loading**: Add support for loading configurations dynamically from external sources.
- **Enhanced Logging and Monitoring**: Implement detailed logging and monitoring for better traceability and issue resolution.
- **User Interface**: Develop a web-based interface for easier management and scheduling visualization.

#### Contributions
We welcome contributions to improve SenecaScheduler. If you have suggestions for enhancements or find bugs, please open an issue or submit a pull request.

#### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

SenecaScheduler aims to simplify the management of weekly tasks and ensure clear communication within teams. By automating the scheduling and notification process, it helps maintain accountability and improve efficiency.