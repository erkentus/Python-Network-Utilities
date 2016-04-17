# Python-Network-Utilities
Python Network Utilities for Linux/Windows systems

## Netcat
Simple netcat implementation in python 2.7 - to open up command line access through tcp connection on the remote host

Two files 
1. netcat-server.py - to be placed in the server where command access is required
2. netcat-client.py - to establish tcp connection, run commands, receive output

Run netcat-server
```bash
#default port 8001, localhost IP - 127.0.0.1
python netcat-server.py 

```

Run client (public IP of the remote host - 54.54.54.54)
```bash
python netcat-client.py -t 54.54.54.54 -p 8001
```
