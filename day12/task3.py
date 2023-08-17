# Create a new list of repeated items from a provided list:
# nums = [3, 4, 2, 2, 1, 3, 3, 3]
# Output = [3, 2]

nums = [3, 4, 2, 2, 1, 3, 3, 3]
result = []
for each in nums:
    if nums.count(each) > 1 and each not in result:
        result.append(each)

print(result)
