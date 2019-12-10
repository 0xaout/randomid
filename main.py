import random 
import string

def randomId():
    # generate a 62 string list
    characters = list(string.ascii_letters) + list(string.digits)            

    # read each lines of the txt file
    with open("shortrandomidgenerator/id.txt", 'r') as r:
       lines = r.readlines()

    # array of 
    id = []
    id.append(characters[random.randint(0, 61)])

   # check if the generated id already exist
    for n,i in enumerate(lines):
        if(lines[n].replace('\n', '') == ''.join(id)):
            while(lines[n].replace('\n', '') == ''.join(id)):
                id.append(characters[random.randint(0, 61)])

    with open("shortrandomidgenerator/id.txt", 'a') as a:
        a.write(''.join(id) + '\n')
               
for i in range(25000):
    randomId()










     
            

     

   