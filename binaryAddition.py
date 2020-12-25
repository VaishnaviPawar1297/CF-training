a = "1001"
b = "1100"

result = ""
carry = 0 
val = 0
        
for i in range(max(len(a),len(b))):
            
    val = carry

    if i < len(a):
                
        val = val + int(a[-(i+1)])
                
    if i < len(b):
                
        val = val + int(b[-(i+1)])
                
    carry = val//2
            
    val = val%2
            
    result += str(val)
            
if carry:
            
        result = result + "1"
        
print(result[::-1])