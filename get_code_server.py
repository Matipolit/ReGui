from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

logging.basicConfig(level=logging.INFO)
code = ""
done = False


class Handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        global done, code
        if "authorize" in self.path:
            logging.info(f"Got request: path={self.path}")
            code = self.path.split("code=")[1]
            self._set_response()
            self.wfile.write(b"Application authorized. You may now close this window.")
            done = True


def get_code(port=8080):
    with HTTPServer(("", port), Handler) as httpd:
        while not done:
            httpd.handle_request()
    return code
