
- [ ] Database Principles
# ACID Principle

A definition of principles a distributed database engine must adhere to in the transaction paradigm

- **Atomicity**
	- "All-or-nothing"; A set of statements or instructions must execute together or none at all.
	- 2 possible outcomes - **Abort** and **Commit**
		- **Abortion** due to (partial) failures
			- Data integrity violation (parse failure)
			- Deadlocks
			- Constraint logic violation (inconsistent state)
				- The end state of multiple transactions is not a valid state of any possible ordering of all statements.
			- Resource limitations (session timeout, buffer limit)
		- **Commit**
			- No errors
		- intermediate phases for partial transactions, prepare-to-commit etc.
	- Approaches to achieve outcomes:
		- **Write-Ahead Logging**
			- audit trail
			- recovering from time-wise crash point
		- **Shadow Paging**
			- modifies copies of pages, keeps record of dirty pages
			- flip pointer
- **Consistency** 
	- A query should return the correct results, regardless of the internal design of the database system. See: [[Memory Consistency Model]]. 
	- Enforcement of an accurate modelling of the real world
		- Entity uniqueness
		- Is-a, Has-a relation
- **Isolation**
	- A transaction (ordered set of statements) executes as if all transactions are executed sequentially. In other words, all other interleaving transactions are transparent to the transaction in execution. The transparency level can vary. See: [[Concurrency Control]]
# BASE Principle
## CAP and PACELC Theorem

See:       [[Perspectives on the CAP Theorem.pdf]]
		[[CAP and PACELC Theorem]]





