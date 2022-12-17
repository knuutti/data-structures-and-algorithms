def binpack(items, S):

    bin_list = []
    

    for item in items:
        i = 0
        if len(bin_list) == 0:
            bin_list.append([item])
            continue
        while i < len(bin_list):
            if sum(bin_list[i]) + item <= S:
                bin_list[i].append(item)
                for j in range(0, i):
                    if sum(bin_list[j]) < sum(bin_list[i]):
                        bin_list.insert(j, bin_list[i])
                        bin_list.pop(i+1)
                break
            elif i == len(bin_list) - 1:
                bin_list.append([item])
                for j in range(0, i):
                    if sum(bin_list[j]) < sum(bin_list[i]):
                        bin_list.insert(j, bin_list[i])
                        bin_list.pop(i+1)
                break
            else:
                i += 1


    return bin_list


    
 
if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")

# A possible output:
#   bin 1: [9]
#   bin 2: [3, 3, 4]
#   bin 3: [6, 3]
#   bin 4: [10]
#   bin 5: [6]
#   bin 6: [8]
#   bin 7: [6]