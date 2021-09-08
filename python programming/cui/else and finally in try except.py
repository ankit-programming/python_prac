#introduction to finally
try:
    f = open("any file name.txt")
except Exception as e:
    print(e)

else:
    print("in else")
#else will run oly if Exception run


finally:
    print("Run this anyway..")
#code written in this will run defenetly


