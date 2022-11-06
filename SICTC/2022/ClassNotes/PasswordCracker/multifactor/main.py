# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "Hello World?"
answer = "hello"
my_auth.set_authentication(question, answer)

my_auth.set_authorization("admin", "ThisIsAStrongPassword123")

# start the GUI
my_auth.mainloop()
