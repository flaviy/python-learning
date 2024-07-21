def all_positives(nums):
    for num in nums:
        if num <= 0:
            return False
    return True