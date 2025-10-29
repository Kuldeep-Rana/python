try:
    c , d = 120, 0
    print(c/d)
except(ZeroDivisionError):
    print("can't do it with zero")
finally:
    print("why don't you try it with number > 0")    


    