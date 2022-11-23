def sums(items):
    # Defining the list for storing all the unique sums
    sums = [0]

    # Calculating the max sum
    max_sum = 0
    for node in items:
        max_sum += node

    # Hash table to store the unique values (faster to check whether a sum already exists)
    sum_table = [0] * (max_sum+1)

    # Variable for storing the amount of unique sums
    total = 0

    for node in items: 
        sum_list = sums.copy()
        for sum in sum_list: 
            # Checking if the sum already exists
            if sum_table[node+sum] == 0:
                sum_table[node+sum] = 1 # adding the new sum to the hash table
                total += 1 # updating the total amount of sums
                sums.append(node+sum) # add the new sum to the list
    
    return total



if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121N