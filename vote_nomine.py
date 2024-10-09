# Frist take 2 input nomine 
nomine1 = input("Enter the name of 1st nomine1: ")
nomine2 = input("Enter the name of 2nd nomine2: ")

#=================================================
vot_count1 = 0
vot_count2 = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    if voter_id == []:
        print("voter sesson is over.")
        if vot_count1 > vot_count2:
            persentic = (vot_count1/no_of_voter)*100
            print(nomine1,"win the election of ",persentic,"%")
            break

        elif vot_count2 > vot_count1:
            perentic = (vot_count2/no_of_voter)*100
            print(nomine2,"win the election of ",perentic,"%")
            break
        
        else:
            print("Both have equal namber of vote govermant deside who will win")
            break


    voter = int(input("Enter your voter id: "))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter)
        print("-----------------------------------")
        print("To give vote to ",nomine1,"press 1 ")
        print("To give vote to ",nomine2,"press 2 ")
        print("-----------------------------------")
        vote = int(input("Enter your precuious vote : "))

        if vote ==1:
            vot_count1 +=1
            print(nomine1,"Thank you to give your important vote for them")

        elif vote ==2:
            vot_count2 +=1
            print(nomine2,"Thanks you to give your important vote for then ")

        elif vote>2:
            print("Chak your pass kye")
        else:
            print("you are not a voter OR you have already voted")


