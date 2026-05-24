from pybloom_live import BloomFilter
import pickle

print("Bloom filter bana raha hoon... thoda wait karo!")

bloom = BloomFilter(capacity=14000000, error_rate=0.001)

with open("rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        password = line.strip().lower()
        bloom.add(password)

with open("bloom_filter.pkl", "wb") as f:
    pickle.dump(bloom, f)

print("Done! bloom_filter.pkl ban gayi!")