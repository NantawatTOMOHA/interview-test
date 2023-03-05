import unittest
def rotate( Array, k) :
            if(all([isinstance(i,int) for i in Array]) and (k in range(0,101) )and (len(Array) in range(0,101)) and max(Array,default = 0)<=1000 and min(Array,default = 0)>=-1000 ):
                if(len(Array)==0):return Array
                k = k % len(Array)
                Array.reverse()
                Array[:k] = reversed(Array[:k])
                Array[k:] = reversed(Array[k:])
                return Array
            return False


class TestNumber(unittest.TestCase):
   def test_rotate_1(self):
        test = rotate([1,2,3,4,5,6],2)
        result = [5,6,1,2,3,4]
        self.assertEqual(result,test)
    
   def test_rotate_2(self):
         test = rotate([1,2,3,4,5,-1000],2)
         result = [5,-1000,1,2,3,4]
         self.assertEqual(result,test)

   def test_rotate_3(self):
         test = rotate([1,2,3,4,5,1000],2)
         result = [5,1000,1,2,3,4]
         self.assertEqual(result,test)

        # A[-1000,1000]
   def test_rotate_4(self):
         test = rotate([1,2,3,4,5,-1001],2)
         result = False
         self.assertEqual(result,test)

   def test_rotate_5(self):
         test = rotate([1,2,3,4,5,1001],2)
         result = False
         self.assertEqual(result,test)

   def test_rotate_6(self):
         test = rotate([1,2,3,4,5,1000],0)
         result = [1,2,3,4,5,1000]
         self.assertEqual(result,test)

         ### k[0,100]
   def test_rotate_7(self):
         test = rotate([1,2,3,4,5,1000],101)
         result = False
         self.assertEqual(result,test)

   def test_rotate_8(self):
         test = rotate([1,2,3,4,5,1000],-1)
         result = False
         self.assertEqual(result,test)

   def test_rotate_9(self):
         test = rotate([1,2,3,4,5,6],0)
         result = [1,2,3,4,5,6]
         self.assertEqual(result,test) 

   def test_rotate_10(self):
         test = rotate([1,2,3,4,5,6],100)
         result = [3,4,5,6,1,2]
         self.assertEqual(result,test)

         ### n[0,100]
   def test_rotate_11(self):
         test = rotate(list(range(0,100)),0)
         result = list(range(0,100))
         self.assertEqual(result,test)

   def test_rotate_12(self):
         test = rotate([],0)
         result = []
         self.assertEqual(result,test)

   def test_rotate_13(self):
         test = rotate(list(range(0,101)),0)
         result = False
         self.assertEqual(result,test)
  
if __name__ == '__main__':
       
      
        unittest.main()

    
