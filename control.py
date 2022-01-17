switch = 0
hold = 0
hold_count = 0
site_x = 4
site_y = 1

#passing argument
def set_switch(val):
    global switch
    switch = val
def get_switch():
    global switch
    return switch
def set_hold(val):
    global hold
    hold = val
def get_hold():
    global hold
    return hold
def set_holdCount(val):
    global hold_count
    hold_count = val
def get_holdCount():
    global hold_count
    return hold_count
def set_siteX(val):
    global site_x
    if val >= 0 and val <= 10:
        site_x = val
def get_siteX():
    global site_x
    return site_x
def set_siteY(val):
    global site_y
    if val<=20:
        site_y = val
def get_siteY():
    global site_y
    return site_y