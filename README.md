# ⚔️ Ragnarok – Lightweight Network Scanner

Ragnarok is a simple Python tool designed to perform a **ping sweep** (using `-sn`) across a given subnet. Built for speed and simplicity, it's ideal for identifying live hosts within a network without triggering noisy scans.

---

## 🔍 Features

- Subnet input (e.g., `192.168.1.0/24`)
- Uses ICMP echo requests for stealthy host discovery
- Clean and minimal command-line interface
- Built with Python and `subprocess` module

---

## 🚀 Usage

```bash
python ragnarok.py 192.168.1.0/24
