try:
    raise Exception("you are ded")
except Exception as error:
    print(error)
else:
    print("you are alive")
finally:
    print("reborn again")