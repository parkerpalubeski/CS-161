#CS 161 Week 2 Assignment

#Part 1
x = 31
print(f"{bin(x)}, {x}")
#The example showed binary, decimal and hex, but the question only asked for binary and decimal


#Part 2 (1st part commented so the program still runs; part of the question was to produce an error)

#y = 1.825
#print(bin(y))
#The error given is "TypeError: 'float' object cannot be interpreted as an integer"
#It does this because the bin function works with integer numbers, but doesn't account for floating point notation in binary

x = 18

#Part 3
y = 0b1011
z = 0xA3

print (y,z)

#Part 4

w = x + y + z
print(f"The sum is {w}")

#Compression

original_size = 240
dictionary_size = 25
compressed_text_size = 148
total = compressed_text_size + dictionary_size
compression_ratio = float((1.0 - (total / original_size))*100)

print(f"Compressed text size: {compressed_text_size}")
print(f"    Dictionary size: {dictionary_size}")
print(f"        Total: {total}")
print(f"  Original text size: {original_size}")
print(f"    Compression: {compression_ratio:.2f}%")

