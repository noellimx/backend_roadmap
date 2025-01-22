![[Fundamentals#Elastic Compute Cloud (EC2)]]


# Restarting an Instance
- when detaching/attaching storage etc.
- ephemeral storage will be lost
- dynamic IP may change
- **EBS** is a distinct service, still runs/chargeable.
# Storage (Disk)
- **Maximum combined persistent storages IOPS** = 260,000 IOPS
- Instance Store (non-persistence)
	- `ephemeral0`,..., `ephemeral24` on a single host.
	- for **linux**, can boot from Instance Store (files will be copied over to root volume in EBS)
- Elastic Block Store
	- See [EBS - Fundamentals](Fundamentals#Elastic Block Store (EBS)) and [[EBS]]
	- persistence
	- within same AZ
	- can snapshot and migrate to another AZ
	- detachable
- Elastic File System
	- Support cross-region replication


