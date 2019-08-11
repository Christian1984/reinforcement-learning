def clamp(input, minVal = -1, maxVal = 1):
    return max(min(input, maxVal), minVal)