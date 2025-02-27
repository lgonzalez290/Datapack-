import random
try1=0
playing=True
print(" this is just basic text thjat i bfell lioke writn down because i am broed this sp[oprbly not wroiten or spelled well because i am doing this really fast and on a mechicxal keyberoad sooooo")
randomnumber=random.randint(1,10)
while playing:
    geuss=input("Geuss a random number :")
    if geuss == randomnumber:
        print("You are gay ")
        playing=False
        try1+=1
        print("It took you this many tries",try1,"")

    else:
        print("geuss again")
        try1+=1