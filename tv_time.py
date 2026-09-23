# Parents are trying to devise screentime rules for their kids
# They decide that the child cna have 30 minutes of cocomelon if their room is clean
# AND they've done their homework


homework = input("Are you done with your homework (Y/N)? ").upper()
room = input("Is your room clean (Y/N)? ").upper()
homework_done = homework == "Y"
room_done = room == "Y"

if homework_done and room_done:
    print("Enjoy CocoMelon, Ipad child")
else:
    print("Nope")