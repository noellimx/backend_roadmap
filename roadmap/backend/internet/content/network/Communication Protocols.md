#network #protocols

### See also
[[Open Systems Interconnection(OSI) Model]]


# Principles

- reliable - fast and correct, faults are transient
	- best-effort routing
	- standardized addressing scheme
- secure
- cost-efficient
- scalable
	- broadcasting
	- scheduling
- versatile
	- support for variety of digital services and applications



## Standard Protocols
### Layer 3/4
- [x] Transmission Control Protocol / Internet Protocol (IP) with SSL ⏬ ✅ 2024-12-08
- uses IP + port socket addressing scheme
-  connection handshake
	- client SYN -> server ACK/SYN -> client SYN
- Secure Sockets Layer/ [[Transport Layer Security]] handshake
	- client Hello
		- sends TLS version options, cipher suite options, client random
	- sever Hello
		- select TLS version and cipher suite, server random and cert
	- client verify server's certificate through Certificate Authority (match cert's public key, identity, sign method etc)
	- key exchange: obtain shared secret using [[Diffie-Hellman_Key_Exchange]]
		- Agree on a prime G and mod p
		- ![[diffie_hellman.png]]



- [x] User Datagram Protocol ✅ 2024-12-08
- uses IP + port socket addressing scheme

### Layer 6/7
- [x] Domain Name System (DNS) ⏬ ✅ 2024-12-08
- translates names (identification strings) to IP addresses
- database chain of authority (roots, trust anchors etc)
- stores cached records - start of authority, ip addresses, SMTP mail exchangers, name servers
- port 53

- [x] Hypertext Transfer Protocol (HTTP) ⏬ ✅ 2024-12-08
- Stable: 1.1 (TCP), 2 (TCP), 3(UDP)
- Request-Response unidirectional mode in client-server model
- Messages exchanged by session layer connection, usually TCP but recently UDP also
- Persistent Connection (HTTP/1.1 onwards)
	- reduce latency, round trips -> better throughput
	- keep alive for time or request quantum
- Packet
	- Request Line: METHOD + URL + VERSION
	- Headers
		- User-Agent
		- Content-Type
		- Host
		- Client specific: Accepted content/encoding scheme, Last-Modified
		- Set-Cookie
	- Body
- [x] File Transfer Protocol (FTP) ⏬ ✅ 2024-12-08
- [x] Secure Shell (SSH) ⏬ ✅ 2024-12-08
- [x] Simple Mail Transfer Protocol (SMTP) ⏬ ✅ 2024-12-08



# Addressing Scheme


- **MAC address**: Layer 2 (Data Link Layer)
- **IP address**: Layer 3 (Network Layer)
- **Port numbers**: Layer 4 (Transport Layer)

Ports, IP addresses, and MAC addresses each reside on different layers of the **OSI model** (Open Systems Interconnection model). Here's how they map to specific layers:

1. **IP Address (Internet Protocol Address)**:
    
    - **Layer 3: Network Layer**  
        The IP address is used to identify devices across networks and is involved in routing data between different networks (i.e., across routers).
2. **MAC Address (Media Access Control Address)**:
    
    - **Layer 2: Data Link Layer**  
        The MAC address is a unique identifier for network interfaces at the hardware level (such as network cards) and is used for communication within the same local network (LAN).
3. **Ports (Port Numbers)**:
    
    - **Layer 4: Transport Layer**  
        Ports are part of the Transport Layer and are used to identify specific processes or services running on a device (e.g., HTTP uses port 80, HTTPS uses port 443). Port numbers are used by protocols like TCP and UDP to direct data to the correct application on a host.



### **Well-Known Ports and Services**
See [[Open Systems Interconnection(OSI) Model#Layer 4 - Transport]]

|**Port**|**Service**|**Protocol**|**Description**|
|---|---|---|---|
|**20**|FTP Data Transfer|TCP|File Transfer Protocol (active mode, data transfer)|
|**21**|FTP Control|TCP|File Transfer Protocol (control, command channel)|
|**22**|SSH|TCP|Secure Shell, used for encrypted remote login and commands|
|**23**|Telnet|TCP|Unencrypted remote login protocol|
|**25**|SMTP|TCP|Simple Mail Transfer Protocol (used for email sending)|
|**53**|DNS|UDP|Domain Name System (resolves domain names to IP addresses)|
|**67**|DHCP Server|UDP|Dynamic Host Configuration Protocol (for assigning IP addresses)|
|**68**|DHCP Client|UDP|Dynamic Host Configuration Protocol (client side)|
|**69**|TFTP|UDP|Trivial File Transfer Protocol (simple file transfer)|
|**80**|HTTP|TCP|Hypertext Transfer Protocol (used for web traffic)|
|**110**|POP3|TCP|Post Office Protocol 3 (email retrieval from server)|
|**119**|NNTP|TCP|Network News Transfer Protocol (used for newsgroups)|
|**123**|NTP|UDP|Network Time Protocol (for synchronizing clocks)|
|**143**|IMAP|TCP|Internet Message Access Protocol (email retrieval)|
|**161**|SNMP|UDP|Simple Network Management Protocol (for network management)|
|**194**|IRC|TCP|Internet Relay Chat (for chat services)|
|**443**|HTTPS|TCP|Hypertext Transfer Protocol Secure (encrypted web traffic)|
|**445**|Microsoft-DS|TCP|Microsoft Directory Services (used by SMB for file sharing)|
|**514**|Syslog|UDP|System Log Protocol (used for sending system log messages)|
|**587**|SMTP (Submission)|TCP|SMTP for sending email (authenticated submission)|
|**631**|IPP|TCP/UDP|Internet Printing Protocol (for printing services)|
|**993**|IMAPS|TCP|Secure IMAP (encrypted email retrieval)|
|**995**|POP3S|TCP|Secure POP3 (encrypted email retrieval)|
|**1080**|SOCKS Proxy|TCP|SOCKS Proxy (used for internet proxying)|
|**1433**|Microsoft SQL Server|TCP|Default port for SQL Server database connections|
|**1434**|Microsoft SQL Monitor|UDP|SQL Server Monitor (used by SQL Server)|
|**3306**|MySQL|TCP|MySQL database default port|
|**3389**|RDP|TCP|Remote Desktop Protocol (for remote desktop connections)|
|**5432**|PostgreSQL|TCP|PostgreSQL database default port|
|**5900**|VNC|TCP|Virtual Network Computing (remote desktop protocol)|
|**6379**|Redis|TCP|Redis (in-memory data structure store)|
|**8080**|HTTP Alternate|TCP|Alternate HTTP port (often used for development or proxies)|

### **Some Other Notable Ports**

|**Port**|**Service**|**Protocol**|**Description**|
|---|---|---|---|
|**69**|TFTP|UDP|Trivial File Transfer Protocol (for bootstrapping and simple file transfers)|
|**161**|SNMP|UDP|Simple Network Management Protocol (for network management)|
|**443**|HTTPS|TCP|Hypertext Transfer Protocol Secure (encrypted web traffic)|
|**8080**|HTTP Alternate|TCP|Alternate HTTP port (often used for development or proxies)|