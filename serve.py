import http.server, os
os.chdir('/Users/ripplingadmin/Desktop/carolineangwright.github.io')
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8765, bind='localhost')
