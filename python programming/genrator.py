#genrator
'''
Itarabel-vo python object jes me __iter__() & __getitem__() defin hote hai
Itrator- agar ham itrabel run karenge to hame itrator milega jes me __next__() dfin hoga
Itration- es itrat kerne ke process ko itration khate hai

'''

#gnrator:- ye ek thre ke itrator hote hai jenshe ham sirf ek bar itrat ker sakte hai
#eg :- range be ek thre se genrator hai

#eg of simple genrator jo at the moment jij ko banata hai
'''for i in range(10):
    print(i)'''

#making own genrator
#agar hame n No. tak no baneae hai to ham genrator ka use karenge take n No. tak No. memory me rahe or jab hame use jarutrat
#hoge tabe ham use use kere itrator ke madad se
#practis to make fimoniche seris and factorial
def gen(a):
    for i in range(a):
        yield i

g = gen(100)
#if we want to print No.
print(g.__next__())

#ager hame kese object ko iterabel banaahai to ham __iter__() ka use kerenge(jase int iterabel nahi hota str hota hai)
#str
s = "ankit"
#making str iterabel
itr = iter(s)
print(itr.__next__())



