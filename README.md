# 🕐 KRONOS - Network Port Scanner

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A powerful yet beginner-friendly network port scanner for penetration testing and security research.

## 👨‍💻 Author

**Hassan Ali**  
GitHub: [@FallenGodfather](https://github.com/FallenGodfather)  
MSc Cyber-Security @ Brandenburg Technical University, Germany

---

## 🎯 About KRONOS

Named after the Greek god of time, **KRONOS** is a fast and efficient port scanning tool built entirely in Python. I created this project to dive deeper into cybersecurity and understand how penetration testers identify vulnerabilities in network systems.

After learning about some of the biggest cyberattacks in history—like the **Yahoo breach (2013)** that compromised 3 billion accounts, the **Equifax hack (2017)** affecting 147 million people, and the devastating **NotPetya attack (2017)** that caused over $10 billion in global damage—I wanted to build something that demonstrates how security professionals proactively find and fix weaknesses before attackers exploit them.

### 🤔 Why Port Scanning?

Port scanning is the **first step in any penetration test**. It's how ethical hackers:

- Discover what services are running on target systems
- Identify potential entry points and vulnerabilities
- Map out the network attack surface
- Detect misconfigurations and unnecessary open ports

KRONOS helps you understand the reconnaissance phase that security researchers use to protect systems from the kinds of attacks that have shaped cybersecurity history.

---

## ✨ Features

- ⚡ **Fast scanning** with customizable port ranges
- 🔍 **Service detection** - identifies common services on open ports
- 🌐 **Hostname resolution** - works with both IPs and domain names
- 📊 **Clean output** with real-time port discovery
- ⌨️ **Interactive interface** - easy for beginners
- 🛡️ **Error handling** - won't crash on you
- 📝 **Detailed scan summaries** at the end

---

## 🚀 Installation & Usage

### Requirements

- Python 3.6 or higher
- That's it! No external libraries needed

### Quick Start

1. **Clone the repo:**
```bash
git clone https://github.com/FallenGodfather/kronos.git
cd kronos
```

2. **Run KRONOS:**
```bash
python kronos.py
```

3. **Follow the prompts:**
```
[?] Enter target IP or hostname
>>> scanme.nmap.org

[?] Enter starting port (default: 1)
>>> 1

[?] Enter ending port (default: 1000)
>>> 100
```

### Example Output

```
======================================================================

                    Kronos (Port Scanner)
                    Port Scanner v1.0
                   Created by Hassan Ali
                   github.com/FallenGodfather

======================================================================

[*] Starting scan on scanme.nmap.org
[*] Port range: 1-100
[*] Time: 23:45:12
----------------------------------------------------------------------
[+] Resolved scanme.nmap.org to 45.33.32.156

[+] Port    22 - OPEN  (SSH)
[+] Port    80 - OPEN  (HTTP)

----------------------------------------------------------------------
[*] Scan complete at 23:46:38
[*] Found 2 open port(s)
[*] Open ports: 22, 80

[*] Thanks for using Kronos!
[*] Remember: Only scan systems you have permission to test
```

---

## 🛠️ How It Works

KRONOS uses Python's `socket` library to test TCP connections:

1. **Creates a socket** for each port in the range
2. **Attempts connection** to target IP:port
3. **Checks the result** - connection successful = port is open
4. **Identifies the service** running on that port
5. **Reports findings** with a clean summary

### Code Structure

```
kronos.py
├── show_banner()         # Displays the ASCII art banner
├── check_port()          # Tests if a specific port is open
├── get_service_name()    # Identifies common services
├── scan_target()         # Main scanning logic
└── main()                # User interaction & input handling
```

---

## 📚 What I Learned

Building KRONOS taught me:

- **Network fundamentals** - TCP/IP, ports, sockets
- **Socket programming** in Python
- **Penetration testing methodology** - the reconnaissance phase
- **Error handling** for real-world scenarios
- **User experience** - making technical tools approachable
- **Ethical hacking principles** and responsible disclosure

---

## ⚠️ Legal Warning

**READ THIS CAREFULLY:**

This tool is for **EDUCATIONAL AND AUTHORIZED TESTING ONLY**.

✅ **DO:**
- Scan your own systems (127.0.0.1)
- Use authorized testing environments (scanme.nmap.org)
- Get written permission before scanning ANY network
- Practice on CTF platforms and labs (TryHackMe, HackTheBox)

❌ **DO NOT:**
- Scan systems without explicit authorization
- Attack corporate networks, government sites, or banks
- Use this for illegal activities
- Assume anything is "okay to scan" without permission

**Unauthorized port scanning is illegal in most countries.** I built this to learn cybersecurity, not to break laws. Always practice ethical hacking: **Permission + Purpose + Professionalism**.

---

## 🎓 Learning Path

### If You're New to Cybersecurity

**Start Here:**
1. Learn TCP/IP networking basics
2. Understand how ports and services work
3. Study the OWASP Top 10 vulnerabilities
4. Practice on TryHackMe (free beginner rooms)

**Next Steps:**
- Learn about other scanning techniques (UDP, stealth scans)
- Study Nmap and its advanced features
- Explore web application security testing
- Build more security tools in Python

**Advanced:**
- Get certified (CompTIA Security+, CEH, OSCP)
- Learn malware analysis and reverse engineering
- Contribute to open-source security projects
- Participate in bug bounty programs

---

## 🔮 Future Ideas

Things I might add later:

- [ ] Multi-threaded scanning (make it faster!)
- [ ] Banner grabbing for service version detection
- [ ] Export results to JSON/CSV
- [ ] UDP port scanning support
- [ ] Stealth scanning techniques
- [ ] Integration with CVE databases
- [ ] Maybe a GUI? (probably not though)

Feel free to contribute if you want to add these features!

---

## 🤝 Contributing

Found a bug? Want to add a feature? Here's how:

1. Fork this repository
2. Create a new branch (`git checkout -b cool-feature`)
3. Make your changes
4. Test everything
5. Commit (`git commit -m 'Added cool feature'`)
6. Push (`git push origin cool-feature`)
7. Open a Pull Request

All contributions welcome! Just keep it ethical and legal.

---

## 📖 Historical Context

Some major attacks that inspired KRONOS:

| Year | Attack | Impact |
|------|--------|--------|
| 2013 | Yahoo | 3 billion accounts compromised |
| 2017 | Equifax | 147 million people affected |
| 2017 | NotPetya | $10 billion in global damage |
| 2017 | WannaCry | 300,000+ systems in 150 countries |
| 2020 | SolarWinds | Multiple gov agencies compromised |
| 2021 | Colonial Pipeline | Critical US infrastructure shutdown |

**These attacks remind us why security matters.** Tools like KRONOS help find vulnerabilities before the bad guys do.

---

## 📜 License

MIT License - see LICENSE file for details

---

## 🙏 Acknowledgments

- Thanks to the Nmap project for inspiration
- Shoutout to the cybersecurity community
- Appreciation to all the educators making security accessible
- Motivated by history's biggest hacks and the need for better security

---

## 📧 Contact

**Hassan Ali**  
🎓 MSc AI Student @ BTU Cottbus, Germany  
💼 Aspiring Cybersecurity Professional  

GitHub: [@FallenGodfather](https://github.com/FallenGodfather)

Feel free to reach out if you have questions or just want to talk about cybersecurity!

---

## 🎯 Practice Targets

Safe places to test KRONOS:

- **Your local machine**: `127.0.0.1`
- **Nmap's test server**: `scanme.nmap.org` (explicitly allows scanning)
- **Your own devices**: routers, servers you personally own
- **CTF platforms**: TryHackMe, HackTheBox labs

---

**⭐ If you learned something from this project, give it a star! ⭐**

*Stay curious. Stay ethical. Stay legal.* 🔐

---

### Why "Kronos"?

Named after the Greek Titan of time, because good reconnaissance takes time and patience. Kronos was powerful but needed to be used wisely—just like port scanning tools.

---

*Last updated: October 2025*
