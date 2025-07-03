# 🏦 Tkinter-Based Online Banking System

A fully functional **desktop GUI Banking Application** developed using Python's **Tkinter** library. It allows users to register, log in, check their balance, deposit and withdraw money, and view transaction history. All data is securely stored in local JSON files.

---

## 🚀 Features

- ✅ User Registration with validation
- 🔐 Secure Login system
- 💵 Deposit and Withdraw funds
- 📊 Real-time Balance display
- 📜 Transaction history tracking
- 💾 Data stored in JSON format
- 🖥️ Fullscreen interface with `Esc` to exit

---

## 🗂️ Project Structure

📦 banking-app/
├── account.py # User dashboard logic
├── auth.py # Login and registration logic
├── main.py # Entry point to start the app
├── utils.py # JSON file handling (load/save users)
├── users.json # Stores all user account info
├── transactions/ # Stores transaction history per user
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📦 Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

---

## ▶️ How to Run the App

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name##
▶️ How to Launch the App

```bash
python main.py
🎮 Controls
Press Esc key to exit fullscreen mode.

🧠 How It Works
main.py – Starts the login interface.

auth.py – Manages user login and registration forms.

account.py – Launches after login, offering Deposit, Withdraw, Balance, History, and Logout options.

utils.py – Contains reusable functions to load and save data to users.json.

📁 Data Handling
All user information is stored in users.json.

Each user's transaction history is saved in:

php-template
Copy
Edit
transactions/<username>_transactions.json
🧾 Sample users.json Entry
json
Copy
Edit
{
  "jane_doe": {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "password": "mypassword123",
    "mobile": "9876543210",
    "balance": 1200
  }
}
