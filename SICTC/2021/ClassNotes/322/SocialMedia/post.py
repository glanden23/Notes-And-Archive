from datetime import datetime
# declare class
# "global" variables?
# initialize an object
# string pritning format
# other methods?

class Post:
    postID = 0
    # initialize
    def __init__(self,username,message):
        # pass variables through
        self.un = username
        self.msg = message
        self.postID = Post.postID
        Post.postID+=1
        self.timestamp = datetime.now()
    
    # string printing format
    # define the string format
    def __str__(self):
        return str(self.postID) + " " + self.un + " " + self.timestamp.__str__()+": "+self.msg
    """
        def setUsername(self,username):
        self.un=username
    """
