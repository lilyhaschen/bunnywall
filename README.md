# 🐰 BunnyWall: Behavioral Firewall 🛡️

A terminal-based behavioral firewall written in Python by Lily (｡•̀ᴗ-)✧, your friendly cybersecurity chaos bunny. BunnyWall scans user input for dangerous patterns, logs threats with adorable sass, and greets you with an ASCII rabbit who’s tired of your shady SQL injections.

## 💡 Features

* Scans for common security threats like SQL injection, dangerous functions, and command injection
* Pattern-based rule engine using regular expressions
* Logs detections with host info and timestamps
* Bunny-themed alerts with ASCII charm
* Command-line arguments for scanning, logging, and dry runs
* Single-file Python script — cute, deadly, and portable

## 🧪 Usage

```bash
# Scan input
python main_bunny_firewall.py --input "DROP TABLE users;"

# View logged threats
python main_bunny_firewall.py --show-log

# Run a test scan without saving logs
python main_bunny_firewall.py --input "eval()" --dry
```

## 🐇 Example Output

```
 (\(\
 ( -.-)
 o_(")(")  BunnyWall Initialized - Cutest Defense Protocol Online

(｡♥‿♥｡) Scanning your input through BunnyWall...
(╯°□°）╯︵ ┻━┻ Action: BLOCK | Reason: SQL Injection attempt | Pattern: DROP TABLE|DELETE FROM|--
🐇✨ BunnyWall caught 1 naughty input(s)! Logged to bunnywall_log.json
```

## ⚙️ Rules

The rule set lives in `bunnywall_rules.json`. If the file is missing, BunnyWall uses default in-memory rules like:

```json
{
  "pattern": "DROP TABLE|DELETE FROM|--",
  "action": "BLOCK",
  "reason": "SQL Injection attempt"
}
```

You can extend it with more regexes or modify the logic in `DEFAULT_RULES`.

## 📚 Use Cases

* Lightweight CLI WAF (Web Application Firewall) testing
* DevOps log analysis and rule experimentation
* Cybersecurity projects with style and sparkle

## 🐾 From the Creator

Built by **Lily**, a cybersecurity enthusiast who believes code should be secure *and* sassy. Powered by kaomojis, espresso, and righteous bunny fury.

---

*“Some bunnies wear armor. Mine has regex.” — Lily*
