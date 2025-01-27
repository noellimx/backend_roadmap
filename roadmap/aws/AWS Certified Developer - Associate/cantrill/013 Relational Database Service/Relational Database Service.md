- Database Server as a Service
	- Manages one or more database instance per server

# Architecture


- One server attaches to a VPN (recall - within a region) across a *subnet group*.
	- For multi-AZ deployments:
		- An *primary* instance asynchronously replicates to a *standby* instance for failover.
	- Can be exposed publicly (using route tables, R53 etc.)
- Each db instance in a server has dedicated EBS storage.

# Cost

- Instance Type
	- Storage Type
	- Storage Size
- Single/Multi-AZ
	- Replicas/Backups
		- GB-month
- Data transfer cost
- Licensing for Commercialised database engine