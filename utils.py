def export_wordlist(words, filename="output/wordlist.txt"):
    with open(filename, "w") as f:
        for word in words:
            f.write(word + "\n")
    print(f"[+] Wordlist exported to {filename}")
