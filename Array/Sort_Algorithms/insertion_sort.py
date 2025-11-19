from typing import MutableSequence

def insertion_sort(data:MutableSequence):
    for first_unsorted_index in range(1,len(data)):
        new_element = data[first_unsorted_index]
        
        i = first_unsorted_index - 1
        while i>=0 and data[i]>new_element:
            data[i+1]=data[i]
            i-=1
        data[i+1]=new_element
        # print(f"End of pass {first_unsorted_index}. 'data' is now {data}")
         


if __name__ == '__main__':
    from array import array
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])
    # numbers = array('i', [8,1,2,3,91,5,6,7])
    

    print(f"Sorting {numbers}")
    insertion_sort(numbers)
    print(f"The sorted data is {numbers}")