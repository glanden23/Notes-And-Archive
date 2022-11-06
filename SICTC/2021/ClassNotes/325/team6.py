"""The function move(my_history, their_history) must return "r", "p", or "s".
my_history and their_history are strings of the same length, perhaps length zero.
"""
import random
strategy_name = 'Totally not just random'

def move(my_history, their_history):
    return random.choice(["r", "p", "s", "k", "l"])