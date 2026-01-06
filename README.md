# orginizer_bot
Asynchronous Telegram bot for productivity: Weather &amp; Pomodoro &amp; Timer.
## Key Features
* **Weather forecast:** real-time weather forecast and recommendations.
* **Pomodoro timer:** focus timer to help you stay more productive
* **Timer:** classic minimalistic timer to help you do your chores
## Tech Stack
* Python 3.12
* Aiogram 3.24 (Telegram Bot framework)
* Requests (To get weather from wttr.in)
* Asyncio
## Installation
1. **Clone the repository:**  
``` bash
git clone <https://github.com/KG1303/orginizer_bot.git> [<directory-name>]
cd directory-name
```
2. **Set up virtual environment:**
``` bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```
3. **Install requirements:**
``` bash
pip install -r requirements.txt
```
4. **Environment variables:**  
Create a `.env` file in the root directory:
``` env
BOT_TOKEN = your_telegram_bot_token
```
5. **Run the bot:**
``` bash
python main.py
```
*P.S. Before the installation process, install Python and git from official website.*
## Licence
MIT Licence. Created for educational purposes.
