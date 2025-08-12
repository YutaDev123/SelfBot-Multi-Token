#!/data/data/com.termux/files/usr/bin/bash
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip
pip install requests discord.py colorama aiohttp

echo -e "\e[32mDone Setup!Run Tool: python launcher.py\e[0m"
