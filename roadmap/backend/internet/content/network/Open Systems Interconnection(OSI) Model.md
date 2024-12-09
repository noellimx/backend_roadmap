#network 

# Layers - Low Level

## Layer 1 - Physical

- Transmission medium - radio waves (geo-stationary / space satellites), cable (coaxial, fibre-optic etc)
- "on the wire" (light, electricity) decodes/encodes symbol into binary representation of datum for upper layers
- 
## Layer 2 - Data Link

- "pushes" data stream from one node to another, i.e Ethernet
- Physical Addressing scheme: Media Access Control assigned to network interface (hardware)

## Layer 3 - Network

- Logical Addressing scheme: IPv6, IPv4

# Layers - High Level

## Layer 4 - Transport
See [[Communication Protocols#Layer 3/4]]

- Connection-orientedness
	- node/host recognition
	- stateful for ordering and error handling of messages
- flow control
	- congestion avoidance
	- error checking

## Layer 5 - Session
- Session establishment and synchronization
## Layer 6 - Presentation
- Syntax transliteration from data (compression, encoding, encryption)
## Layer 7 - Application
- Semantics for high level processes and services



