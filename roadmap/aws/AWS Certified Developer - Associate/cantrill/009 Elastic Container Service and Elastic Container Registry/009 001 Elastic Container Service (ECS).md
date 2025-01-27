- managed container service

# Tasks

Configuration for a set of containers
- Ports to expose
- CPU/memory allocation
- Environment variables
- Security (Roles...)

# Service
Runs instantiations of (multiple) Tasks in a cluster
-  Service definition:
	- Launch type: `EC2` or `Fargate`
		- `EC2` if you want to manage the underlying host along with EC2 constraints (AZ resilience...)
		- `Fargate` if want to plug and play, AWS will identify and provision resources accordingly from shared infrastructure
			- From network perspective, deployment is attached to a VPC
	- Platform: OS to use
	- Cluster: AWS Cluster ARN to deploy in
	- supports Blue/Green deployment
	- LoadBalancer: balancer to use
	- Security (Roles...)
