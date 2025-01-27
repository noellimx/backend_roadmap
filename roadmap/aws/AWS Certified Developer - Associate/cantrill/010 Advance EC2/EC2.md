# User Data
- User Data is on launch only
- AMIs does not store user data, it is part of the instance, not disk.

# Instance Profile
- Automatically created when IAM role is created via console.
- Attach IAM roles to an instance
- After selecting role for an instance, Systems Manager Agent (SSM) within the instance will create temporary credential based on the instance profile.

# Systems Manager Parameter Store
- Stores KMS-enrypted
	- configuration and secrets
	- Licenses
	- plain, ciphers
- In instance:
	- `aws ssm get-parameters --names <KEY> --with-decryption`
	- without `--with-decryption` will need to call KMS

# Integration with CloudWatch

- Instance needs to install a CloudWatch Agent
	- Configure with roles and attach log files

# Cluster Placement Group
- Shares underlying hardware with multiple instances
- Single AZ only
- Spread vs Cluster - separate or group one instance from another
- Partition - spread one group from another (can be different AZ, 7 instance per AZ)
- 10 Gbps single stream, instance to instance
