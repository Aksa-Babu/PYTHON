def longestLength(a):
    max1=len(a[0])
    temp=a[0]
    for i in a:
        if(len(i)>max1):
            max1=len(i)
            temp=i
    print("THe word with the longest length is:",temp,"amd length is",max1)
a=["one","two","three","four"]
longestLength(a)