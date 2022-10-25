# Pixels and Images

*Borrowed and modified with permission from Prof. Straubing*

The images that you will work with are made up of rows and columns of "pixels".  You have heared of pixels before, both because cameras are often described in terms of the megapixels they can capture and because you know what it means when an image looks "pixelated". 

Each pixel is represented by 3 components: one red, one green, and one blue. Each component has a value ranging from 0 to 255. (Why this range? It's because each pixel stores one byte of information, which is 8 bits, where each bit can be 0 or 1, so there are 256 (2^8) possible values for each of the three components. We will learn more about bits and bytes at the end of the semester.) 

A pixel with red, blue and green components (255,255,255) is white; (255,0,0) is pure bright red; (0,255,0) is pure green; (0,0,255) is pure blue; and (0,0,0) is black; (0,255,255) is a bluish-green; and (128,128,128) is a medium gray.

Without importing new modules in Python, there's no special data structure specifically for grid-like row/column data (which you might hear called a "matrix", a "2D array"), but we can create something that works pretty well by having a **list of lists**, just like we have talked about in class. For example, if you imagine data you want to store in a row/column format (which I will start calling a "matrix" here) like a spreadsheet:

```
4    5    9
2    3    7
1    4    5
2    0    6
```

would be represented in Python by this list of lists:

```
mymatrix = [ [4,5,9], [2,3,7], [1,4,5], [2,0,6]]
```

Recall from class how we access different elements in a list of lists:

```
# second row of the list (i.e., [2, 3, 7])
mymatrix[1]

# third element of second row (i.e., 7)
mymatrix[1][2]

# number of rows
len(mymatrix)

# number of columns
len(mymatrix[0])

```

In the case of our images, each pixel is itself represented by *another* list of length three: one value for red compnent, one for the green, and one for the blue. This makes our images *three-dimensional* lists. For example, a (very tiny) image that is 4 pixels high and 3 pixels wide might be represented by 

```
myimage = [ [ [255,255,  0], [255,255,0], [255,255,0]],
            [ [255,128,  0], [255,128,0], [255,128,0]],
            [ [  0,255,  0], [  0,128,0], [  0,  0,0]],
            [ [ 50,100,200], [255,255,0], [127,  0,0]]  ]
```

If you wanted to change all of the components of the pixel in the first row, second column to 255 to make that pixel white, you could do this:

```
myimage[0][1] = [255, 255, 255]
```


Now that you know a little more about pixels and how they work, you can [go back to the problem set](https://github.com/CSC1-1101-TTh9-S21/ps7/blob/main/README.md#step-4-write-the-greyscale-function).
