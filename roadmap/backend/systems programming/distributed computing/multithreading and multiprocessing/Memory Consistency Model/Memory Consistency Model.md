### Readings
- [[A Primer on Memory Consistency and Cache Coherence - 2nd Edition.pdf]]
- [[Cache Coherence]]
# Overarching Principle

- **Liveness** - Good things happen eventually. 
- **Safety** - Only good things happen.

- A contract or design between programmer and system to guarantee correctness of order. See [[Memory Consistency Model#Sequential Consistency|Sequential Consistency]]
- A memory model to specify the behaviour of multi-threaded programs executing with shared memory.
	- Multiple correct behaviours are allowed in a multi-threaded environment
		- Non-deterministic - intermediate order of execution varies but outcome (end state) is the same (logical equivalence)


## Models
https://jepsen.io/consistency/models
![[Consistency Model_jepson.png]]
*Linearizability* if `op_a()` responds before invocation of `op_b()` , then the result of `op_a` is a precondition for the invocation of `op_b`. 
### Sequential Consistency In Multithreaded, Multi-level Memory Environments

Given all threads and storage structures, the execution is a permuted order of instructions that also respects the order of execution in each thread. A permuted order that is deterministic is a stronger model of consistency (strict consistency)

- 2 Requirements : Atomicity and Program Order