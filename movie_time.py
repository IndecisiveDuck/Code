movie_rating = input("What Movie do you want to see(G, PG, PG-13, R)? ")

if movie_rating == 'G':
    print("Enjoy your movie")
else:
    age = int(input("How old are you? "))

    if movie_rating == "PG":
        age_cutoff = 7
    elif movie_rating == "PG-13":
        age_cutoff = 13
    elif movie_rating == "R":
        age_cutoff = 17
    else:
        print("Invalid movie rating")

    if age >= age_cutoff:
        print("Enjoy your movie!")
    else:
        gardian = input("Are you with a parent or guardian(Y/N)? ")
        if gardian == "Y":
            print("Enjoy your movie!")
        else:
            print("Sorry, no admitence.")