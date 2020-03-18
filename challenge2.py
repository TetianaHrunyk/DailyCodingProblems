def multiply(myList) : 
    result = 1
    for x in myList: 
         result = result * x  
    return result  

def product(inlist: list) -> list:
    length = len(inlist)
    product = multiply(inlist)
    outlist = [product for i in range(length)]
    for i in range(length):
        product[i] /= inlist[i]
        
    return product
        