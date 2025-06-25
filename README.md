# 🧪 File Integrity Checker (Made with Python!)

Hey there! 👋  
So this is a little project I made to **check if a file has been changed or messed with** — like, if someone edits it or it gets corrupted, this will let you know ⚠️

## 💡 Why I Made This

I was learning about **hashing** and how it's used to check file integrity, and I thought — why not make a simple tool to test it myself? This was fun and I got to understand how **tampering detection** actually works behind the scenes. 😄

## 🔍 What It Does

- You choose a file (like `notes.txt`)
- It calculates a special digital fingerprint of the file (called a SHA-256 hash 🧬)
- It saves that fingerprint in a `.hash` file
- Next time you run it, it compares the file again to see if it was changed

If the fingerprint matches: all good ✅  
If it doesn’t match: something’s different! ⚠️

## 🛠️ How to Use It

```bash
python integrity_checker.py
