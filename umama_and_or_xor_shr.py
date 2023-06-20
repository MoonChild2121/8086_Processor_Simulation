instructions = ["And", "Or", "Xor"]
enter = input("Enter instructions: ")
if (enter=="And"):
    def And(value):
        string="0000"
        if value[4:6]=='dx':
            string=string+"011"
        elif value[4:6]=='cx':
            string=string+"010"
        elif value[4:6]=='bx':
            string=string+"001"
        elif value[4:6]=='ax':
            string=string+"000"
        else:
            print("Instruction is not valid.")
        
        if value[7:9]=='dx':
            string=string+"011"
        elif value[7:9]=='cx':
            string=string+"010"
        elif value[7:9]=='bx':
            string=string+"001"
        elif value[7:9]=='ax':
            string=string+"000"
        else:
            print("Instruction is not valid.")
        
        print(string)

if(enter=="Or"):
    def Or(value):
        string="0001"
        if value[3:5]=='dx':
            string=string+"011"
        elif value[3:5]=='cx':
            string=string+"010"
        elif value[3:5]=='bx':
            string=string+"001"
        elif value[3:5]=='ax':
            string=string+"000"
        else:
            print("Instruction is not valid.")
        
        if value[6:8]=='dx':
            string=string+"011"
        elif value[6:8]=='cx':
            string=string+"010"
        elif value[6:8]=='bx':
            string=string+"001"
        elif value[6:8]=='ax':
            string=string+"000"
        else:
            print("Instruction is not valid.")

        print(string)
if(enter=="Xor"):
    def Xor(value):
        string="0011"
        if value[4:6]=='dx':
            string=string+"011"
        elif value[4:6]=='cx':
            string=string+"010"
        elif value[4:6]=='bx':
            string=string+"001"
        elif value[4:6]=='ax':
            string=string+"000"
        else:
            print("Instruction is not valid.")
        
        if value[7:9]=='dx':
            string=string+"011"
        elif value[7:9]=='cx':
            string=string+"010"
        elif value[7:9]=='bx':
            string=string+"001"
        elif value[7:9]=='ax':
            string=string+"000"
        else:
            print("Instruction is not valid.")
            
        print(string)


def opcode(value):
    if value[0:3]=='And':
        And(value)
    elif value[0:2]=='Or':
        Or(value)
    elif value[0:3]=='Xor':
        Xor(value)
    else:
        print("Instruction is not valid.")

opcode("Ax ax,bx")

def SHR(source,shift):
    if (regSize.has(source)):                  
        size = regSize.get(source)
        source = conversion(source,16,2)
        if(size==8):
             source = setsize("00000000",source)
        else:
             source = setsize("0000000000000000",source)
        source = source.slice(0,size-shift)
        regkey= source.slice(0,1)
        for i in range(shift):
            print(i)
            source = source.replace(/^/,"0")
        
        source = conversion(source,2,16)
        if (size==8):
            you_decide = dest.slice(-1)
            source = setsize("00",source)
            if(you_decide=="H"):
                source=source+regVal.get(regkey+"L")
            else:
                source=regVal.get(regkey+"H")+source
        
        else:
            source = setsize("0000",source)