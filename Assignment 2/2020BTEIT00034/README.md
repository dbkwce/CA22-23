# Vector Quantization (VQ) Algorithm along with Huffman Coding
## Author: Daulatrao Patil - 2020BTEIT00034
## Date: 08/08/2022
## Reference:
- [GeeksForGeeks](https://www.geeksforgeeks.org/learning-vector-quantization/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)
- [Wikipedia](https://en.wikipedia.org/wiki/Vector_quantization)
- [Github](https://github.com/topics/vector-quantization)
---
### Implementing in Python

Tested with Python 3.9.5
Vector Quantization algorithm is nearly identical to K-Nearest Neighbour(KNN) algorithm expect that it uses a smaller, trained codebook instead of a large, unlabeled dataset.

Three different methods intialization methods are used for VQ algorithm:
-   _random_ : Initialize with random values
-   _zeros_ : Initialize with all zeros
-   _dataset sample_ : Initialize by picking a vector from the dataset

### Images used:
- _Training_: img\input\Daulatrao-Patil-BW.bmp
- _Test_: img\input\Daulatrao-Patil-BW-Reszied.bmp

### Output:
- _Output image_: img\output\Daulatrao-Patil-BW-VQ.bmp

### Compression ratio:
- _Compression ratio_: It was near to 80% of the original image size i.e. 0.8. The size of original image was around 3 MB and compressed image size is around 0.5 MB (512 KB exact).