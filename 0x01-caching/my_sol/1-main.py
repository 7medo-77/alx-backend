#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache
ans_FIFOCache = __import__('1-ans_fifo_cache').ans_FIFOCache

his_cache = ans_FIFOCache()
his_cache.put("A", "Hello")
his_cache.put("B", "World")
his_cache.put("C", "Holberton")
his_cache.put("D", "School")
his_cache.print_cache()
his_cache.put("A", "Battery")
his_cache.print_cache()
his_cache.put("C", None)
his_cache.print_cache()
his_cache.put("J", "Mission")
his_cache.print_cache()

print('-'*55)
print('-'*55)
print('-'*55)

my_cache = ans_FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("A", "Battery")
my_cache.print_cache()
my_cache.put("C", None)
my_cache.print_cache()
my_cache.put("J", "Mission")
my_cache.print_cache()
