# Author: Christian Palacios
# 
# 
# Date: 10/05/2024
#
#
# Version: 1.0.0
#
#
# Availability: https://github.com/chris-palacios/School-Projects/tree/main/Image_Comparison
#

def list_to_bin(arr: list)->str:
    binary = ''
    for element in arr:
        binary = binary + str(element)
    return binary

def calc_cost(num1:str, num2:str) -> int:
    #Using XOR to flip bits to true that are not a match then returning the cost to change
    num1 = int(num1,2)
    num2 = int(num2,2)
    return bin(num1 ^ num2).count('1')

def sum(image:list)->int:
    # if the image is empty return 0 since there is no cost
    if len(image) == 0:
        return 0
    #check to see if it is a 2D array to multiply row * column 
    if isinstance(image[0], list):
        return (len(image) * len(image[0]))
    #if not return the length of the array
    else:
        return len(image)

def main(image1:list[list[int]],image2:list[list[int]])->list[list]:
    
    len1 = len(image1)
    len2 = len(image2)

    #Base case for if one image is empty and the other is not
    if (len2 == 0  or len1 == 0 ):
        if(len2 == len1):
            return [[]]
        #returns the size of the array that is not empty since all bits need to be changed
        temp = (len1 * len(image1[0])) if len2 == 0 else (len2 * len(image2[0]))
        D = [temp]
        return D
    
    #set the DP array to be the 
    D = [[0 for i in range(len1 +1)] for j in range(len2 +1)]
    
    for i in range(len1 + 1):
        D[0][i] = sum(image1[0:i])
    for j in range(len2 + 1):
        D[j][0] = sum(image2[0:j])
    
    
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            #comparing each row bit by bit. 
            if (image1[j-1]==image2[i-1]):
                cost = 0
            else:
                cost = calc_cost(list_to_bin(image1[j-1]), list_to_bin(image2[i-1]))

            D[i][j] = min(
                D[i-1][j-1] + cost,
                D[i-1][j] + cost,
                D[i][j-1] + cost
            )

    for row in D:
            print(row)


    return D
            
if __name__ == '__main__':
    image1= [[0,1,1],
             [0,1,0],
             [1,0,0]]
    
    image2= [[0,0,1],
             [1,1,0],
             [1,0,1]]
    main(image1,image2)
