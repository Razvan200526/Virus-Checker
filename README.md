This Python script scans your system for potentially malicious files by calculating their hashes and comparing them with known malicious file hashes stored in a signatures.txt file.

Features
-Scans files on your system.
-Computes the hash of each file (MD5, SHA-1, or SHA-256).
-Compares file hashes to a list of known malicious file hashes stored in signatures.txt.
-Identifies potentially malicious files and provides an alert.


Prerequisites
Python 3.x
Required Python libraries:
-hashlib
-os

Installation:
  1) Clone the repository
    git clone https://github.com/yourusername/malicious-file-identifier.git
    cd malicious-file-identifier
  2)Ensure the signatures.txt file is in the same directory as the script, and contains the known malicious file hashes (one per line).

