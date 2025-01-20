# Services
IAM, IAM Identity Center

- AWS account starts with root user, with the option to create more users under the same account.
	- max 5000 AIM users per account
	- max 10 groups for a single user
- Manage policies of users, groups and roles to limit or allow permissions (default is **deny all**)
- Authentication
- Supports federation.
- MFA to dashboard
	- pins via authenticator app
	- passkeys device recognition
- Access keys to console
	- Key ID + Secret Access Key (secret is visible once)


## Policy

- A collection of statements to express permissions.
- Explicit Deny > Explicit Allow > Implicit Deny
- Example:
```
{
	"Version" : "2020-02-02",
	"Statement" : [
		{
			"Sid": "FullAccess",
			"Effect": "Allow",
			"Action": ["s3:*"],
			"Resource": ["*"]
		}
	]
}
```

- Managed Policy: can be reused and applied to multiple users, lesser management overhead

# User Group
- collection of users
- can add policies
- NOT principals, cannot be referenced by a resource policy

# Role (IAM)
- Trust policies authorizes principals.
- Permission [policies](#Policy) applies permissions.
- Assumed temporarily by principals:
	- External principals such as web identities (google,x ...).
	- Internal principals such as AWS service or cross-account user.
- Secure Token Service will provide short term credentials.
- Case Study: Lambda
	- Elastic service (0 to many)
	- credentials on demand
- Case Study: External Microsoft Active Directory
	- roles can support > 5000 (the limit for no. of IAM users/account)
		- map multiple users to single role
- Case Study: App consumers accessing AWS service
	- Client app does not need to store aws user credentials, assume a role by a web identity.

# Role (Service-linked)
- specific to a certain AWS service to interact with other AWS services.


# Security
- `sts:AssumeRole`
- key id + secret pair, limited permissions wand expires.

# Organizations

- Management Account - account that creates an organization.
- Invites other accounts to be members.
- Organization is hierarchal.
	- Member defers billing management to management account.

# Service Control Policies
- Setting permission boundaries for the **organisation** and organisation units.
	- Restrict region, storage size etc
	- If account is restricted, the root user of the account is also affected.
- **Does not grant effective permission**. 
	- Effective permission = (Service Control Policy + Resource Control Policy) Intersecting with Identity/Role Policy.

# CloudWatch Logs

![[Fundamentals#CloudWatch]]

- Integration with AWS services (EC2, CloudTrail etc) using
	- natively in service
	- Unified CloudWatch Agent
	- SDKs
- Regional

# CloudTrail

![[Fundamentals#CloudTrail]]