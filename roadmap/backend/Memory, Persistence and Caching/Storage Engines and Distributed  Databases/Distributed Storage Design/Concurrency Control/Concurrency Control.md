- [ ] [[Transaction Isolation]]

# Problem
- Sequential execution is slow and unfair (blocks other transactions).
- A transaction acting on incorrect data
	- reads data that is yet to be committed (dirty read)
	- a re-read of a single row has changed from initial read due to write commit by another transaction (non-repeatable read)
	- a re-read of a subset of rows has changed from initial read due to write commit by another transaction (phantom read)
	- a successful commit of a group of transactions is inconsistent with any execution order of their statements (transaction inconsistency/serializable anomaly)

# Solution
- Allow interleaving while providing guarantee levels
	- Synchronization via [[Database Locks|database locks]].
# Protocols
## Pessimistic

- Prevention by Look-Ahead
	- Denial of conflicting requests

## Optimistic





