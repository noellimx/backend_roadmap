
![[Fundamentals#CloudWatch]]

- Namespace - container for metrics
- Datapoint - `timestamp + value + unit of measure`
- Metric - `time-ordered set of data points`
	- `CPUUtilization`, `DiskWriteBytes` ...
	- Resolution = interval (frequency)
	- also includes **dimensions**
	- `instanceId` etc
# Retention
as data ages, data is aggregated with less granularity.