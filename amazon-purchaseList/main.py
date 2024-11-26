purchase_list = [12,12,34,34,34,89]

purchase_list_2 = sorted(set(purchase_list))
print("Unique list: ", purchase_list_2)
print("--------------------------------------------------------")
####################################################################
#### Timpe Complexity:
# Set moves through all the list
# Each insertion is O(1)
# So the time complexity is O(n)

# Sorted uses Timsort which has a time complexity of O(m log m)

## Final Time Complexity = O(n)+ O(m log m)

####################################################################

### Space Complexity:
# Set uses O(n)
# Sorted uses O(n)

## Final Space Complexity = O(n)

####################################################################
def remove_duplicates_in_place(arr):
    if not arr:  # Handle edge case for empty array
        return arr, 0

    i = 0  # Pointer for the position of unique elements

    for j in range(1, len(arr)):
        print("\nArray at iteration %s: %s" % (j, arr))
        if arr[j] != arr[i]:  # Found a new unique element
            print("Found a new unique element:", arr[j])
            print("i:", i, "j:", j)
            i += 1
            arr[i] = arr[j]  # Move it to the next position in the array
        else:
            print("Found a duplicate element:", arr[j])
            print("i:", i, "j:", j)
    return arr, i + 1  # i + 1 is the count of unique elements

result = remove_duplicates_in_place(purchase_list)
print("Modified array and unique count:", result)
