import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "core"))

from checker import load_bloom, analyze

def main():
    print("=" * 40)
    print("    PASSWORD STRENGTH ANALYZER")
    print("=" * 40)
    
    password = input("\nEnter password: ")
    
    if len(password) == 0:
        print("Error: Password khali nahi hona chahiye!")
        return
    
    print("\nAnalyzing...")
    bloom = load_bloom()
    results = analyze(password, bloom)

    print("\n" + "=" * 40)
    print("           RESULTS")
    print("=" * 40)
    print(f"Length        : {results['length']} characters")
    print(f"Variety Score : {results['variety_score']}/4")
    print(f"Entropy       : {results['entropy']} bits")
    print(f"Common Pass   : {'YES ⚠️' if results['is_common'] else 'NO ✅'}")
    print("-" * 40)
    
    if results['rating'] == "WEAK":
        print(f"Rating        : WEAK ❌")
    elif results['rating'] == "FAIR":
        print(f"Rating        : FAIR ⚠️")
    elif results['rating'] == "STRONG":
        print(f"Rating        : STRONG 💪")
    else:
        print(f"Rating        : VERY STRONG 🔥")
    
    print("=" * 40)

if __name__ == "__main__":
    main()