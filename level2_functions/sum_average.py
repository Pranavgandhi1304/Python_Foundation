# function 
def sum_and_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total = total + num
        count = count + 1
    average = total / count
    print("DEBUG: total =", total, "average =", average)
    return total, average

# Main part
nums = [10, 20, 30, 40, 50]
result_sum, result_avg = sum_and_average(nums)
print("Sum:", result_sum)
print("Average:", result_avg)