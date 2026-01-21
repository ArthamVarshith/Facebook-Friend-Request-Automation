# Facebook Friend Request Automation (People Search)

A Python-based automation script that uses **Selenium with a logged-in Brave browser profile** to automatically send Facebook friend requests from **People Search results**, while simulating human-like behavior.

---

## 📌 Project Purpose

This project automates the **manual Facebook friend request process** in a controlled and realistic manner by:

- Using a real Brave browser instance
- Reusing an already authenticated Facebook user profile
- Adding random delays to mimic human actions
- Avoiding Facebook APIs or private scraping endpoints

---

## 🎯 Use Cases

- Networking and community building  
- Audience growth for creators and founders  
- Market research outreach  
- Controlled social automation experiments  
- Personal productivity automation  

---

## 🛠 Tech Stack

| Component   | Technology |
|------------|------------|
| Language   | Python |
| Automation | Selenium |
| Browser    | Brave |
| Driver     | ChromeDriver |
| Driver Mgmt| webdriver-manager |

---

## 📂 Project Structure

.
├── facebook_friend_bot.py
├── requirements.txt
├── README.md
├── docs/
└── examples/

---

## ⚙️ How It Works

1. Launches **Brave browser** with an existing logged-in Facebook profile  
2. Opens Facebook **People Search** using a keyword  
3. Automatically scrolls through search results  
4. Detects **“Add Friend”** buttons using multiple selectors  
5. Sends friend requests with random human-like delays  
6. Stops once the end of the page is reached  

---

## 🔍 Automation Flow

User Input (Keyword)
↓
Open Facebook People Search
↓
Scroll Page
↓
Find "Add Friend" Buttons
↓
Send Friend Requests
↓
Repeat Until End of Results

## 👨‍💻 Author
Artham Varshith 
Software Engineer
