![[Fundamentals#Elastic Block Store (EBS)]]
# Snapshot

- Full origin-copy, cross-region
- New EBS volume has immediate full performance
	- Incrementals are lazy loaded.
- Incremental snapshot backed by S3
- **Fast Snapshot Restore**
	- up to 50 snaps per region
		- i.e if 1 snap per AZ => 4 snaps used for 4 AZ.
- Cost by usage (GB-month), not size allocation.
- **KMS Encryption** for copies uses the same DEK.