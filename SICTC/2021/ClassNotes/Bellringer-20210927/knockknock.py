def loop():
    UI = input("Knock knock >>> ");
    if UI.lower() == "who's there?":
        UI = input("Kanga >>> ");
        if UI.lower() == "kanga who?":
            print("Actually, it's kangaroo!");
        else:
            print('You ruined the joke! You were supposed to say "Kanga who?"!');
            loop();
    else:
        print('You ruined the joke! You were supposed to say "Who'+"'"+'s there?"!');
        loop();
loop();
