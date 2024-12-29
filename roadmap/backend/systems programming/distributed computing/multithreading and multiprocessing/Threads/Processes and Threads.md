- [ ] Threads ⏫ 
### readings
[CoreDumpped: Why threads are needed in a single core](https://youtu.be/M9HHWFp84f0?si=S0Qjc1RrJvPo5smx)
[CoreDumpped: IPC: to share memory or pass message](https://youtu.be/Y2mDwW2pMv4?si=1jz4fH_BlJnluKER)



## Components of a Process

- Static
	- Text (code/instructions)
	- Data (variables)
	- Register Set - load/store data in execution
- Dynamic on runtime
	- Heap - dynamically allocated memory
	- Stack - for control flow
	- Program counter - track next instruction using instruction register
## Process Control Block
```
struct ProcessControlBlock /*process*/ {
	id
	memory_manager
	io_manager
	file_manager
	parent:ProcessControlBlock
	threads:[]Thread_t
}

struct Thread_t {
	id
	state:State
	program_counter
	gp_registers
	ins_register
	flags
	stack_pointer
	process:ProcessControlBlock
}
```
