import lib
import socketserver
import socket
import sys
import time
import logging


def my_main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = "10.10.36.147"
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    lib.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, lib.PORT)
    lib.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, lib.PORT)
    server = socketserver.UDPServer((lib.HOST, lib.PORT), lib.UDPHandler)
    server.serve_forever()


my_main()