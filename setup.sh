#!/data/data/com.termux/files/usr/bin/bash
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip
pip install requests discord.py colorama aiohttp
echo "Setup xong! Chạy tool bằng lệnh: python launcher.py"
