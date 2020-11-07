#Serving as an introductory task in my first python class, 
#this python code simply swaps between the cheese and citites values using placeholders
def swap(b,h,k):
    placeholder = b[h]
    b[h]= b[k]
    b[k]= placeholder
    return b
cheese = ['Brie','Cheddar','Gruyere','Asiago']
cities = ['DC','New York','San Francisco']

print(swap(cheese,0,3))
print(swap(cities,1,2))
    
    
