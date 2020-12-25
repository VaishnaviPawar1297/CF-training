def threeSum(nums):
        n = len(nums)
        nums = sorted(nums)
        
        result = []
        
        if len(nums)==0:
            
            return result
        
        elif len(nums)==1 and nums[0]==0:
            
            return result
        
        else:
            
            for i in range(n-2):
                
                l = i+1
                r = n-1
                
                while l!=r:
                    
                    total= nums[i]+nums[l]+nums[r]
                    
                    if total==0 and [nums[i],nums[l],nums[r]] not in result:
                        
                        result.append([nums[i],nums[l],nums[r]])
                    
                    elif total<0:
                        
                        l=l+1
                    else:
                        
                        r=r-1
            
            return result

nums = [-1,0,1,2,-1,-4]
threeSum(nums)

