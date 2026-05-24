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

```
password-checker/
├── core/
│   ├── __init__.py
│   ├── checker.py        # Core logic
│   └── bloom_filter.pkl  # Download separately (see below)
├── cli.py                # CLI interface
├── gui.py                # GUI interface
├── build_bloom.py        # Bloom filter builder
├── wordlist.txt          # Common passwords list
├── requirements.txt      # Dependencies
└── README.md
```

## ⚙️ Installation

### 🪟 Windows

#### Step 1 — Clone the repository
```bash
git clone https://github.com/Ketan65/password-checker.git
cd password-checker
```

#### Step 2 — Install dependencies
```bash
python -m pip install -r requirements.txt
```

#### Step 3 — Download Bloom Filter
👉 [Download bloom_filter.pkl](https://drive.google.com/file/d/14o29HLjpKBXeRnoT0Pwux_mHsXpWeN-c/view?usp=sharing)

Place the downloaded file inside the `core/` folder:
```
password-checker/
    └── core/
          └── bloom_filter.pkl  ← place here
```

#### Step 4 — Run the app
```bash
# GUI
python gui.py

# CLI
python cli.py
```

---

### 🐧 Kali Linux / Ubuntu

#### Step 1 — Clone the repository
```bash
git clone https://github.com/Ketan65/password-checker.git
cd password-checker
```

#### Step 2 — Install dependencies
```bash
# Virtual environment banao
python3 -m venv venv
source venv/bin/activate

# Dependencies install karo
pip install -r requirements.txt

# Tkinter (if not installed)
sudo apt install python3-tk -y
```

#### Step 3 — Download Bloom Filter
```bash
# Browser se download karo:
# https://drive.google.com/file/d/14o29HLjpKBXeRnoT0Pwux_mHsXpWeN-c/view?usp=sharing

# Phir move karo:
mv ~/Downloads/bloom_filter.pkl core/
```

#### Step 4 — Run the app
```bash
# GUI
python3 gui.py

# CLI
python3 cli.py
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
