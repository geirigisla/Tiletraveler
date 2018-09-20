#Upphafsstaða characters
# char_x, char_y = 1, 1
#Opna hurðin í fyrsta herbergi er í Norður, 'n'

def print_doorways_available(doors):
    """Prentar út hverjar mögulegar dyragættir eru"""
    print("You can travel:", doors)

def print_victory():
    """Prentar victory!"""
    print("Victory!")

def character_locator(char_x, char_y):
    """Finnur staðsetningu characters miðað við upplýsingar úr korti"""
    victory = False
    if char_x == 1 and char_y == 1:   doorways = 'n' 
    elif char_x == 1 and char_y == 2: doorways = 'nes' 
    elif char_x == 1 and char_y == 3: doorways = 'es'  
    elif char_x == 2 and char_y == 1: doorways = 'n'   
    elif char_x == 2 and char_y == 2: doorways = 'ws'  
    elif char_x == 2 and char_y == 3: doorways = 'we'  
    elif char_x == 3 and char_y == 2: doorways = 'ns'  
    elif char_x == 3 and char_y == 3: doorways = 'ws'
    elif char_x == 3 and char_y == 1: doorways = ''; victory = True
    
    return doorways, victory

def compass(direction):
    """tekur inn doorways kóða úr "character_locator" og sendir út réttan texta"""
    
    if direction == 'n':     path = "(N)orth."
    elif direction == 'nes': path = "(N)orth or (E)ast or (S)outh."
    elif direction == 'es':  path = "(E)ast or (S)outh."
    elif direction == 'ws':  path = "(S)outh or (W)est."
    elif direction == 'we':  path = "(E)ast or (W)est."
    elif direction == 'ns':  path = "(N)orth or (S)outh."
    elif direction == '':    path = "Victory!" 

    return path

def set_new_position(validdirection):
    """tekur input um hvaða átt notandi vill færa character, skilar út áttinni"""
    nextmove = input("Direction: ").lower()
    while nextmove not in validdirection:
        print("Not a valid direction!")
        nextmove = input("Direction: ").lower()

    return nextmove

def mover(char_nextmove, opendoors, char_x, char_y):
    """tekur inn núverandi x og y hnit characters - umbreytir í "charmoves" og breytir byggt á inputti - og skilar út x og y hniti"""
    charmoves_x = char_x
    charmoves_y = char_y
    travelpass = True
    if (char_nextmove == 'n') and ('n' in opendoors): charmoves_y += 1; charmoves_x, charmoves_y
    elif (char_nextmove == 's') and ('s' in opendoors): charmoves_y -= 1; charmoves_x, charmoves_y
    elif (char_nextmove == 'e') and ('e' in opendoors): charmoves_x += 1; charmoves_x, charmoves_y
    elif (char_nextmove == 'w') and ('w' in opendoors): charmoves_x -= 1; charmoves_x, charmoves_y
   
    return charmoves_x, charmoves_y, travelpass

char_x=1; char_y=1

while 1:
    
    char_doorways, victory = character_locator(char_x, char_y)  # character_locator(char_x, char_y) #Character locator finnur hvar character er
    #Býr til char_doorways breytuna úr nsew kóða úr character_locator
   
    if victory == True:
        print_victory()
        break      
        
    mypath = compass(char_doorways) #Sendir nsew kóða í compass til að finna réttan texta
    #Býr til mypath breytuna úr compass
    print_doorways_available(mypath) #Prentar

    char_nextmove = set_new_position(char_doorways) #Tekur inn input notanda um átt
   
char_x, char_y, travelpass = mover(char_nextmove, char_doorways, char_x, char_y)