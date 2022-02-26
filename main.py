import lib
import socketserver
import socket
import sys
import logging


def init_main(hostname, ip):
    logging.info(hostname)
    if ip == "127.0.0.1":
        ip = sys.argv[1]
    logging.info(ip)
    lib.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ip, lib.PORT)
    lib.topvia = "Via: SIP/2.0/UDP %s:%d" % (ip, lib.PORT)
    server = socketserver.UDPServer((lib.HOST, lib.PORT), lib.UDPHandler)
    server.serve_forever()


hostnm = socket.gethostname()
my_ip = socket.gethostbyname(hostnm)

init_main(hostnm, my_ip)
