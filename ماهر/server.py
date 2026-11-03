import http.server
import socketserver
import webbrowser
import socket
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    local_ip = get_local_ip()
    url = f"http://localhost:{PORT}"
    network_url = f"http://{local_ip}:{PORT}"

    print("=" * 60)
    print("      نظام إدارة ديون ومشتركي المولدة - السيد ماهر")
    print("=" * 60)
    print(f" [✓] السيرفر يعمل الآن بنجاح!")
    print(f" [🖥️] للفتح على هذا الكمبيوتر: {url}")
    print(f" [📱] للفتح من الموبايل (نفس شبكة الواي فاي): {network_url}")
    print("=" * 60)
    print(" اضغط Ctrl+C لإيقاف السيرفر في أي وقت")
    print("=" * 60)

    try:
        webbrowser.open(url)
    except Exception:
        pass

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nتم إيقاف السيرفر. مع السلامة!")
            sys.exit(0)
