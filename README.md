### Python script to recover corrupted data blocks of disks in a RAID 5 (block-level striping with distributed parity)

This was part of a programming-related problem I solved for my Technical Computer Science 2 class.

For instance for line 1 of `data.txt`
```
52616e64  XXXXXXXX  204b6174  7a3a2052  7130676c
...
```
the script will recover the content for the `XXXXXXXX` block:
```
x_block of line 1 = 7920482e
...
```
by performing the "bitwise XOR" for the integers at the indexes of each block.

For the first character of each block that would be `X = 5 ^ 2 ^ 7 ^ 7 = 7`
