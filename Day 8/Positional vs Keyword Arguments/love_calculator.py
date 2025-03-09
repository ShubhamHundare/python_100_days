def calculate_love_score(name1, name2):
    word_1 = ["T", "R", "U", "E"]
    word_2 = ["L", "O", "V", "E"]
    count_1 = []
    count_2 = []

    name3 = (name1 + name2).upper()

    for i in range(0, 4):
        count1 = name3.count(word_1[i])
        count_1.append(count1)

        count2 = name3.count(word_2[i])
        count_2.append(count2)

    total_1 = sum(count_1)
    total_2 = sum(count_2)

    total = str(total_1) + str(total_2)
    print(f"Your Love Score is {total} %")


name1 = input("Enter your Name :\n")
name2 = input("Enter your crush name :\n")

calculate_love_score(name1, name2)
