import os
import math
import pickle
def check_length(password):
    length = len(password)
    return length
def length_score(password):
    length = len(password)
    
    if length < 8:
        return 0        # bahut chota
    elif length < 12:
        return 1        # theek hai
    elif length < 16:
        return 2        # acha hai
    else:
        return 3        # bahut acha
def check_variety(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    score = 0
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1
    
    return score


def check_entropy(password):
    pool = 0
    
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        pool += 32
    
    if pool == 0:
        return 0
    
    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)
    
def load_bloom():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    bloom_path = os.path.join(base_dir, "bloom_filter.pkl")
    with open(bloom_path, "rb") as f:
        bloom = pickle.load(f)
    return bloom

def check_dictionary(password, bloom):
    password_lower = password.strip().lower()
    if password_lower in bloom:
        return True   # common password hai - WEAK!
    else:
        return False  # rare password hai - GOOD!
    
def analyze(password, bloom):
    results = {}
    
    # length check
    results["length"] = len(password)
    results["length_score"] = length_score(password)
    
    # variety check
    results["variety_score"] = check_variety(password)
    
    # entropy check
    results["entropy"] = check_entropy(password)
    if results["entropy"] < 28:
        results["entropy_score"] = 0
    elif results["entropy"] < 36:
        results["entropy_score"] = 1
    elif results["entropy"] < 60:
        results["entropy_score"] = 2
    else:
        results["entropy_score"] = 3
    
    # dictionary check
    results["is_common"] = check_dictionary(password, bloom)
    if results["is_common"]:
        results["dictionary_score"] = 0
    else:
        results["dictionary_score"] = 2
    
    # total score
    total = (results["length_score"] + 
             results["variety_score"] + 
             results["entropy_score"] + 
             results["dictionary_score"])
    
    results["total_score"] = total
    
    # final rating
    if results["is_common"]:
        results["rating"] = "WEAK"
    elif total <= 4:
        results["rating"] = "WEAK"
    elif total <= 7:
        results["rating"] = "FAIR"
    elif total <= 10:
        results["rating"] = "STRONG"
    else:
        results["rating"] = "VERY STRONG"
    
    return results