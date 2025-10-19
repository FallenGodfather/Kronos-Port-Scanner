# 🚀 KRONOS Quick Start Guide

**Created by Hassan Ali (@FallenGodfather)**

---

## What is KRONOS?

KRONOS is a Python port scanner I built to learn about network security and penetration testing. It's named after the Greek Titan of time—because good reconnaissance takes time and patience.

This guide will help you get started, whether you're completely new to cybersecurity or just want to see what the tool can do.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Your First Scan](#your-first-scan)
3. [Understanding the Results](#understanding-the-results)
4. [Common Ports Cheat Sheet](#common-ports-cheat-sheet)
5. [Safe Testing Targets](#safe-testing-targets)
6. [Troubleshooting](#troubleshooting)
7. [Next Steps](#next-steps)

---

## Getting Started

### Step 1: Install Python

You need Python 3.6 or newer. Check if you have it:

```bash
python --version
```

or

```bash
python3 --version
```

If you don't have Python, download it from [python.org](https://python.org).

### Step 2: Get KRONOS

Clone the repository:

```bash
git clone https://github.com/FallenGodfather/kronos.git
cd kronos
```

### Step 3: Run It!

```bash
python kronos.py
```

That's it! No pip install, no dependencies, nothing complicated.

---

## Your First Scan

When you run KRONOS, you'll see the banner and some prompts. Here's what to do:

### Scanning Your Own Computer (Safest Option)

```
[?] Enter target IP or hostname
>>> 127.0.0.1

[?] Enter starting port (default: 1)
>>> 1

[?] Enter ending port (default: 1000)
>>> 100
```

This scans ports 1-100 on your local machine. Safe and legal!

### Scanning the Nmap Test Server

```
[?] Enter target IP or hostname
>>> scanme.nmap.org

[?] Enter starting port (default: 1)
>>> 1

[?] Enter ending port (default: 1000)
>>> 1000
```

This server is specifically provided for people to practice port scanning.

---

## Understanding the Results

### Reading the Output

Here's what you'll see:

```
[*] Starting scan on 127.0.0.1
[*] Port range: 1-100
[*] Time: 23:45:30
----------------------------------------------------------------------
[+] Port    22 - OPEN  (SSH)
[+] Port    80 - OPEN  (HTTP)
[+] Port   443 - OPEN  (HTTPS)
----------------------------------------------------------------------
[*] Scan complete at 23:46:15
[*] Found 3 open port(s)
[*] Open ports: 22, 80, 443
```

### What Does This Mean?

- **[*]** = Information messages
- **[+]** = Found an open port!
- **[!]** = Warning or error
- **[?]** = Question/prompt for you

If you see `Port 22 - OPEN (SSH)`, it means:
- Port 22 is accessible
- SSH (Secure Shell) service is likely running there
- This is a potential entry point to the system

**No output for a port = it's closed or filtered**

---

## Common Ports Cheat Sheet

Here are ports you'll commonly find open:

| Port | Service | What It Does | Should It Be Open? |
|------|---------|--------------|-------------------|
| 20-21 | FTP | File transfers (unencrypted) | ⚠️ Only if needed |
| 22 | SSH | Remote terminal access | ✅ Common on servers |
| 23 | Telnet | Remote access (INSECURE!) | ❌ Should be disabled |
| 25 | SMTP | Email sending | ⚠️ Only on mail servers |
| 53 | DNS | Domain name lookups | ✅ On DNS servers |
| 80 | HTTP | Web traffic (unencrypted) | ⚠️ Prefer HTTPS (443) |
| 110 | POP3 | Email retrieval | ⚠️ Only on mail servers |
| 143 | IMAP | Email access | ⚠️ Only on mail servers |
| 443 | HTTPS | Secure web traffic | ✅ Good! Encrypted |
| 445 | SMB | Windows file sharing | ⚠️ High risk if exposed |
| 3306 | MySQL | Database server | ❌ Should be firewalled |
| 3389 | RDP | Windows remote desktop | ⚠️ Common attack target |
| 5432 | PostgreSQL | Database server | ❌ Should be firewalled |
| 5900 | VNC | Remote desktop | ⚠️ Often insecure |
| 8080 | HTTP-Alt | Alternative web port | ⚠️ Check what's running |

### Quick Risk Assessment

- ✅ **Green**: Generally okay if properly configured
- ⚠️ **Yellow**: Could be risky, should be secured
- ❌ **Red**: High risk, should probably be closed

---

## Safe Testing Targets

### Where You CAN Scan

1. **Your own computer**
   - `127.0.0.1` or `localhost`
   - 100% safe and legal

2. **scanme.nmap.org**
   - Specifically allows port scanning
   - Great for practice
   - Maintained by the Nmap project

3. **Your own devices**
   - Your router (usually 192.168.1.1)
   - Your own servers
   - Virtual machines you created

4. **CTF platforms**
   - TryHackMe challenges
   - HackTheBox machines
   - CTFtime events

### Where You CANNOT Scan

❌ **NEVER SCAN:**
- Your school/university network (without permission)
- Your employer's network (unless it's your job)
- Google, Facebook, Amazon, etc.
- Banks or financial institutions
- Government websites
- Literally ANY system you don't own or have written permission to test

**Getting caught = possible criminal charges, fines, or jail time**

Not joking. People have gone to prison for unauthorized scanning.

---

## Troubleshooting

### Problem: "Could not resolve hostname"

**Why:** The hostname doesn't exist or you're offline

**Fix:**
- Check your internet connection
- Try pinging the host first: `ping scanme.nmap.org`
- Use an IP address instead of a hostname

### Problem: Scan is super slow

**Why:** Scanning takes about 1 second per port

**Fix:**
- Scan fewer ports (e.g., 1-100 instead of 1-65535)
- This is normal! Port scanning isn't instant
- Scanning all 65535 ports takes ~18 hours

### Problem: No open ports found

**Possible reasons:**
- Firewall is blocking the connection
- No services are actually running
- You're scanning the wrong IP
- Your own firewall is blocking outbound connections

**Try:**
- Scan 127.0.0.1 first to verify the tool works
- Disable your firewall temporarily (carefully!)
- Try a different target like scanme.nmap.org

### Problem: Permission denied / Access error

**On Windows:**
- Run Command Prompt or PowerShell as Administrator
- Right-click → "Run as administrator"

**On Linux/Mac:**
- Some ports require root: `sudo python kronos.py`
- Or just scan ports above 1024 (don't need root)

---

## Next Steps

### Beginner Level

**You're ready when you can:**
- ✅ Successfully scan localhost
- ✅ Scan scanme.nmap.org
- ✅ Identify what common services are
- ✅ Explain why port 22 might be open

**Learn next:**
- TCP vs UDP protocols
- The three-way handshake
- How firewalls work
- Basic Linux commands

### Intermediate Level

**Try these challenges:**
- Modify the code to scan specific ports only
- Add a progress bar
- Make it save results to a file
- Add more service names to the dictionary
- Learn about threading to speed up scans

**Study:**
- Nmap and its advanced features
- Network protocols (TCP/IP stack)
- Wireshark for packet analysis
- Basic Python scripting

### Advanced Level

**Build on KRONOS:**
- Add multi-threading for parallel scanning
- Implement banner grabbing (grab service versions)
- Create UDP port scanning
- Build a vulnerability scanner
- Add OS fingerprinting

**Explore:**
- Metasploit Framework
- Burp Suite for web app testing
- Assembly and reverse engineering
- Malware analysis

---

## Learning Resources

### Free Platforms

1. **TryHackMe** (tryhackme.com)
   - Best for beginners
   - Guided learning paths
   - In-browser hacking labs

2. **HackTheBox** (hackthebox.com)
   - More challenging
   - Realistic scenarios
   - Great community

3. **OverTheWire** (overthewire.org)
   - Command line practice
   - Perfect for Linux skills
   - Progressive difficulty

### Books I'm Reading

- "Black Hat Python" by Justin Seitz
- "The Web Application Hacker's Handbook"
- "Hacking: The Art of Exploitation"

### YouTube Channels

- NetworkChuck
- John Hammond
- IppSec (HackTheBox walkthroughs)
- LiveOverflow

### Certifications

- **CompTIA Security+** (beginner)
- **CEH** - Certified Ethical Hacker (intermediate)
- **OSCP** - Offensive Security Certified Professional (advanced)

---

## Tips & Tricks

### Speed Up Your Scans

Scan common ports first:
```
Start port: 1
End port: 1000
```

Most services run on well-known ports (1-1024).

### Finding Your Router's IP

**Windows:**
```bash
ipconfig
```
Look for "Default Gateway"

**Linux/Mac:**
```bash
ip route | grep default
```
or
```bash
netstat -nr | grep default
```

### Keyboard Shortcuts

- **Ctrl+C**: Stop the scan
- **Ctrl+Z**: Pause (Linux/Mac)
- **Ctrl+D**: Exit Python interpreter

---

## Ethics & Professionalism

### The Hacker Mindset

Good hackers follow these principles:

1. **Get permission first** - Always
2. **Document everything** - Keep notes
3. **Report responsibly** - Disclose vulnerabilities properly
4. **Never cause harm** - Don't delete or modify data
5. **Respect privacy** - Don't access personal information
6. **Keep learning** - Technology changes fast

### Responsible Disclosure

If you find a vulnerability:

1. Don't exploit it (just document it)
2. Contact the organization privately
3. Give them time to fix it (30-90 days)
4. Don't publicly disclose until it's patched
5. Never demand payment (that's extortion)

---

## Fun Facts About Kronos

### Why I Named It That

In Greek mythology, Kronos (Cronus) was the Titan god of time. I chose this name because:

- Good reconnaissance takes time and patience
- You can't rush a thorough security assessment
- Kronos was powerful but needed to be used wisely
- It just sounds cool, honestly

### Development Stats

- Lines of code: ~170
- Time spent on ASCII art: way too long
- Coffee consumed: several cups
- Fun level: 10/10

---

## Support & Community

### Need Help?

- Open an issue on GitHub
- Check the README.md for more details
- Join r/cybersecurity on Reddit
- Ask on Stack Overflow

### Want to Contribute?

- Fork the repo
- Add cool features
- Fix bugs you find
- Submit a pull request

All skill levels welcome!

---

## Final Words

Remember:

- **Start small** - scan localhost first
- **Practice legally** - use authorized targets
- **Learn continuously** - cybersecurity evolves daily
- **Stay ethical** - use your powers for good
- **Have fun** - hacking should be enjoyable!

**Questions?** Feel free to reach out!

**Hassan Ali**  
GitHub: [@FallenGodfather](https://github.com/FallenGodfather)

---

**Happy scanning! 🔐**

*"With great power comes great responsibility."*

---

*Last updated: October 2025*