#Are you ready for school?
#Setup checklist

readyList = []
questionList = []
# ask user what they need to do and set it in the question list and ready list.
print("What do you need to do today?")
ui = input(">>> ")
while ui!= "quit":
    questionList.append(ui)
    readyList.append(False)
    ui = input("What do you need to do today? (quit to end) >>> ")

# Keep asking questions until all are answers as done.
while(False in readyList):
    #i loops through questions
    i=0
    while(i<len(questionList)):
        # if ready is false, ask if they did it.
        if (readyList[i]==False):
            ui=input(f"Did you {questionList[i]}? >>> ")
            # if they say yes, set it as done.
            if ui=="y":
                readyList[i]=True
        i+=1
print("You are ready!")