"""
Tool used to learn new tokens
"""

from tokenlearner import learnFromText
from tokenizer import TokenHolder, Token, readTokenFile, writeTokenFile

import os

def main():
    fileName = input("Text File: ")
    tokenFile = input("Token File:")

    holder = TokenHolder()
    
    if os.path.exists(tokenFile):
        print("[INFO] Reading existing tokens...")
        readTokenFile(tokenFile, holder)
        print(f"[INFO] Loaded {str(len(holder.tokens))} pre-existing tokens!")
    
    learnFromText(holder, fileName)

    print(f"[INFO] Expanded token data to contain {str(len(holder.tokens))} tokens!")
    print("[INFO] Saving token data...")

    writeTokenFile(tokenFile, holder)

main()