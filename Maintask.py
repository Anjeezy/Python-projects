def greeting(username):
    print(f"\n Hi {username} Welcome to the Exam Portal! \n")


def greet(username):
    print(f"\n Hi {username} \n")


def courses_section():
    while True:
        user_input = input(
            "Press Space and Enter to proceed to Course Section \n \n ").title()
        if user_input == " ":
            greet(name)
            break
        else:
            print("invalid Command")


def Next_():
    while True:
        user_input = input(
            "Press Space and Enter to proceed to continue\n \n ").title()
        if user_input == " ":
            greet(name)
            break
        else:
            print("invalid Command")


def Next_Exam():
    while True:
        user_input = input(
            "Press Space and Enter to proceed to continue to result section\n \n ").title()
        if user_input == " ":
            greet(name)
            break
        else:
            print("invalid Command")


print("JOINT ADMISSIONS AND MATRICULATION BOARD")

while True:
    name = input("What is your name?: ")

    if len(name) >= 21:
        print("Name should not exceed 20 characters\n")
        continue
    elif len(name) <= 2:
        print("Name should be at least 3 characters\n")
        continue
    elif any(char.isdigit() for char in name):
        print("Name should not contain numbers")
    else:
        break

while True:
    try:
        age = int(input("What is your age?: "))
        if age > 25:
            print("Ineligible for examination. Age should not be more than 25\n")
            continue
        elif age < 16:
            print("Ineligible for examination, Age shoudl be at least 16\n")
            continue
        break
    except ValueError:
        print("Invalid age")


greeting(name)

Total_score = 0
score = 0
bio_score = 0
chm_score = 0
phy_score = 0
comp_score = 0
eng_score = 0
mth_score = 0

location = input("where do you live?: ").title()

if location in ["Abuja", "Lagos"]:
    score += 3
else:
    score += 0

courses_section()

courses = ["Biology", "Chemistry", "Physics",
           "Maths", "English", "Computer Science"]
courses_completed = []
while True:
    if len(courses_completed) == 4:
        break
    raw_courses_input = input(
        f"\n Welcome to the Course Section. Select 4 Courses with each course seperated by a single comma:\n {', '.join(courses)} \n \n").strip()
    courses_input_list = [s.strip().title()
                          # splits input into list
                          for s in raw_courses_input.split(",") if s.strip()]

    if len(courses_input_list) != 4:
        print("Please ensure you select 4 courses from the list ")
        continue
    if len(courses_input_list) != len(set(courses_input_list)):
        print("You cannot select the same course(s)")
        continue
    invalid_courses = [s for s in courses_input_list if s not in courses]
    if invalid_courses:
        print(
            f"Invalid response one or more courses not in list of courses ")
        continue
    selected_list = courses_input_list[:]
    if selected_list in courses_completed:
        print(
            f"One or more {selected_list} already completed. Select another course")
        continue
    else:
        print("\n Courses Selected\n Moving on to Selected Courses Section ")
        Next_()

    selected_course_completed = []
    remaining_courses = selected_list[:]
    while True:
        if len(selected_course_completed) == 4:
            break
        print(
            f"Welcome to the Selected Courses section. You selected: {', '.join(selected_list)}")
        if 1 <= len(remaining_courses) < 4:
            print(f"\nYou have {', '.join(remaining_courses)} left ")
        pick_course = input(
            "\nPick a course out of these to continue \n \n ").title()

        if pick_course in selected_course_completed:
            print(f"\n{pick_course} already Picked")
            print("Pick another!")
            continue
        if pick_course not in selected_list:
            print(f"\n{pick_course} not in Selected list")
            continue
        if pick_course in selected_list:
            if pick_course == "Biology":
                print("\nWelcome to The Biology Section ")
                bio_attempts_left = 3
                bio_score = 0
                while bio_score <= 20 and bio_attempts_left >= 1:
                    print(
                        "Biology Test Starts Now!. Select the best options A, B, C, D for each question")
                    bio_score = 0
                    Q1 = input(
                        "\n1. What is the largest organ of the human body?: \n A. Heart \n B. Liver \n C. Skin \n D. Lungs \n \n ").title()
                    if Q1 == "C":
                        bio_score += 20
                    else:
                        bio_score += 0
                    Q2 = input(
                        " \n2. How many litres of Blood are in the averge Adult Man?: \n A. 5 \n B. 1 \n C. 10 \n D. 3 \n \n ").title()
                    if Q2 == "A":
                        bio_score += 20
                    else:
                        bio_score += 0
                    Q3 = input(
                        "\n3. What organ is responsible for respiration?: \n A. Stomach \n B. Diaphragm \n C. Heart \n D. Lungs \n  \n").title()
                    if Q3 == "D":
                        bio_score += 20
                    else:
                        bio_score += 0
                    Q4 = input(
                        " \n4. What part of the eyes sees colour?: \n A. Retina \n B. Rods \n C. Cones \n D. Lens \n \n ").title()
                    if Q4 == "C":
                        bio_score += 20
                    else:
                        bio_score += 0
                    Q5 = input(
                        " \n5. What is the longest bone in the human body?: \n A. Femur \n B. Humerus \n C. Tibia \n D. Ulna \n \n ").title()
                    if Q5 == "A":
                        bio_score += 20
                    else:
                        bio_score += 0

                    Grade_F = bio_score <= 20
                    Grade_D = 21 == bio_score <= 39
                    Grade_C = 40 == bio_score <= 59
                    Grade_B = 60 == bio_score <= 79
                    Grade_A = bio_score >= 80

                    if Grade_A:
                        print(
                            f"\nWell done! {name} your grade is {bio_score}A")
                    elif Grade_B:
                        print(
                            f"\nWell done! {name} your grade is {bio_score}B")
                    elif Grade_C:
                        print(
                            f"\nWell done! {name} your grade is {bio_score}C")
                    elif Grade_D:
                        print(
                            f"\nWell done! {name} your grade is {bio_score}D")
                    elif Grade_F:
                        bio_attempts_left -= 1
                        print(
                            f" \nSorry {name} your grade is {bio_score}F Fail")
                        print(f" Attempts left is {bio_attempts_left}\n")
                    if bio_score <= 20 and bio_attempts_left == 0:
                        print(
                            f" You have {bio_attempts_left} Attempts Left. No more retakes")
                        break
                selected_course_completed.append(pick_course)
                courses_completed.append(pick_course)
                remaining_courses.remove(pick_course)
                print("\n Test Completed. Moving on to Selected Courses Section")
                Next_()
            elif pick_course == "Chemistry":
                print(" \nWelcome to The Chemistry Section")
                chm_attempts_left = 3
                chm_score = 0
                while chm_score <= 20 and chm_attempts_left >= 1:
                    print(
                        "Chemistry Test Starts Now!. Select the best options A, B, C, D for each question")
                    chm_score = 0
                    Q1 = input(
                        " \n1. Which of the following is a noble gas?: \n A. Oxygen \n B. Nitrogen \n C. Helium \n D. Hydrogen \n \n ").title()
                    if Q1 == "C":
                        chm_score += 20
                    else:
                        chm_score += 0
                    Q2 = input(
                        " \n2. The atomic number of an element represents the number of?: \n A. Neutrons \n B. Protons \n C. Electrons only \n D. Neutrons \n \n ").title()
                    if Q2 == "B":
                        chm_score += 20
                    else:
                        chm_score += 0
                    Q3 = input(
                        " \n3. Which of these is a compound?: \n A. Iron \n B. Water \n C. Oxygen \n D. Hydrogen \n \n ").title()
                    if Q3 == "B":
                        chm_score += 20
                    else:
                        chm_score += 0
                    Q4 = input(
                        " \n4. What is the compound CaCl2?: \n A. Calcium Chloride \n B. Calcium Oxide \n C. Calcium bicarbonate \n D. Caustic soda \n \n ").title()
                    if Q4 == "A":
                        chm_score += 20
                    else:
                        chm_score += 0
                    Q5 = input(
                        " \n5. What is the atomic number of Oxygen?: \n A. 16 \n B. 7 \n C. 10 \n D. 8 \n \n ").title()
                    if Q5 == "D":
                        chm_score += 20
                    else:
                        chm_score += 0

                    Grade_F = chm_score <= 20
                    Grade_D = 21 == chm_score <= 39
                    Grade_C = 40 == chm_score <= 59
                    Grade_B = 60 == chm_score <= 79
                    Grade_A = chm_score >= 80

                    if Grade_A:
                        print(
                            f"\nWell done! {name} your grade is {chm_score}A")
                    elif Grade_B:
                        print(
                            f"\nWell done! {name} your grade is {chm_score}B")
                    elif Grade_C:
                        print(
                            f"\nWell done! {name} your grade is {chm_score}C")
                    elif Grade_D:
                        print(
                            f"\nWell done! {name} your grade is {chm_score}D")
                    elif Grade_F:
                        chm_attempts_left -= 1
                        print(
                            f" \nSorry {name} your grade is {chm_score}F Fail")
                        print(f" Attempts left is {chm_attempts_left}\n")
                    if chm_score <= 20 and chm_attempts_left == 0:
                        print(
                            f" You have {chm_attempts_left} Attempts Left. No more retakes")
                        break
                selected_course_completed.append(pick_course)
                courses_completed.append(pick_course)
                remaining_courses.remove(pick_course)
                print("\n Test completed. Moving on to Selected Courses Section")
                Next_()
            elif pick_course == "Physics":
                print(" \nWelcome to The Physics Section")
                phy_attempts_left = 3
                phy_score = 0
                while phy_score <= 20 and phy_attempts_left >= 1:
                    print(
                        " Physics Test Starts Now!. Select the best options A, B, C, D for each question")
                    phy_score = 0
                    Q1 = input(
                        " \n1. The unit of force is?: \n A. Joule \n B. Watt \n C. Newton \n D. Pascal \n \n ").title()
                    if Q1 == "C":
                        phy_score += 20
                    else:
                        phy_score += 0
                    Q2 = input(
                        " \n2. Which of these is a vector quantity?: \n A. Speed \n B. Velocity \n C. Distance \n D. Time \n \n ").title()
                    if Q2 == "B":
                        phy_score += 20
                    else:
                        phy_score += 0
                    Q3 = input(
                        " \n3. The energy possessed by a moving body is called?: \n A. Potential energy \n B. Heat energy \n C. Kinetic energy \n D. Light energy \n \n ").title()
                    if Q3 == "C":
                        phy_score += 20
                    else:
                        phy_score += 0
                    Q4 = input(
                        " \n4. What is Force X Area?: \n A. Pressure \n B. Acceleration \n C. Power \n D. Velocity \n \n ").title()
                    if Q4 == "A":
                        phy_score += 20
                    else:
                        phy_score += 0
                    Q5 = input(
                        " \n5. What is the unit of Current?: \n A. Joules \n B. Volts \n C. Watts \n D. Ampere \n \n ").title()
                    if Q5 == "D":
                        phy_score += 20
                    else:
                        phy_score += 0

                    Grade_F = phy_score <= 20
                    Grade_D = 21 == phy_score <= 39
                    Grade_C = 40 == phy_score <= 59
                    Grade_B = 60 == phy_score <= 79
                    Grade_A = phy_score >= 80

                    if Grade_A:
                        print(
                            f"\nWell done! {name} your grade is {phy_score}A")
                    elif Grade_B:
                        print(
                            f"\nWell done! {name} your grade is {phy_score}B")
                    elif Grade_C:
                        print(
                            f"\nWell done! {name} your grade is {phy_score}C")
                    elif Grade_D:
                        print(
                            f"\nWell done! {name} your grade is {phy_score}D")
                    elif Grade_F:
                        phy_attempts_left -= 1
                        print(
                            f" \nSorry {name} your grade is {phy_score}F Fail")
                        print(f" Attempts left is {phy_attempts_left}\n")
                    if phy_score <= 20 and phy_attempts_left == 0:
                        print(
                            f" You have {phy_attempts_left} Attempts Left. No more retakes")
                        break
                selected_course_completed.append(pick_course)
                courses_completed.append(pick_course)
                remaining_courses.remove(pick_course)
                print("\n Test completed. Moving on to Selected Courses Section")
                Next_()
            elif pick_course == "Maths":
                print("\nWelcome to The Maths Section")
                mth_attempts_left = 3
                mth_score = 0
                while mth_score <= 20 and mth_attempts_left >= 1:
                    print(
                        "Maths Test Starts Now!. Select the best options A, B, C, D for each question")
                    mth_score = 0
                    Q1 = input(
                        " \n1. Simplify 2x + 3x?: \n A. 5 \n B. 6x \n C. 5x \n D. 4x \n \n ").title()
                    if Q1 == "C":
                        mth_score += 20
                    else:
                        mth_score += 0
                    Q2 = input(
                        " \n2. What is the square root of 49?: \n A. 7 \n B. 6 \n C. 9 \n D. 14 \n \n ").title()
                    if Q2 == "A":
                        mth_score += 20
                    else:
                        mth_score += 0
                    Q3 = input(
                        " \n3. Find the mean of 2,3,4,8.?: \n A. 5 \n B. 6 \n C. 4 \n D. 10 \n \n ").title()
                    if Q3 == "B":
                        mth_score += 20
                    else:
                        mth_score += 0
                    Q4 = input(
                        " \n4. The sum of angles in a triagnle is?: \n A. 90 \n B. 360 \n C. 120 \n D. 180 \n \n ").title()
                    if Q4 == "D":
                        mth_score += 20
                    else:
                        mth_score += 0
                    Q5 = input(
                        " \n5. What is diameter/2?: \n A. Sector \n B. Radius \n C. Segment \n D. Arc \n \n ").title()
                    if Q5 == "B":
                        mth_score += 20
                    else:
                        mth_score += 0

                    Grade_F = mth_score <= 20
                    Grade_D = 21 == mth_score <= 39
                    Grade_C = 40 == mth_score <= 59
                    Grade_B = 60 == mth_score <= 79
                    Grade_A = mth_score >= 80

                    if Grade_A:
                        print(
                            f"\nWell done! {name} your grade is {mth_score}A")
                    elif Grade_B:
                        print(
                            f"\nWell done! {name} your grade is {mth_score}B")
                    elif Grade_C:
                        print(
                            f"\nWell done! {name} your grade is {mth_score}C")
                    elif Grade_D:
                        print(
                            f"\nWell done! {name} your grade is {mth_score}D")
                    elif Grade_F:
                        mth_attempts_left -= 1
                        print(
                            f" \nSorry {name} your grade is {mth_score}F Fail")
                        print(f" Attempts left is {mth_attempts_left}\n")
                    if mth_score <= 20 and mth_attempts_left == 0:
                        print(
                            f" You have {mth_attempts_left} Attempts Left. No more retakes")
                        break
                selected_course_completed.append(pick_course)
                courses_completed.append(pick_course)
                remaining_courses.remove(pick_course)
                print("\n Test completed. Moving on to Selected Courses Section")
                Next_()
            elif pick_course == "English":
                print("\nWelcome to the English Section")
                eng_attempts_left = 3
                eng_score = 0
                while eng_score <= 20 and eng_attempts_left >= 1:
                    print(
                        "English Test Starts Now!. Select the best options A, B, C, D for each question")
                    eng_score = 0
                    Q1 = input(
                        " \n1. Choose the correct synonym of happy?: \n A. Sad \n B. Angry \n C. Worried \n D. Joyful \n \n ").title()
                    if Q1 == "D":
                        eng_score += 20
                    else:
                        eng_score += 0
                    Q2 = input(
                        " \n2. Which of the following is a verb?: \n A. Quickly \n B. Run \n C. Beautiful \n D. Tall \n \n ").title()
                    if Q2 == "B":
                        eng_score += 20
                    else:
                        eng_score += 0
                    Q3 = input(
                        " \n3. Identify the adjective in this sentence 'The boy is tall'?: \n A. Boy\n B. Is \n C. Tall \n D. The \n \n ").title()
                    if Q3 == "C":
                        eng_score += 20
                    else:
                        eng_score += 0
                    Q4 = input(
                        " \n4. Which of these is a correct sentence?: \n A. Give him him bag \n B. Give him his bag \n C. Give his him bag \n D. Give his is bag \n \n ").title()
                    if Q4 == "B":
                        eng_score += 20
                    else:
                        eng_score += 0
                    Q5 = input(
                        " \n5. The plural of child is?: \n A. Children \n B. Childs \n C. Child \n D. Childrens \n \n ").title()
                    if Q5 == "A":
                        eng_score += 20
                    else:
                        eng_score += 0

                    Grade_F = eng_score <= 20
                    Grade_D = 21 == eng_score <= 39
                    Grade_C = 40 == eng_score <= 59
                    Grade_B = 60 == eng_score <= 79
                    Grade_A = eng_score >= 80

                    if Grade_A:
                        print(
                            f"\nWell done! {name} your grade is {eng_score}A")
                    elif Grade_B:
                        print(
                            f"\nWell done! {name} your grade is {eng_score}B")
                    elif Grade_C:
                        print(
                            f"\nWell done! {name} your grade is {eng_score}C")
                    elif Grade_D:
                        print(
                            f"\nWell done! {name} your grade is {eng_score}D")
                    elif Grade_F:
                        eng_attempts_left -= 1
                        print(
                            f" \nSorry {name} your grade is {eng_score}F Fail")
                        print(f" Attempts left is {eng_attempts_left}\n")
                    if eng_score <= 20 and eng_attempts_left == 0:
                        print(
                            f" You have {eng_attempts_left} Attempts Left. No more retakes")
                        break
                selected_course_completed.append(pick_course)
                courses_completed.append(pick_course)
                remaining_courses.remove(pick_course)
                print("\n Test completed. Moving on to Selected Courses section")
                Next_()
            elif pick_course == "Computer Science":
                print("\nWelcome to the Computer Science Section")
                comp_attempts_left = 3
                comp_score = 0
                while comp_score <= 20 and comp_attempts_left >= 1:
                    print(
                        "Computer Science Test Starts Now!. Select the best options A, B, C, D for each question")
                    comp_score = 0
                    Q1 = input(
                        "\n1. What does CPU stand for?: \n A. Control Power Unit \n B. Central Processing Unit \n C. Central Program Unit \n D. Central Power Unit \n \n ").title()
                    if Q1 == "B":
                        comp_score += 20
                    else:
                        comp_score += 0
                    Q2 = input(
                        " \n2. The brain of the computer?: \n A. Mouse \n B. Monitor \n C. CPU \n D. Keyboard \n \n ").title()
                    if Q2 == "C":
                        comp_score += 20
                    else:
                        comp_score += 0
                    Q3 = input(
                        "\n3. Which of these is an output device?: \n A. Monitor \n B. Scanner \n C. Mouse \n D. Keyboard \n \n ").title()
                    if Q3 == "A":
                        comp_score += 20
                    else:
                        comp_score += 0
                    Q4 = input(
                        "\n4. Which of the following is a storage device?: \n A. Printer \n B. Monitor \n C. Flash drive \n D. Keyborard \n \n ").title()
                    if Q4 == "C":
                        comp_score += 20
                    else:
                        comp_score += 0
                    Q5 = input(
                        "\n5. Which of the following is a programming language?: \n A. Macbook \n B. Python \n C. Cobra \n D. English \n \n ").title()
                    if Q5 == "B":
                        comp_score += 20
                    else:
                        comp_score += 0

                    Grade_F = comp_score <= 20
                    Grade_D = 21 == comp_score <= 39
                    Grade_C = 40 == comp_score <= 59
                    Grade_B = 60 == comp_score <= 79
                    Grade_A = comp_score >= 80

                    if Grade_A:
                        print(
                            f"\nWell done! {name} your grade is {comp_score}A")
                    elif Grade_B:
                        print(
                            f"\nWell done! {name} your grade is {comp_score}B")
                    elif Grade_C:
                        print(
                            f"\nWell done! {name} your grade is {comp_score}C")
                    elif Grade_D:
                        print(
                            f"\nWell done! {name} your grade is {comp_score}D")
                    elif Grade_F:
                        comp_attempts_left -= 1
                        print(
                            f"\n Sorry {name} your grade is {comp_score}F Fail")
                        print(f" Attempts left is {comp_attempts_left}\n")
                    if comp_score <= 20 and comp_attempts_left == 0:
                        print(
                            f" You have {comp_attempts_left} Attempts Left. No more retakes\n")
                        break
                selected_course_completed.append(pick_course)
                courses_completed.append(pick_course)
                remaining_courses.remove(pick_course)
                print("\nTest completed. Moving on to Selected Course section")
                Next_()

print(" Congratulations! ")
print(
    f" All Selected Courses: {" , ".join(selected_course_completed)} were completed! ")
print(" \n Examination Completed \n")
Next_Exam()
print(" EXAMINATION RESULTS \n")
while True:
    if "Biology" in selected_course_completed:
        print(f" Biology = {bio_score}")
    if "Chemistry" in selected_course_completed:
        print(f" Cehmistry = {chm_score}")
    if "Physics" in selected_course_completed:
        print(f" Physics = {phy_score}")
    if "Maths" in selected_course_completed:
        print(f" Math score = {mth_score}")
    if "English" in selected_course_completed:
        print(f" English ={eng_score}")
    if "Computer Science" in selected_course_completed:
        print(f"Computer Science = {comp_score}")
    break
score1 = bio_score + chm_score + phy_score
score2 = mth_score + eng_score + comp_score
Total_score = score1 + score2 + score
if Total_score < 200:
    print(f"Your Total score is {Total_score}. FAIL")
if 200 <= Total_score <= 299:
    print(f"Your Total score is {Total_score} PASS")
if Total_score >= 300:
    print(f"Your score is {Total_score} PASS WITH EXCELLENCE")
print(f" Have a Good day \n END!")
