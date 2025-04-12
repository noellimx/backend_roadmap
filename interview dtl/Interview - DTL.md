
```
package main

import "fmt"

  

func main() {

  fmt.Printf("Hello")

}

  

// Golang

// 

  

conn.Write() - Not block M thread

conn.Read() - Not block machine thread?

// epoll?

  

// 

// sync.Mutex vs sync.RWMutex

  

var counter uint64

  

increase it in multi-goroutines?

  

// Memory Model? <- Atomic Variable

  
  

// Databases

// - Postgres

// - MySQL -> Postgres

  

// X (a, b, c, d) <- BTREE (a, b, c) <- THis

  

// 1 mill

  

SELECT a, b, c, d FROM

WHERE a >= ? AND a <= ?

  

SELECT a, b, c FROM

WHERE a >= ? AND a <= ?

  

// When index-only scan?

  

// ACID properties

  

A - Atomicity: 

C

I - 

D - Durability: Stored in Disk

  
  

tx = Begin()

tx.INSERT A

tx.INSERT B

err := tx.Commit() // RETURN err = nil

// DB restart => data still persist?

  

// 

file, err := os.Create("file1")

if err != nil {

  panic(err)

}

  

_, err := file.Write([]byte("data 01"))

err = nil

  

// OS restart

// fsync? Redis

  
  

Atomicity, How DB does that?

// Write Ahead Logging?

// wal <- Postgres

  
  

2 Phase Locking?

  
  

How to lock the row when SELECT?

  

BEGIN

SELECT * FROM ... FOR UPDATE

...

COMMIT

  
  
  

// Golang

  

var a int

var mutA sync.Mutex

var b int

var mutB sync.Mutex

  

func transfer() {

  mutA.Lock()

  a -= 10

  mutA.Unlock()

  mutB.Lock()

  b += 10

  mutB.Unlock()

  Strongest Isolation Level?

  - Read Un

  - Read Committed

  - Repeatable

  - Serialization

  MVCC? What main reason of MVCC?

}

  
  

// Distrbuted Systems 

  

- Transactional Outbox?

  

Write A DB

Send Kafka

  

- Raft Consensus?

- CAP Theorem?

- Split Brain?

  

Redis Sentinel?

Persistence of Redis?

BGSAVE & AOF
```