from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    return {
        "score": result['score'],
        "feedback": result['feedback'],
        "crack_times_display": result['crack_times_display']
    }

import argparse
from analyzer import analyze_password
from wordlist_generator import generate_wordlist
from utils import export_wordlist

parser = argparse.ArgumentParser(description="Password Strength Analyzer and Wordlist Generator")
parser.add_argument('--password', help='Password to analyze')
parser.add_argument('--inputs', nargs='+', help='Personal info (name, pet, etc.)')
parser.add_argument('--output', default='output/wordlist.txt', help='Output file')

args = parser.parse_args()

if args.password:
    print("\n[+] Password Analysis:")
    analysis = analyze_password(args.password)
    for k, v in analysis.items():
        print(f"{k}: {v}")

if args.inputs:
    print("\n[+] Generating custom wordlist...")
    words = generate_wordlist(args.inputs)
    export_wordlist(words, args.output)
