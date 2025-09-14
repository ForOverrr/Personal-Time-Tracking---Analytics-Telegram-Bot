# Personal Time-Tracking & Analytics Telegram Bot

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)

A personal Telegram bot designed to help you track your time effortlessly and analyze how you spend it. Log activities with simple commands and receive text summaries and visual charts of your productivity.



---

## Features ✨

- **Simple Time Tracking**: Start and stop tracking any activity with the `/begin` and `/stop` commands.
- **Persistent Storage**: All your activity data is saved in a local SQLite database.
- **Data Analysis**: Get summaries of your time usage for the current day or week.
- **Visual Reports**: Receive pie charts visualizing your time distribution for a clear overview.
- **Secure**: Your API token is kept safe and separate from the code using environment variables.

---

## Technologies Used 🛠️

- **Backend**: Python
- **Telegram API Wrapper**: [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot)
- **Database**: SQLite
- **Data Analysis**: Pandas
- **Data Visualization**: Matplotlib
- **Environment Variables**: `python-dotenv`

---

## Setup and Installation 🚀

### 1. Prerequisites

- Python 3.8 or newer
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)

### 2. Clone the Repository

```bash
git clone https://github.com/ForOverrr/Personal-Time-Tracking---Analytics-Telegram-Bot.git
cd Personal-Time-Tracking---Analytics-Telegram-Bot
```

### 3. Create and Activate the Virtual Environment

```bash
python -m venv venv

# Activate on Mac/Linux
source venv/bin/activate

# Activate on Windows
.\venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a file named `.env` in the root of your project folder and add your Telegram API token:

```env
TELEGRAM_TOKEN="YOUR_REAL_API_TOKEN_HERE"
```

### 6. Run the Bot

```bash
python bot.py
```

---

## Usage

Interact with your bot in Telegram using the following commands:

- `/begin <activity>` — Start tracking a new activity (e.g. `/begin Reading`)
- `/stop` — Stop tracking the current activity
- `/summary` — Get a summary of your time usage for today or the current week
- `/chart` — Receive a pie chart showing your time distribution

---

## Contributing

Contributions are welcome! Feel free to fork the repository and open a pull request with your improvements.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
