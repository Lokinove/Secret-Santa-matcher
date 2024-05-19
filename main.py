import random
ppl = int(input("How many people are there? "))



names = []
for i in range(ppl):
    name = input("Enter a name: ")
    names.append(name)
random.shuffle(names)


nocouples = int(input("how many couples"))
couples = []

for i in range(nocouples):
  couples.append(input("couple " + str(i+1) + ": "))
  print(couples)


def secetsente():
  global nocouples
  i = 2
  #for i in range(ppl):
  print(str(names[1],names[2]))
    # if nocouples == 0: 
    #   if str(names[i-1] + names[i]) == couples[i]:
    #     print(names[i-1] + " is giving to " + names[i])
    #   else:
    #     print(names[i-1] + " is giving to " + names[i])
secetsente()