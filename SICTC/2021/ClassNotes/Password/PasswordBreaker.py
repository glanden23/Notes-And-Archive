import datetime
def passwordBreakerIntVersion():
    passwordToCheck = 123456
    beginTime = datetime.datetime.now()

    cpuGuess = 0

    while cpuGuess != passwordToCheck:
        cpuGuess+=1
    print(f"Got it!: {cpuGuess}")
    print(datetime.datetime.now() - beginTime)