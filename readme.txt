# Personal Time-Tracking & Analytics Telegram Bot

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)

A personal Telegram bot designed to help you track your time effortlessly and analyze how you spend it. Log activities with simple commands and receive text summaries and visual charts of your productivity.

!(https://i.imgur.com/example.png) ## Features ✨

- **Simple Time Tracking**: Start and stop tracking any activity with the `/begin` and `/stop` commands.
- **Persistent Storage**: All your activity data is saved in a local SQLite database.
- **Data Analysis**: Get summaries of your time usage for the current day or week.
- **Visual Reports**: Receive a pie chart visualizing your time distribution for a clear overview.
- **Secure**: Your API token is kept safe and separate from the code using environment variables.

---

## Technologies Used 🛠️

- **Backend**: Python
- **Telegram API Wrapper**: `python-telegram-bot`
- **Database**: SQLite
- **Data Analysis**: Pandas
- **Data Visualization**: Matplotlib
- **Environment Variables**: `python-dotenv`

---

## Setup and Installation 🚀

Follow these steps to get your own instance of the bot running.

### 1. Prerequisites

- Python 3.8 or newer
- A Telegram Bot Token from **@BotFather**

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name


# Create the environment
python -m venv venv

# Activate it (on Mac/Linux)
source venv/bin/activate

# Activate it (on Windows)
.\venv\Scripts\activate


pip install -r requirements.txt


5. Configure Environment Variables

Create a file named .env in the root of your project folder and add your Telegram API token.

.env:

TELEGRAM_TOKEN="YOUR_REAL_API_TOKEN_HERE"
6. Run the Bot

Start the bot with the following command:

Bash
python bot.py
