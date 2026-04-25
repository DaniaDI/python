Custom HashMap Implementation (Python):

This repository contains a manual implementation of a HashMap (Hash Table) from scratch using Python.
 It demonstrates the fundamental concepts of data structures, focusing on efficiency and collision management.

📌 Overview:
The goal of this implementation is  the behavior of Python's built-in dict. It allows storing data in Key-Value pairs, ensuring that data retrieval is optimized using a hashing mechanism.

🚀 Features:
The MyHashMap class supports the following standard operations:
put(key, value): Inserts a (key, value) pair into the HashMap. 
If the key already exists, the value is updated.
get(key): Returns the value to which the specified key is mapped, or -1 if the map contains no mapping for the key.remove(key): Removes the mapping for a specific key if it exists.

🛠️ Technical:
Hash Function: A simple modulo operator ($key % size) to map large keys into a fixed-size array of 1,000 buckets.Collision Handling 
Separate Chaining :
  Since different keys might result in the same hash index, each bucket stores a List (chain). This allows multiple key-value pairs to coexist at the same index without overwriting each other.