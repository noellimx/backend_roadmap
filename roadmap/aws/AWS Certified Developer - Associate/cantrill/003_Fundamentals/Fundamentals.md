
# Public vs Private Services

![[zone_visbility.png]]
# AWS Global Infrastructure

The AWS Cloud in Asia Pacific and China has 44 Availability Zones within 14 geographic Regions, with 34 Edge Network locations and 5 Regional Edge Cache locations.

**Regions (Availability Zones):**

Hong Kong SAR (3), Melbourne (3), Mumbai (3), Seoul (4), Singapore (3), Sydney (3), Tokyo (4), Osaka (3), Beijing (3), Ningxia (3), Jakarta (3), Hyderabad (3), Malaysia (3), Thailand (3).

**Edge Locations**

Auckland, New Zealand; Bangalore, India; Bangkok, Thailand; Brisbane, Australia; Chennai, India; Hanoi, Vietnam; Ho Chi Minh City, Vietnam; Hong Kong SAR, China; Hyderabad, India; Jakarta, Indonesia; Kolkata, India; Kuala Lumpur, Malaysia; Manila, Philippines; Melbourne, Australia; Mumbai, India; New Delhi, India; Osaka, Japan; Perth, Australia; Pune, India; Seoul, South Korea; Singapore; Sydney, Australia; Taipei, Taiwan; Tokyo, Japan; Beijing, China; Shanghai, China; Zhongwei, China; Shenzhen, China

**Regional Edge Caches**

Mumbai, India; Singapore; Seoul, South Korea; Tokyo, Japan; Sydney, Australia

# Virtual Private Cloud (VPC)
- logically isolated network
- 1 default VPC per region
- subnets are local to an availability zone
- peering is supported (user a's vpc in zone a to user b's vpc in zone b)
- Internet Gateway is attached
- Includes Security Group (SG) and network access control list (NACL)

![[vpc_fundamental.png]]

# Elastic Compute Cloud (EC2)

- Virtual server (compute point). [CPU-Memory-Disk-NIC]
- Infrastructure as a service.
- Default private - attached to vpc network, AZ resilient.
- Range of specifications (size, capabilities...).
- On demand billing - storage, cpu usage
- Storage local or Elastic Block Store (EBS)
- Lifecycle - running -> stopped -> terminated
	- running cost: (CPU | Mem), Disk, Network Traffic
	- stopped does not omit charges from disk.
	- terminated is non-reversible
- *Amazon Machine Image* - snapshot of an image
	- root volume
	- block device mapping - attach store/EBS volume to instance
- access via ssh ::3389

# Simple Storage Service (S3)
- Storage Platform - public, housed in a region
- for blobs: media, files, big data
- Object: key => value (content)
- Objects are placed into **Buckets**. 
	- Since storage is public -> bucket name is globally unique.
	- Buckets are structurally flat (no concept of mounting or hierarchy).
	- One account is limited to 100/1000 (soft/hard) buckets.
	- One bucket is capped at **5TB**.

# CloudFormation
- Infrastructure as code.
- Host templates in repository for portability.
- Declarative representation of a **stack**.
- Maps logical resource in template to physical resource (creation).

# CloudWatch
- Region-based
- Observability and metrics for resource usage.
- Retent, manage and analyse.
- Generate logs + trigger events.
	- Stream = time-ordered Logs[]
	- Logs = { timestamp + message }


# Shared Responsibility Model for Security

- AWS User - Interface, Application, Data Security
- AWS - Platform, Infrastructure


# High Availability | Fault Tolerance | Disaster Recovery
- High Availability: Maximizing service uptime.
- Fault Tolerance: A fault on one or more parts of a system does not bring down the whole system. Works through and after failure.
- Disaster Recovery - offsite backups and spare resources

# Route53 (DNS)

- Domain Registration and Name Servers
	- DN validation with external provider
	- IP to DN binding
- Record Types: NS, A, AAAA, MX, TXT

# Elastic Network Interface (ENI)

- Contains:
	- Mac address
	- 1 IPv4/DNS private to the VPC
	- Additional secondary IPv4s
	- 1 Optional public IPv4
		- dynamic on restart
		- resolves to
			- Private IP within VPC
			- Public IP beyond VPC
		- If Elastic IP is assigned => replaces public, ephemeral IPv4
	- Additional IPv6 addresses
		- Conceptually publicly resolveable



# Amazon Resource Name

`arn:<partition>:<service>:<region>:<account-id>:<resource-id>`


# CloudTrail
- 90 days no-cost logging of api calls/activities.
	- Near real-time, around 50 minutes delay.
	- Stored in [[#Simple Storage Service (S3)]].
- Event Types:
	- Management: Control planes operations (initialize/terminating resource)
		- Default enabled, no charge
	- Data: Input / Output, optional and charge-able
	- Insight
- Region-based
	- Global service events (Route53, STS, Cloudfront) enable on configuration.
	- Logged into `us-east-1`
- Can log into CloudWatch
- In an organisation, a management account can see member account's log.


# Key Management Service (KMS)
- Region-based and public service.
- Create, manage, store asymmetric/symmetric keys.
	- supply own key to KMS for KMS to encrypt.
		- `kms_encrypt(OWNKEY) -> ENCRYPTED_OWN_KEY` (keep the encrypted key)
		- `kms_decrypt(ENCRYPTED_OWN_KEY) -> OWNKEY` (discard own key after use)
- FIPS 140-2 Level 2 compliant.
	- Use custom key store by CloudHSM (Hardware Security Module) for FIPS 140-2 Level 3 compliance.
		- CloudHSM: not integrated with other AWS services, AWS only provides the hardware, user manages it.
- CMS Keys are generated or imported:
	- As a resource (policy configurable)
	- Encrypted before storing, never leaves KMS.
	- A decrypt client request will 1) decrypt the stored key 2) decrypt the client cipher to obtain the plaintext.
- Sample Decrypt(ciphertext=Encrypt(**your own key**))
	- `aws kms encrypt --key-id=alias/key1 --output=text --query=CiphertextBlob --plaintext=fileb://./plain --cli-binary-format raw-in-base64-out | xargs -I {} aws kms decrypt --output=text --ciphertext-blob={} --query=Plaintext | base64 --decode`
![[key_policy_sample#Sample Policy]]

# Elastic Block Store (EBS)

## SSD Volume Types
- gp2/gp3
	- General Purpose
	- boot volumes, virtual desktops, single instance database
- io2/io3
	- sub-millisecond latency
	- for I/O instensive operations
## HDD Volume Types
- st1 (throughput-optimized), sc1(cold)
- slow, cannot support boot/store root volume
