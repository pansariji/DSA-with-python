from typing import MutableSequence

def shell_sort(data:MutableSequence):
    n = len(data)
    #for initial gap
    gap=1
    while gap<n//3:
        gap = gap*3+1
    # gap = n//2
    while gap>0:
        # print(gap, end=",")
        for i in range(gap, n):
            new_element=data[i]

            j=i
            while j >= gap and data[j-gap]>new_element:
                print(f"\twriting {data[j-gap]} to position {j}")
                data[j]=data[j-gap]
                j-=gap
            print(f"storing {new_element} to position {j}")
            data[j]=new_element
        print(f"end of the pass {gap}. data is now {data}")
        gap//=3
        # gap//=2


if __name__ == '__main__':
    from array import array
    data = array('i',[20,35,-15,7,55,1,-22])
    shell_sort(data)
    print("the sorted data is", data)