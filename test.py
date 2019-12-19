def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

lis = [1,2,3]
test_var_args('yasoob', *lis)

def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print (key, "=", value) 
  
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')     