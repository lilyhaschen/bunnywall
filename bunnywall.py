# 🐰 BunnyWall: Behavioral Firewall 🛡️
# Created by Lily (｡•̀ᴗ-)✧ The Cybersecurity Chaos Bunny

import re
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
import socket
import platform

LOG_FILE = Path("bunnywall_log.json")
RULES_FILE = Path("bunnywall_rules.json")

DEFAULT_RULES = [
    {"pattern": r"DROP TABLE|DELETE FROM|--", "action": "BLOCK", "reason": "SQL Injection attempt"},
    {"pattern": r"wget|curl|base64", "action": "ALERT", "reason": "Suspicious command usage"},
    {"pattern": r"/etc/passwd|/shadow", "action": "BLOCK", "reason": "System file access attempt"},
    {"pattern": r"eval\(|exec\(", "action": "BLOCK", "reason": "Dangerous function call"},
    {"pattern": r"import os|import subprocess", "action": "ALERT", "reason": "Potential command injection"},
    {"pattern": r"union select", "action": "BLOCK", "reason": "SQL Injection vector"}
]

# (=^-ω-^=)ﾉﾞ Load rules

def load_rules():
    if RULES_FILE.exists():
        with open(RULES_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_RULES

# (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Scan for evil

def scan_input(input_text, rules):
    detections = []
    timestamp = datetime.utcnow().isoformat()
    for rule in rules:
        if re.search(rule["pattern"], input_text, re.IGNORECASE):
            detections.append({
                "action": rule["action"],
                "reason": rule["reason"],
                "pattern": rule["pattern"],
                "timestamp": timestamp,
                "input": input_text,
                "host": socket.gethostname(),
                "platform": platform.system()
            })
    return detections

# (*≧ω≦) Log like a pro bun

def log_detection(events):
    if not events:
        return
    existing = []
    if LOG_FILE.exists():
        with open(LOG_FILE, 'r') as f:
            existing = json.load(f)
    existing.extend(events)
    with open(LOG_FILE, 'w') as f:
        json.dump(existing, f, indent=2)
    print(f"🐇✨ BunnyWall caught {len(events)} naughty input(s)! Logged to {LOG_FILE}")

# (๑˃̵ᴗ˂̵) Show log history

def show_log():
    if LOG_FILE.exists():
        with open(LOG_FILE, 'r') as f:
            data = json.load(f)
        for entry in data:
            print(json.dumps(entry, indent=2))
    else:
        print("(・_・;) No logs found. Bunny sleeping.")

# Bunny ASCII intro
ASCII_BUNNY = r"""
 (\(\
 ( -.-)
 o_(")(")  BunnyWall Initialized - Cutest Defense Protocol Online
"""

# (｡･ω･｡)ﾉ♡ Main function

def main():
    parser = argparse.ArgumentParser(description="BunnyWall Behavioral Firewall")
    parser.add_argument("--input", type=str, help="User input to scan")
    parser.add_argument("--show-log", action="store_true", help="Display past alerts")
    parser.add_argument("--dry", action="store_true", help="Run in dry mode (no logging)")
    args = parser.parse_args()

    print(ASCII_BUNNY)

    if args.show_log:
        show_log()
        return

    if not args.input:
        print("(╯°□°）╯︵ ┻━┻ Please provide input with --input")
        return

    print("(｡♥‿♥｡) Scanning your input through BunnyWall...")
    rules = load_rules()
    findings = scan_input(args.input, rules)
    if findings:
        if not args.dry:
            log_detection(findings)
        for f in findings:
            print(f"(╯°□°）╯︵ ┻━┻ Action: {f['action']} | Reason: {f['reason']} | Pattern: {f['pattern']}")
    else:
        print("(＾◡＾)っ✂ All clear, bunfriend! No suspicious patterns found.")


if __name__ == "__main__":
    main()
