
import subprocess
import optparse
#from random import choice,randrange
import random

def welcome_MACSlash():
    welcome = """
    -----------------------------------
    < Welcome to | MacReverse-SHELL | >
    -----------------------------------
              
              @zackonit-root  
   
   [**]     Choose MAC-VENDOR       [**]

   ==================================
    -> Casuallity Phones :   phone
    ->      IPhone       :  iphone
   ==================================

   """
    return welcome 

def generate_newUAA():
    alphabet = "a b c d e f"
    alphabet = alphabet.split(sep=" ")

    hexa_bin,hexa_n  = random.choice(alphabet) ,random.randrange(0,10)
    hexa_bin = hexa_bin+str(hexa_n)+":"
    return hexa_bin 

def change_MACaddress(mac_interface,typePhone,new_mac,COM):
    mac_interface = mac_interface
    typePhone = typePhone 
    command_complete =  "ifconfig " +  mac_interface + " down"
    change_mac = subprocess.run(command_complete,shell=True)

    command_complete =  "ifconfig " + mac_interface + " hw ether " +  new_mac + COM*3
    
    change_mac = subprocess.run(command_complete,shell=True)

    command_complete = "ifconfig " + mac_interface + " up"
    change_mac = subprocess.run(command_complete,shell=True)

    return "[+] Your new MAC is: @"+new_mac+COM *3


def reverse_BreakWall():
    OptReverse = optparse.OptionParser()
    OptReverse.add_option("--ph",dest="phone",help="<Hacker MAC_designer for Phone type Android and anothers")
    OptReverse.add_option("--iph",dest="iphone",help="Hacker Mac_designer for IPHONE type iOS ")
    OptReverse.add_option("--i",dest="interface",help="Network Interface,please execute in your terminal -> ifconfig ")
    OptReverse.add_option("--COM", dest="COM",help="Your new Serial UAA")


    (options,arguments) = OptReverse.parse_args()  

    phone = options.phone   #dest = interface
    iphone = options.iphone
    interface = options.interface 
    COM = options.COM 


    if phone and iphone:
        return "Error: Choose one Mac Vendor"
    
    elif phone:
        #access to dictionary => phones (devices_Vendorphones)
        devices_Vendorphones = ("7C:39:20:","00:1c:7b:","2c:f4:c5:")
        return change_MACaddress(interface,"<Android Phone Convencional>",random.choice(devices_Vendorphones),COM)
       
    elif iphone:
        #access to dictionary devices_action
        devices_action = ("f8:f1:b6:","f8:e0:79:","e0:75:7d:")
        return change_MACaddress(interface,"<IPhone iOS Operative>",random.choice(devices_action),COM)
    else:
        #random token
        all_devices = ("7C:39:20:","00:1c:7b:","2c:f4:c5:","f8:f1:b6:","f8:e0:79:","e0:75:7d:")
        return change_MACaddress(interface,"<Random Device>",random.choice(all_devices),generate_newUAA())


if __name__ == "__main__":
    shellWelcome = welcome_MACSlash()
    print(shellWelcome)
    print(reverse_BreakWall())









