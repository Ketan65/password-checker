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

```bash
# Clone the repository
git clone https://github.com/Ketan65/password-checker.git
cd password-checker

# Install dependencies
pip install pybloom-live

# Build Bloom Filter (requires rockyou.txt)
python build_bloom.py
```

## 🚀 Usage

### CLI
```bash
cd core
python
from checker import load_bloom, analyze
bloom = load_bloom()
results = analyze("YourPassword@123", bloom)
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
