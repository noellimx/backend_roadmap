## Memory Hierarchy and Virtualization
- [ ] memory hierarchy
see also: [[Von Neumann Architecture]]
![[memory hierarchy.png]]

### **overriding principles**
- closer to CPU, needs faster prefetch, load and store
- balance cost (production, power), speed and needs
- hierarchy model to keep temporal (recent-used) and spatial locality.
	- using page tables to map physical addresses to virtual addresses
	- physical addresses are used to identify caches and main memory
	- address-translation cache (translation lookaside buffer) for fast address lookup
	- **TLB vs. Page Tables: Key Differences**

| **Aspect**       | **Page Table**                                    | **Translation Lookaside Buffer (TLB)**                     |
| ---------------- | ------------------------------------------------- | ---------------------------------------------------------- |
| **Function**     | Maps virtual addresses to physical addresses      | Caches recent virtual-to-physical address mappings         |
| **Location**     | Stored in memory (managed by the OS)              | Hardware cache inside the CPU                              |
| **Size**         | Large (can be very large in 64-bit systems)       | Small (typically 32 to 512 entries)                        |
| **Lookup Speed** | Slower (accesses memory)                          | Very fast (constant time access in hardware)               |
| **Granularity**  | Maps entire virtual pages                         | Stores translations for specific virtual pages             |
| **Efficiency**   | Can be slow due to large size and multiple levels | High efficiency due to fast hardware lookup                |
| **Usage**        | Used for every address translation in memory      | Used for frequently accessed addresses, speeding up access |

** from fast to slow latency **
- registers, inbuilt into CPU ~1 nanosecond
- SRAM for caches, 
	- organised into cache lines
		- L1 is nearest to CPU ~1-2 nanoseconds
		- L2 private to a CPU core ~3-10 nanoseconds
		- L3 shared between CPU cores ~10-30 nanoseconds
- DRAM for hard disks, main memory ~100 nanoseconds
	- using capacitor, need refresh (write-back) -> slower
- remote drives: NAND Flash for Solid State Drives
	- electrical charge stored in memory cells, organized into pages and blocks
- remote drives: tapes etc ~ Microseconds to milliseconds


