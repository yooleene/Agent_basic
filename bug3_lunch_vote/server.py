# -*- coding: utf-8 -*-
"""
점심 메뉴 투표 페이지 서버
브라우저에서 http://localhost:8000 으로 접속하면 투표 페이지가 보입니다.
"""

import http.server
import socketserver
from pathlib import Path

PORT = 8000
BASE = Path(__file__).parent
SERVE_DIR = BASE / "public"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SERVE_DIR), **kwargs)

    def log_message(self, fmt, *args):
        print(f"  [요청] {fmt % args}")


def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print()
        print("=" * 46)
        print(f"  서버 실행 중 →  http://localhost:{PORT}")
        print("=" * 46)
        print("  종료하려면 이 터미널에서 Ctrl + C")
        print()
        httpd.serve_forever()


if __name__ == "__main__":
    main()
