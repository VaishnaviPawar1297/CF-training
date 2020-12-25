triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
n = len(triangle)

i = 0
for j in range(i+2):
    #print("j = ", j)
    for k in range(j,j+2):
        #print("j = ", j)
        #print("k = ", k)
        for l in range(k,k+2):
            #print("k = ", k)
            #print("l = ", l)
            print(str(triangle[0][i])+','+str(triangle[1][j])+','+str(triangle[2][k])+','+str(triangle[3][l]))