import http.server
import os
import socketserver
import webbrowser
from pathlib import Path

PORT = 5500
BASE_DIR = Path(__file__).resolve().parent


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, format, *args):
        # Giữ terminal gọn gàng khi tải ảnh, video và âm thanh
        pass


def main():
    target_html = BASE_DIR / "index.html"
    source_html = BASE_DIR / "index-v30.html"
    if not target_html.exists() and source_html.exists():
        target_html.write_text(source_html.read_text(encoding="utf-8"), encoding="utf-8")

    os.chdir(BASE_DIR)
    with socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler) as httpd:
        url = f"http://127.0.0.1:{PORT}/index.html"
        print(f"Đang chạy học liệu số văn bản miêu tả lớp 5 tại: {url}")
        print("Nhấn Ctrl + C để dừng máy chủ.")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng máy chủ học liệu.")


if __name__ == "__main__":
    main()