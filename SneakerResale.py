def start():
    print("Enter a Brand")
    item = str(input())
    if item in 'Adidas':
        adidas()
    elif item == 'Nike':
        nike()
    else:
        error()

def adidas():
    print("Enter shoe")
    item = str(input())
    if item == 'Original':
        noProfit()
    elif item == 'Yeezy':
        yeezy() 
    else:
        error()

def nike():
    print("Enter a Nike Collaboration or Nike Brand Shoe")
    item = str(input())
    if item == 'Converse':
        noProfit()
    elif item in ['Fear of God','Off-White','Sacai']:
        bigProfit()
    elif item == 'Jordan':
        airJordan()
    else:
        error()

def airJordan():
    print("Enter a designer or Jordan Model")
    item = str(input())
    if item == 'Jordan 1 Retro':
        jordan1()
    elif item == 'Jordan 6':
        jordan6()
    elif item == 'Travis Scott':
        bigProfit()
    else:
        error()

def jordan1():
    print("Enter a Jordan 1 Colorway")
    item = str(input())
    if item in ['Yellow Toe', 'First Class']:
        smallProfit()
    elif item in ['Satin Black Toe', 'University Blue']:
        bigProfit()
    else:
        error()

def jordan6():
    print("Enter a Jordan 6 Colorway")
    item = str(input())
    if item in ['Infared', 'Dorenbecher', 'Olympic']:
        bigProfit()
    else:
        error()
    

def yeezy():
    print("Enter Yeezy Model")
    item = str(input())
    if item == '700':
        state700()
    elif item == '500':
        bigProfit()
    elif item == '350':
        state350()
    else:
        error()

def state700():
    print("Enter Yeezy 700 Colorway")
    item = str(input())
    if item in ['Static']:
        bigProfit()
    elif item in ['Intertia','Analog','Mauve',
                    'Tephra','Geode','Teal','Salt']:
        noProfit()
    elif item in ['Wave Runner', 'Vanta','Utility Black', 'Magnet']:
        smallProfit()
    else:
        error()

def state350():
    print("Enter version of 350")
    item = str(input())
    if item in ['V2']:
        state350V2Colorway()
    elif item in ['V1']:
        bigProfit()
    else:
        error()

def state350V2Colorway():
    print("Enter Yeezy 350 V2 Colorway")
    item = str(input())
    if item in ['Bred', 'Beluga','Beluga 2.0','Oreo',
                    'Copper','Olive','Core Red Black',
                    'Zebra','Blue Tint','Glow','Hyperspace',
                    'Static','Reflective']:
        bigProfit()
    elif item in ['Clay','Cream']:
        noProfit()
    elif item in ['Lundmark', 'Synth','Terraform',
                      'Semi-Frozen Yellow','Butter','Sesame','Black']:
        smallProfit()
    else:
        error()


        


def noProfit():
   print("No Profit \n=====================")
   start()

def bigProfit():
    print("Big Profit \n=====================")
    start()

def smallProfit():
   print("Small Profit \n=====================")
   start()

def error():
    print("You entered an invalid shoe start over \n=====================")
    start()
        

start()

