"""
The purpose of these scripts is to check the limits of RDS instance.
And once we have reached the limits, evaluate the options we have to serve higher traffic.

- A script to continuously write to the database.
    - Create 50 connections to the database.
    - Each of these connections will simulate an application thread.
    - Let's say we want to simulate 1000 writes per second.
    - Thus each of these connections need to do 1000/50 i.e 20 insertions per second.
    - It depends on the latency of each write statement. If say each insertion takes 100 ms, then
      a connection would be able to do only 10 insertions per second.
    - In such case, we can try increasing the number of connections to say 100 and try to accomplish
      1000 insertions per second.
- A script to continuously read from the database.
    - Similarly create multiple connections to the database.
    - Do a like query which is computationally intensive.

Questions
- How to check the query log.
- How to see slow running queries
- How to triangulate issues which lead to high CPU usage or memory usage or I/O usage.
- Setup a multi-AZ deployment so that standby instance can be promoted as the primary instance in case of failover.
- Setup a replica and use it for read operations and for analytical queries

- How does database guarantee durability.
- What are ACID guarantees.
"""