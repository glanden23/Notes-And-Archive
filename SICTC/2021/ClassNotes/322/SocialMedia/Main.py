#
# Dependencies
#
from post import Post
allPostArchive = []

print("Welcome to THE BookFace!")
username = input("What is your username? >>> ")
userInterface="""
What would you like to do?
"add" - Add a post to the archive.
"remove" - Remove a post from the archive.
"change user" - Change the user name associated with any future posts.
"print" - Dispaly the current up to date list of all posts.
"quit" - End the program.
"""
print(userInterface)
UI = input(">>> ").lower()
#
# User input loop
#
while UI != "quit":
    if UI == "add":
        UI = input("What is your message? >>> ")
        post=Post(username, UI)
        allPostArchive.append(post)
    elif UI == "remove":
        id=int(input("Which post do you want to delete? >>> "))
        for i in range(len(allPostArchive)):
            if allPostArchive[i].postID == id:
                del allPostArchive[i]
                break
    elif UI == "change user":
        username = input("What is your username? >>> ")
    elif UI == "print":
        for post in allPostArchive:
            print(post)
    print(userInterface)
    UI = input(">>> ").lower()
print("Goodbye!")