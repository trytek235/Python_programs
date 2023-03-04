import sys, time

indent = 1
indentationRise = True

while(True):
    try:
        if(indentationRise):
            time.sleep(0.01)
            print(' '*indent + "********")
            indent += 1
            if(indent>=60):
                indentationRise=False
        elif(indentationRise==False):
            time.sleep(0.01)
            print(' ' * indent + "********")
            indent -=1
            if(indent<=0):
                indentationRise = True
    except(KeyboardInterrupt):
        sys.exit()
