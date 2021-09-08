#NUMPY
arrays = '''
Arrays :- jes me ek he trhe ke datatype ke vaue ho
eg. [1,2,3,4,5] , ["a","d","w"] , [1.223,2.56,5.133] 
               
               TYPES
    1>.1-D(Vector)            2>.Multidimansional (Matrices) / 2-D,3-D etc
eg.[1,2,3,4,55,3]              eg.[[1,2,3,4]
                                   [5,6,7,8]
                                   [9,10,11,12]]



'''
arrays_creation = ''' 

----------------------------------- Creating arrays ----------------------
        
       =============                        |                    ============================
      ||1-D(Vector)||                       |                   ||Multidimansional (Matrices)|| / 2-d,3-detc
       =============                        |                    =============================
                                            |
.From python data                           |
-----------------                           |
                                            |
import numpy as np                          |                    import numpy as np
l = [1,2,3,4]                               |                    l1 = [1,2,3,4]
array = np.array(l)                         |                    l2 = [5,6,7,8]
print(array)                                |                    array = np.array([l1,l2])
                                            |                    print(array)
--------------------------------------------|----------------------------------------------------------
.Alternative methods for making array       |
-------------------------------------       |
                                            |
1>.fromiter()  2>.arange()   3>.linspace()  | 4>.empty()  5>.zeroes()  6>.ones()  7>.eye()  8>.full() 
9>.random.rand()  10>.random.randint()      |
                                            |
1>.fromiter()                               |
import numpy as np                          |
dic = {1:"a",2:"b",3:"c"}                   |
x = np.fromiter(dic,dtype = np.int32)       |
print(x)                                    |
                                            |
2>.arange()                                 |
arange(starting value,ending value,gap)     |
optional thing:-dtype,axisetc               |
                                            |
importing                                   |importing
x = np.arange(3,10,1,dtype = np.float32)    |x = np.arange(6)#0-5 tak number
print(x)                                    |x = x.reshape(2,3)# (2,3) = size
                                            |
3>.linspace                                 |
linespace(startval,endval,no.ofElementWant) |
importing                                   |
x = np.linspace(3.5,10,3,dtype=np.int32)    |
                                            |
4>.empty()                                  |
                                            |make random number array
                                            |x = np.empty([3,5],oder = "f")
                                            |Note:-
                                            |"f"=contiguous order-row
                                            |"c"=fortran order-column
5>.zeroes()                                 |
creat array with element "0"                |x = np.zeroes([3,5],order = "f")
6>.ones()                                   |
creat array with element "1"                |x = np.ones([3,5])
                                            |
7>.eye()                                    |
creat nxn array with diganouly element "1"  |x = np.eye(5)
                                            |
8>.full()                                   |
make array with same element                |x = np.full([3,5],"a")
                                            |
9>.random.rand()                            |
make arrray with float element              |x = np.random.rand(3,5)
                                            |
10>.random.ranint()                         |
make array with int element                 |x = np.random.randint(1,20,size=(3,5))
                                            |
----------------------------------------------------------------------------------------------------------
'''

arrays_concept = '''
1>.Axis
numpy array ke dimansion
no. of dimansion == no. axis
axis0 = 1d , axis1 = 2detc
axis = 0(row / horizontal)-->
axis = 1(column / vertical)|
                           v

2>.Rank                 3>.Shape                                    4..itemsize
no of axis              no of elements in array                     size of each element in byte
1D array = [0]          -----------------------
2D array = [0,1]        <shape kase likhte hai>
                        -----------------------
                        1D = (3,)
                        2d = (no of list , no of element in list)

5>.dtype 
tell type of data
dtype=float , int8.32.64 etc
'''

arrays_accisses = '''

---------------------------Accessing arrays elemnt-------------------------------
1>.Slicing      2>.functions :-hsplit() vsplit() extract() split()

==========
1>Slicing
==========
          1D                                |                       2d
same as stirng sclicing                     |
[starting , ending ,steps]                  |[numbr of list slicing , no of elment sclicing]
eg.                                         |eg.
[::]                                        |[0:3 , 1:]
                                            |
==============                              |              
2>.By function                              |
==============                              |
-> hsplit()                                 |
split horizontaly                           |x = np.array([[1,2,3,7] , [6,7,8,4]])  
                                            |y = np.hsplit(x,2)  
                                            |
-> vsplit()                                 |
split vertically                            |x = np.array([[1,2,3,7] , [6,7,8,4]]) 
                                            |y = np.vsplit(x,2)  
                                            |
->split()                                   |
x = np.array([1,2,3,4,5,6,7,8])             |x = np.array([1,2,3,4][5,6,7,8]]) 
y = np.split(x,2)                           |y = np.split(x,[2,5],axis=0)
           or                               |
y = np.split(x,[2,5])                       |
                                            |
->extract()                                 |
split data from list when condition statisfy|x = np.array([1,2,3,4][5,6,7,8]]) 
                                            |condition = np.mod(x,3)==0
                                            |y = np.extract(condition,x)               
----------------------------------------------------------------------------------------------
'''
arrays_attributes = '''
--------------------------------------Some arrays attribute-----------------------------------------------
we can do arthmetic proccess in array                                                                    |
x = np.array([1,2,3,4][5,6,7,8]])                                                                        |
y = x+1                                                                                                  |
                                                                                                         |
----------------------------------------------------------------------------------------------------------
======                   |=======                    |========               |=========                  |
1.flat|                  |2.ndim                     | 3.nbytes              |4.aragmax                  |  
======                   |=======                    |========               |=========                  |
to mak array itreabel    | to print no. of dimansion | to print size of all  |ye hame max no. ke janghae |                
for item in x.flat:      |                           |element consuming data |bataye ga                  |
       print(item)       |                           |                       |                           |
                         |print(x.ndim)              |print(x.nbyte)         |print(x.aragmax)           |    
                         |                           |                       |                           |
                         |                           |                       |                           |

=========
5.where()
=========
agar ham us jagaha ka naumber to condtion ko statisfiye kerta hai
y = where(x>4)
----------------------------------------------------------------------------------------------------------------
'''

arrays_concat = '''
hstack() vstack() concate
l1 = [1,2,3]
l2 = [6,5,7] 
l3 = [6,4,5] 

la = np.array([[1,2,3],[6,5,7]])
la1 = np.array([[6,4,5],[6,5,7]])
             1D                                   |          2D
                                                  |
->hstack                                          |
y = np.hstack((l1,l2,l3))                         |y = np.hstack((la,la1))
                                                  |
->vstack                                          |
y = np.vstack((l1,l2,l3))                         |y = np.vstack((la,la1))
                                                  |
->concate                                         |
y = x.concatenate((l1,l2,l3),axis = 0)            |
                                                  |
--------------------------------------------------------------------------------------------------------
'''

arrays_transpos = '''
jab ham transpose ka use kerte hai hai to us me ek oe list add ho jate hai
ye matris ko transpose ker dega 
 row ko column me or 
 column ko row mw
T
l1 = np.array([[1,2,3],[6,7,8],[3,2,4]])
l2 = np.array([[3,6,2],[7,5,8]])
cl = np.concatenate((l1,l2.T),axis=1)
print(cl)
'''

info = '''\n.......................................ENTER  NUM  FOR TUTUORIAL YOU WANT...................................\n\n
0-Full numpy   1-Array creation  2-Array concept  3-Array concept  4-Array accisses  5-Array concat  6-Array attributes  7-Array transpose
'''
import time
while True:
       print(info,"\n")
       user_input = int((input("Enter what you want to learn in NUMPY")))
       time_input = int(input("Time for Reading in sec"))
       if user_input == 0:
              print(f"{arrays}\n")
              time.sleep(time_input)
              print(f"{arrays_creation}\n")
              time.sleep(time_input)
              print(f"{arrays_concept}\n")
              time.sleep(time_input)
              print(f"{arrays_accisses}\n")
              time.sleep(time_input)
              print(f"{arrays_attributes}\n")                  
              time.sleep(time_input)
              print(f"{arrays_concat}\n")
              time.sleep(time_input)              
              print(f"{arrays_transpos}")
              #{time.sleep(5)}
              time.sleep(time_input)

       if user_input == 1:
              print(f"{arrays}\n")
              time.sleep(time_input)

       if user_input == 2:
              print(f"{arrays_creation}\n")
              time.sleep(time_input)

       if user_input == 3:
              print(f"{arrays_concept}\n")
              time.sleep(time_input)

       if user_input == 4:
              print(f"{arrays_accisses}\n")
              time.sleep(time_input)

       if user_input == 5:
              print(f"{arrays_attributes}\n")
              time.sleep(time_input)
       if user_input == 6:
              print(f"{arrays_concat}\n")
              time.sleep(time_input)

       if user_input == 7:
              print(f"{arrays_transpos}\n")
              time.sleep(time_input)