#!/data/data/com.termux/files/usr/bin/bash
pkg update -y && pkg upgrade -y
pkg install python git curl -y
pip install --upgrade pip
pip install requests discord.py colorama aiohttp

mkdir -p /sdcard/Download

curl -o /sdcard/Download/launcher.py https://raw.githubusercontent.com/YutaDev123/SelfBot-Multi-Token/main/launcher.py

echo -e "\e[32mDone Setup! Launcher đã được tải về "
echo -e "Run tool bằng lệnh:\ncd /sdcard/Download && python launcher.py\e[0m"
