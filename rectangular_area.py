"""
    Author:      Piotr Lasek
    Date:        23 November 2019
    Description: A solution for the "Largest Rectangular Area in a Histogram" 
                 problem
"""


# ----------------------------------------------------------------------------- 

def plot_hist(h):
    for i in range(max(h)):
        for j in range(len(h)):
            if max(h)-i > h[j]:
                print('  ', end='')
            else:
                print('x ', end='')
        print()
    for j in range(len(h)):
        print("--", end='')
    print()
    for j in range(len(h)):
        print("{} ".format(j), end='')
    print()
    print()

# ----------------------------------------------------------------------------- 

def max_area(h):
    areas = []

    for x in range(len(h)):
        area = 0
        max_y = h[x]

        for y in h[x:]:
            if y < max_y:
                break
            area += max_y
        
        for y in reversed(h[0:x]):
            if y < max_y:
                break
            area += max_y

        areas.append(area)

    return max(areas)

# ----------------------------------------------------------------------------- 

h = [1, 3, 2, 6, 5, 3, 20, 0, 10]
plot_hist(h)

a = max_area(h)
print("Largest rectangle: {}".format(a))
