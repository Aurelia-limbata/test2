class Test:

    def pri(self, a):
        if a == 1:
            print(1)
        
        if a != 1:
            print("This is %f, not 1" % a)

a = input("input any number!\n")
test = Test()
test.pri(a)
