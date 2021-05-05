    
# def writeFile():
#     file = open("filename.txt", "w")

#     for n in range(1,11):
#         newline = f"This is line {n} \n"
#         file.write(newline)

#     file.close()

# def readFile():
#     file = open("filename.txt", "r")

#     print(file.read())

#     file.close()


# writeFile()
# readFile()

# def readAndWrite():
#     file = open("filename.txt", "r")

#     outfile = ""

#     for line in range(1, 101):
#         if line % 2 == 1:
#             outfile += file.readline()
#         else:
#             file.readline()

#     file = open("filename.txt", "w")
#     file.write(outfile)
#     file.close()

teams = ["liverpool", "man city", "arsenal", "man united"]

with open("teams.txt", "w") as file:
    for n in range(0,4):
        newline = f"{str(n+1)} - {teams[n]} \n"
        file.write(newline)

with open("teams.txt", "r") as file:
    for line in file:
        print(line)


def readTeams():
    file = open("teams.txt", "r")

    outfile = "This is a new line\n"

    for line in range(1,6):
        if line == 1 or line == 3:
            print(file.readline() + "Fail")
        else:
            outfile = outfile + file.readline()
            

    file = open("teams.txt", "w")
    file.write(outfile)
    file.close()


readTeams()


    
# readAndWrite()