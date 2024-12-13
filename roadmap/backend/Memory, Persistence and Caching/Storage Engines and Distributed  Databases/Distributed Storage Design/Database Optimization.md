
- [ ] Performant Read
- [ ] Performant Write (Data Integration)
- [ ] Distributiveness

Performant Read vs Performant Write

### scans

- [ ] bitmap scan
- [ ] index scan

### join strategies

### Hash Join vs Merge Join:

| Aspect               | **Hash Join**                                             | **Merge Join**                                         |
| -------------------- | --------------------------------------------------------- | ------------------------------------------------------ |
| **Sort Requirement** | Does not require sorting of input tables                  | Requires input tables to be sorted on the join key     |
| **Memory Usage**     | Can be memory-intensive, especially for large hash tables | Generally low memory usage                             |
| **Best for**         | Large, unsorted tables, or when one table is small        | Sorted data or when there are indexes on join keys     |
| **Performance**      | Can degrade if memory is insufficient (spills to disk)    | Very efficient if tables are already sorted or indexed |
| **Time Complexity**  | O(N) for hashing + O(M) for probing                       | O(N + M), where N and M are the number of rows         |

