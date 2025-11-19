from typing import MutableSequence

def  selection_sort(data:MutableSequence) ->None :
    for last_unsorted_index in range(len(data)-1,0,-1):
        largest=0
        for i in range(1, last_unsorted_index+1):
            if data[i]>data[largest]:
                largest = i
        if largest==last_unsorted_index:
            continue
        else:
            data[largest], data[last_unsorted_index] = data[last_unsorted_index], data[largest]
        # print(f"End of pass {last_unsorted_index}. 'data' is now {data}")

if __name__ == '__main__':
    from array import array
    number = array('i',[20,35,-15,7,55,1,-22])
    print(f"Before sorting: {number}")
    selection_sort(number)
    print(f"After sorting: {number}")