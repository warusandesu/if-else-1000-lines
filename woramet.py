name = (input("What is your name? \n"))
while name == "":
       name = (input("Enter your name:"))
if name == "พี" or name == "P" or name == "p" or name == "Pee" or name == "pee" or name == "อัครชัย" or name == "Akarachai" or name == "akarachai":
                print("ควายไอ้เหี้ยโง่ไอ้กากไอ้สถุนไอ้ควยควยควยควยควยควยควยควยควยควย")
                exit()
else :
        print("Hello " + name + "!")
age = int(input("How old are you? \n"))
while age == "":
       age = (input("Enter your age:"))
if age <= 17:
        print("Hey, kiddo!")
        future = str(input("What do you want to be in the future? \n"))
        print("So an " + future + "? " "Have a nice day and keep learning hard, " + name + "!")
elif age >= 18:
        job = str(input("What do you do for a living? \n"))
        if job == "Student" or job == "student":
                print("Please study hard, " + name + "!")
        elif job == "Enginner" or job == "engineer":
                print("Wow, so you build stuff? " + "that's nice, " + name + "!")
        elif job == "Doctor" or job == "doctor" or job == "Medic" or job == "medic" or job == "Nurse" or job == "nurse" or job == "Surgeon" or job == "surgeon" or job == "Physician" or job == "physician":
                print("Thanks for keeping us fine, " + name + "!")
        elif job == "Teacher" or job == "teacher" or job == "Professor" or job == "professor":
                print("Thanks for educating us, " + name + "!")
        elif job == "Programmer" or job == "programmer" or job == "Developer" or job == "developer" or job == "Software Engineer" or job == "software engineer":
                print("So you are a big geek! " + "That's awesome, " + name +"!")
        elif job == "Unemployed" or job == "unemployed" or job == "Jobless" or job == "jobless":
                print("Good luck finding a job, " + name + "!")
        elif job == "Soldier" or job == "soldier" or job == "Military" or job == "military" or job == "Army" or job == "army":
                print("Thank you for your service, " + name + "!")
                branch = str(input("Which branch are you in? \n"))
                if branch == "Army" or branch == "army":
                        print("So you are in the Army, " + name + "!")
                elif branch == "Marines" or branch == "marines":
                        print("You eat cranyons! ")
                elif branch == "Navy" or branch == "navy":
                        print("So you sail the seas, " + name + "!")
                elif branch == "Air Force" or branch == "air force" or branch == "Airforce" or branch == "airforce" or branch == "Air force":
                        pilot = str(input("Are you a pilot? \n"))
                        if pilot == "Yes" or pilot == "yes":
                                print("That's awesome!")
                        else :
                                print("You are no fun...")
                elif branch == "Navy" or branch == "navy" :
                        print("So you sail the seas!")
                        seals = str(input("That's mean you are in the SEALs, right? \n"))
                        if seals == "Yes" or seals == "yes":
                                print("Wow, that's awesome!")
                        else :
                                print("Oh my bad...")                         
                rank = str(input("What is your rank then? \n"))
                if rank == "Private" or rank == "private":
                        print("So you are Private " + name + "!")
                elif rank == "Sergeant" or rank == "sergeant":
                        print("So you must be good at leading people, Sergeant " + name + "!")
                elif rank == "Lieutenant" or rank == "lieutenant" or rank == "Lt" or rank == "lt" or rank == "LT" or rank == "Captain" or rank == "captain" or rank == "capt" or rank == "Capt" or rank == "Major" or rank == "major" or rank == "Colonel" or rank == "colonel":
                        print("Wow so you are an officer! " + "Thank you for your service!")
                elif rank == "General" or rank == "general" or rank == "Gen" or rank == "gen":
                        print("Wow, a general!")
                else :
                        print("Thank you for your service once again!")
        elif job == "Farmer" or job == "farmer":
                print("Thank you for producing our food!")
        elif job == "Chef" or job == "chef" or job == "Cook" or job == "cook":
                print("So you are good at cooking! That's nice!")
        elif job == "Artist" or job == "artist" or job == "Painter" or job == "painter" or job == "Designer" or job == "desginer":
                print("Wow, you must be creative!")
        elif job == "Musician" or job == "musician" or job == "Singer" or job == "singer":
                print("That's nice!")
        elif job == "Architect" or job == "architect":
                print("So you design buildings? Nice!")
        elif job == "Police Officer" or job == "police officer" or job == "Police" or job == "police" or job == "Cop" or job == "cop":
                print("Thanks for keeping us safe!")
        elif job == "Firefighter" or job == "firefighter" or job == "Fireman" or job == "fireman":
                print("Thank you for your bravery!")
        elif job == "Scientist" or job == "scientist" or job == "Researcher" or job == "researcher":
                print("Wow, you must be smart!")
        elif job == "Athlete" or job == "athlete" or job == "Sportsperson" or job == "sportsperson" or job == "Footballer" or job == "footballer" or job == "Basketball Player" or job == "basketball player" or job == "Tennis Player"  or job  == "tennis player" or job == "Runner" or job == "runner":
                print("That's awesome! Keep it up!")
        elif job == "Writer" or job == "writer" or job == "Author" or job == "author" or job == "Novelist" or job == "novelist" or job == "Poet" or job == "poet":
                print("That's great! Keep writing!")
        elif job == "Dancer" or job == "dancer" or job == "Choreographer" or job == "choreographer":
                print("Wow! keep dancing!")
        elif job == "Photographer" or job == "photographer":
                print("So you take great pictures!")
        elif job == "Journalist" or job == "journalist" or job == "Reporter" or job == "reporter":
                print("Thanks for keeping us informed!")
        elif job == "Pilot" or job == "pilot" or job == "Flight Attendant" or job == "flight attendant":
                print("Wow, you must love traveling!")
        elif job == "Mechanic" or job == "mechanic" or job == "Technician" or job == "technician":
                print("So you fix things! That's nice!")
        else : 
                print("That's nice!")
elif age >= 65:
        retire = str(input("Are you retired? \n"))
        if retire == "Yes" or retire == "yes":
                print("Enjoy your retirement, " + name + "!")
        else :
                print("Wow you are still working hard!")




