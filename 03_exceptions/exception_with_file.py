class FileOps:
    

    def readUserInput(self):
        print("write what you want to say")
        while(True):
            inputs = input("")
            if inputs == "Q":
                break
            try:
                #with open("user_input.txt") as file: # this will cause - No such file or directory: 'user_input.txt'
                with open("user_input.txt", "a+") as file: # lets add a+ mode in it,should work now, you can toggle these two lines
                    file.write(inputs)
            except Exception as e: 
                print(e)
                print("something went wrong")   


ops = FileOps()
ops.readUserInput()