## Python script to recover corrupted data blocks of disks in a RAID 5 (block-level striping with distributed parity)

This was part of a programming-related problem I solved for my Technical Computer Science 2 class.

```
52616e64  XXXXXXXX  204b6174  7a3a2052  7130676c
4149443a  20412050  XXXXXXXX  6a1b7b25  6e616c20
5265636f  6c6c6563  6a0f0f42  74696f6e  XXXXXXXX
486f7720  38191e13  53746f72  61676520  XXXXXXXX
33737d79  XXXXXXXX  0a537973  74656d2e  20204945
45452041  6e6e616c  XXXXXXXX  20746865  787f462e
20486973  XXXXXXXX  206f6620  3727105a  436f6d70
7574696e  672c2056  18140f67  6f6c756d  65203332
...
```

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
