print("How much change? (enter stop to quit)")
UI = input(">>> ")
while UI != "stop":
    UI = float(UI)
    UI = UI * 100
    quarter = 0
    dime = 0
    nickle = 0
    penny = 0
    while UI - 25 >= 0:
        UI-= 25
        quarter+=1
    while UI - 10 >= 0:
        UI-= 10
        dime+=1
    while UI - 5 >= 0:
        UI-= 5
        nickle+=1
    while UI - 1 >= 0:
        UI-= 1
        penny+=1
    if quarter == 1:
        qT = ""
    else:
        qT = "s"
    if dime == 1:
        dT = ""
    else:
        dT = "s"
    if nickle == 1:
        nT = ""
    else:
        nT = "s"
    if penny == 1:
        pT = ""
    else:
        pT = "s"
    print(f"""
{quarter} Quarter{qT}
{dime} Dime{dT}
{nickle} Nickle{nT}
{penny} Pennie{pT}
          """)
    UI = input(">>> ")
print("Goodbye.")