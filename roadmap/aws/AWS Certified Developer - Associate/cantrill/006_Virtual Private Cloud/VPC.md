![[Fundamentals#Virtual Private Cloud (VPC)]]


# Custom VPCs

- Maximum 5 VPC per AZ.
- 1Pv4 CIDR Blocks and Public IPs
	- 1 Primary Private Block
	- Block masks from /16 - / 28 (max 65336 hosts, min 16 hosts)
	- can have IPv6 enabled (assignment strictly by AWS)
- DNS Settings:
	- `enableDnsHostnames` - assign instances DNS names
	- `enableDnsSupport` - enable DNS resolution
- Subnets
	- Reserved IPs:
		- Network address - first addr
		- VPC Router address - second addr
		- Reserved for DNS - third
		- Reserved for future use - fourth
		- broadcast - last
	![[vpc_subnet.png]]
# Internet Gateway
- 0..1 IGW to 0..1 VPC
- Maintains mapping of public to private address in VPC
# Route Tables
- settings to map DST of incoming packets to next hop
	- more specific range -> higher precedence
- `0.0.0.0/0 -> IGW` Route any DST back to IGW


# Stateless vs Stateful Firewalls
- Stateless: does not know if traffic is part of a stateful connection
- Stateful: does recognise a connection i.e if request is allowed => subsequent communications is allowed.

# Security Features
## Network Access Control List
- Stateless firewall for VPCs
- M Subnets : 1 NACL
## Security Group
- Access control on an instance, IP or security group (resource) level.
- Whitelist only.


# Network Address Translation (NAT) Gateway
- Remapping SRC or DST of traffic.
- Runs from public subnet.
