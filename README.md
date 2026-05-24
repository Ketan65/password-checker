# 🔐 Password Strength Analyzer

A professional password strength analysis tool built in Python, featuring a **Bloom Filter** trained on 14 million real-world leaked passwords (RockYou dataset).

## ✨ Features

- 🔍 **Length Analysis** — Checks password length and scores it
- 🔠 **Character Variety** — Detects uppercase, lowercase, digits, and symbols
- 📊 **Entropy Calculation** — Mathematically measures password unpredictability
- 🚫 **Dictionary Attack Simulation** — Checks against 14M+ real leaked passwords using Bloom Filter
- 🖥️ **CLI Interface** — Terminal based analyzer
- 🎨 **GUI Interface** — Dark themed desktop app with show/hide password toggle

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI)
- pybloom-live (Bloom Filter)
- RockYou Dataset (14M passwords)

## 📁 Project Structure


## ⚙️ Installation

### Step 1 — Clone the repository
```bash
git clone https://github.com/Ketan65/password-checker.git
cd password-checker
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Download Bloom Filter
Download the pre-built bloom filter (trained on 14M passwords):

👉 [Download bloom_filter.pkl](https://drive.google.com/file/d/14o29HLjpKBXeRnoT0Pwux_mHsXpWeN-c/view?usp=sharing)

Place the downloaded file inside the `core/` folder:

## 🚀 Usage

### CLI
```bash
python cli.py
```

### GUI
```bash
python gui.py
```

## 📊 Rating System

| Rating | Score | Meaning |
|--------|-------|---------|
| 🔥 VERY STRONG | 11-12 | Excellent password |
| 💪 STRONG | 8-10 | Good password |
| ⚠️ FAIR | 5-7 | Needs improvement |
| ❌ WEAK | 0-4 | Change immediately |

## 👨‍💻 Author

**Ketan Verma**  
B.Tech Computer Science (Cyber Security)  
GLA University, Mathura  
GitHub: [@Ketan65](https://github.com/Ketan65)
