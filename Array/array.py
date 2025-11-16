from array import array
int_array = array('l', [0] * 7)


int_array[0] = 20
int_array[1] = 35
int_array[2] = -15
int_array[3] = 7
int_array[4] = 55
int_array[5]= 1
int_array[6] = -22
print(int_array)
print('-'*80)
for i in range(len(int_array)):
    print(int_array[i])

    
print('-'*80)

print(int_array.itemsize)

print('-'*80)


found_index=-1
for i in range(len(int_array)):
    if int_array[i]==7:
        found_index=i
        break
print(f"The index of value 7 is {found_index}")