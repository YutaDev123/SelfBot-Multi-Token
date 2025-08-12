import os
import requests

URL = "https://raw.githubusercontent.com/YutaDev123/SelfBot-Multi-Token/refs/heads/main/main.py"
SCRIPT_FILE = "main.py"
WORK_DIR = "/sdcard/Download"  # Thư mục bạn muốn chạy script

def update_script():
    try:
        print("[*] Đang kiểm tra cập nhật từ GitHub...")
        r = requests.get(URL)
        if r.status_code == 200:
            # Lưu file vào WORK_DIR
            with open(os.path.join(WORK_DIR, SCRIPT_FILE), "wb") as f:
                f.write(r.content)
            print("[+] Đã tải bản mới nhất.")
        else:
            print("[-] Không tải được file, status code:", r.status_code)
    except Exception as e:
        print("Lỗi khi cập nhật:", e)

def run_script():
    print("[*] Đang chạy file main.py ...")
    os.chdir(WORK_DIR)
    os.system(f"python {SCRIPT_FILE}")

if __name__ == "__main__":
    update_script()
    run_script()
