import unittest
def Two_Sum(nums, target):
    if(all([isinstance(i,int) for i in nums]) and (target in range(-109,110) )and (len(nums) in range(2,105)) and max(nums)<=109 and min(nums)>=-109 ):

        keep = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in keep:
                return [keep[key], i]
            else:
                keep[nums[i]] = i
        return False
    return False

class TestNumber(unittest.TestCase):
   def test_two_sum_1(self):
        test = Two_Sum([2,7,11,15],9)
        result = [0,1]
        self.assertEqual(result,test)

   def test_two_sum_2(self):
        test = Two_Sum( [3,2,4],6)
        result = [1,2]
        self.assertEqual(result,test)

   def test_two_sum_3(self):
        test = Two_Sum([3,3],6)
        result = [0,1]      
        self.assertEqual(result,test)

        #test constraint 2 <= nums.length <= 104 

   def test_two_sum_4(self):
        test = Two_Sum(list(range(0,150)),6)
        result = False 
        self.assertEqual(result,test)
    
   def test_two_sum_5(self):
        test = Two_Sum([1],1)
        result = False 
        self.assertEqual(result,test)

        
        #test not found two sum
   def test_two_sum_6(self):
        test = Two_Sum([1,2],6)
        result = False 
        self.assertEqual(result,test)


        #test constraint -109 <= nums[i] <= 109
   def test_two_sum_7(self):
        test = Two_Sum([2000,1,3],4)
        result = False 
        self.assertEqual(result,test)

   def test_two_sum_8(self):
        test = Two_Sum([-2000,1,3],4)
        result = False 
        self.assertEqual(result,test)
        
        #test constraint -109 <= target <= 109
   def test_two_sum_8(self):
        test = Two_Sum([109,0,1],110)
        result = False 
        self.assertEqual(result,test)

   def test_two_sum_8(self):
        test = Two_Sum([-110,0,1],-110)
        result = False 
        self.assertEqual(result,test)

if __name__ == '__main__':
     unittest.main()