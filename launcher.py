import os
import requests

URL = "https://raw.githubusercontent.com/YutaDev123/SelfBot-Multi-Token/main/main.py"
SCRIPT_FILE = "main.py"

def update_script():
    try:
        print("[*] Đang kiểm tra cập nhật từ GitHub...")
        r = requests.get(URL)
        if r.status_code == 200:
            with open(SCRIPT_FILE, "wb") as f:
                f.write(r.content)
            print("[+] Đã tải bản mới nhất.")
        else:
            print("[-] Không tải được file, status code:", r.status_code)
    except Exception as e:
        print("Lỗi khi cập nhật:", e)

def run_script():
    print("[*] Đang chạy file main.py ...")
    os.system(f"python {SCRIPT_FILE}")

if __name__ == "__main__":
    update_script()
    run_script()
