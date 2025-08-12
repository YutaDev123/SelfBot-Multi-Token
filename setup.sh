#!/data/data/com.termux/files/usr/bin/bash
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip
pip install requests discord.py colorama aiohttp
echo "Done Setup!Run tool: python launcher.py"
