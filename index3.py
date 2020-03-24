import time



for i in range(1, 10):
    print("Printed immediately.")
    time.sleep(i)
    print("Printed after {} seconds.".format(i))
