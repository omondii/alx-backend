Background Context

In this project, you learn different caching algorithms.
Resources

Read or watch:

    Cache replacement policies - FIFO
    Cache replacement policies - LIFO
    Cache replacement policies - LRU
    Cache replacement policies - MRU
    Cache replacement policies - LFU

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What a caching system is
    What FIFO means
    What LIFO means
    What LRU means
    What MRU means
    What LFU means
    What the purpose of a caching system
    What limits a caching system have


A caching system - a mechanism that stores frequently accessed data in a cache(storage space).
A cache is much faster to access than the original data source hence reduced response times. 
<u> Caching Systems </u>
-> Refers to a component used to store copies of frequently accessed data in a cache. 
1. <b> FIFO </b>
-> A cache replacement mechanism where the oldest items are removed first when the cache reaches its max capacity

2. <b> LIFO </b>
-> Removes the recently added items when the cache is full. Last item added is removed first

3. <b> LRU </b>
-> /*Least Recently Used*/ - removes the least recently used item when the cache is full. 
-> Assumes that data that hasn't been used is less likely to be accessed soon

4. <b> MRU </b>
-> /*Most Recently Used*/ - removes the most recently used items from the cache when it is full. 
-> Assumes the most recently used is more likely to be accessed again soon
 