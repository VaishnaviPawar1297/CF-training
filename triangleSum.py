triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

result = [None] * len(triangle)
n = len(triangle) - 1
      
for i in range(len(triangle[n])):       
    result[i] = triangle[n][i]
   
    
for i in range(len(triangle) - 2, -1,-1):
   
    for j in range( len(triangle[i])):
      
        result[j] = triangle[i][j] + min(result[j], result[j + 1])
        
  
print(result[0]) 
        
