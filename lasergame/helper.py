import math

def clamp(input, minVal = -1, maxVal = 1):
    return max(min(input, maxVal), minVal)

def clamp_angle(rads):
    if (rads < 0):
        return 2 * math.pi - rads
    elif (rads > 2 * math.pi):
        return rads - 2 * math.pi
    else:
        return rads

def rads_to_degs(rads):
    return 360 * rads / (2 * math.pi)

def degs_to_rads(degs):
    return 2 * math.pi * degs / 360