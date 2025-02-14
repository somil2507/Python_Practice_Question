def decorators(func):

    def wrraper():
        print("Transaction Initiated")

        func()

        print("Trasaction Completed")

    return wrraper

def transaction():

    print("Executing all the steps....")

tran = decorators(transaction) 

tran()