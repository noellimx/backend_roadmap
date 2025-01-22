![[Fundamentals#Elastic Compute Cloud (EC2)]]


# Restarting an Instance
- when detaching/attaching storage etc.
- dynamic IP may change

# Stopping an Instance
- ephemeral storage will be lost.
- **EBS** is a distinct service, still runs/chargeable.
- dynamic IP may change
- The instance type, kernel, RAM disk, and user data can be changed while the instance is stopped.
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

# Amazon Machine Image (AMI)
- Instance Template containing OS, software etc to launch a virtual server.
- **Cross region** supported.
	- Cross by creating a new AMI.
- "Baking" - Creating an image from a configured instance
	- Created image will store storage information (**block device mapping** + optional **snapshot**)
		- A new instance from an image will create a volume from the snapshot volume.
			- Modifications are independent from origin.

# Purchase Options
- On-demand
	- Default, instance is assigned to host by AWS
- Spot
	- Runs instance as long as set price is less than spot price
	- spot price > set price => may be evicted
	- **interruptible**
- Reserved
	- Pay for the reserved instance slot whether instance is running or not
- Dedicated Host
	- Charge per host
	- Set capacity
- Dedicated Instance
	- Host is not shared or owned
	- hardware is dedicated to user
	- no capacity management
# Saving Plans
- Hourly commitment for 1 or 3 years
- EC2, Fargate or Lambda


# Metadata
Within instance itself: 
`http://169.254.169.254/latest/meta-data`
`http://169.254.169.254/latest/dynamic`
`http://169.254.169.254/latest/user-data`