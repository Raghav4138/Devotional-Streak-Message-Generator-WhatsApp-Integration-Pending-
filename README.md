# 📿 Devotional Streak Message Generator (WhatsApp Integration Pending)

This project generates **personalized devotional messages** for clients of *Parambhog Arjee Seva*.  
Messages are tailored based on how many days (streak) their Arjee has been going on.  

⚠️ **Note:** WhatsApp API integration is **pending**. Currently, the script only generates customized messages and displays them in the console.  

---

## ✨ Features

- Reads client details from a simple CSV file (`sample_data.csv`).
- Calculates streak duration (difference between today's date and starting date).
- Chooses a **custom message template** based on streak milestones (e.g. 7 days, 21 days, 50 days, 100 days).
- Generates devotional messages in Hindi with streak-specific blessings.
- Designed to integrate easily with WhatsApp API in the future.

---

## 📂 Project Structure
arjee-message-generator/
├── sample_data.csv # Example input data
├── message_generator.py # Main script
├── README.md # Project documentation
└── requirements.txt # Dependencies

---
## 📊 Sample Input (`sample_data.csv`)

```csv
name,date,phone
Ramesh,2025-08-10,+919876543210
Suresh,2025-07-30,+919812345678
Priya,2025-07-08,+919811112222
Anita,2025-06-23,+919833344455
Arjun,2025-06-09,+919844455566
```
- name → Client’s name
- date → Starting date of Arjee (YYYY-MM-DD)
- phone → Contact number (planned for WhatsApp integration)

🖥️ Usage

Clone this repository

``` bash
git clone https://github.com/your-username/arjee-message-generator.git
cd arjee-message-generator
```

Install dependencies (if you use pandas)

``` bash
pip install -r requirements.txt
```

Run the script
``` bash
python message_generator.py
```

Check console output — you’ll see customized messages generated for each client.

## 📩 Example Output
जय श्री श्याम 🙏
प्रिय Ramesh,
आपकी अरजी पिछले 14 दिनों से बाबा के दरबार में लग रही है।
हम प्रार्थना करते हैं कि बाबा शीघ्र ही आपकी पुकार सुनें और आपको आशीर्वाद प्रदान करें।
जय श्री श्याम।

## 🚀 Roadmap

✅ Core message generator (completed)
⏳ WhatsApp API integration (pending)
⏳ Option to export messages to CSV/Excel
⏳ Web-based UI for non-technical users

