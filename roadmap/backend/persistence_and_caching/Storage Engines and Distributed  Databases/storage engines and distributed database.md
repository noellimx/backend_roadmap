[[Distributed Storage Design]]
[[Storage Engines]]


### Query Execution Plan

1. Connection
2. Parse
	- Syntax, semantic checking
	- tokenization/algebrization into objects in a parse tree
3. Rewrite
	- modify parsed form into query tree based on pre-defined rules that can be executed more efficiently
4. Plan
	- orders operations (), select [[Database Optimization#scans|scans]] and [[Database Optimization|best access path]], I/O and CPU cost
5. Execute


