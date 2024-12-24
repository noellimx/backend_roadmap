### Readings
- [[A Primer on Memory Consistency and Cache Coherence - 2nd Edition.pdf]]
- [[Memory Consistency Model#Overarching Principle]]

## Incoherence Problem
- Multiple actors (cores) accessing copies of a datum from multiple cache levels, and at least one actor is writing (incoherent state).
- Pertaining to all storage structures (cache,TLB, main memory) of a *shared address space* 

## Solution
- Invalidation of stale data
- Propagation of fresh data (full visibility)
- Prevention by design and implementing a cache coherence protocol
	- Each storage structure having a *[[Cache Controller|cache controller]]* (finite state machine) to interact with each storage module.
- Not visible to the programmer, restricted to coherence protocol.

## Cache States (MOESI)
- Modified, Owned, Exclusive, Shared, Invalidated


## Cache Coherence Interface

### Methods
- Read(memory_addr) -> val:Data
- Write(memory_addr, val:Data) -> ack:Data


### Coherence Invariant
- At any given epoch:
	1) Single Write Multiple Read of memory location 
	2) Reads return same value (state)

### Protocol Types
Consider actors (memory pipelines) are executed out-of-order, there are 2 main types of protocols:
1) **Consistency-agnostic**
	- Synchronous write propagation to all caches
	- as if caches are absent - client reads/write a atomic memory system
	- Good separation of concerns
2) **Consistency-directed**
	- Asynchronous write propagation (allows dirty read of stale data)
	- Still maintains/enforce coherence by design , i.e read/write orders
 3) 