switch = 0

def go(event):
    global switch
    if((event.x>=98) and (event.x<=256) and (event.y>=194) and (event.y<=244) and (switch == 0)):
        switch = 1

def rotate(event):
    pass

def drop(event):
    pass

def left_shift(event):
    pass

def right_shift(event):
    pass

def set_block(event):
    pass

def hold_block(event):
    pass

#argument transport
def set_switch(val):
    global switch
    switch = val
def get_switch():
    global switch
    return switch