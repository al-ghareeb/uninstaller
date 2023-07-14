# Importing
import subprocess

# Displaying the name 
subprocess.call("apt install figlet" ,  shell=True )
subprocess.call("clear " ,  shell=True )
subprocess.call("figlet 'Al Ghareeb'" ,  shell=True )
subprocess.call("echo '-> With this program you can easliy unimstall any program.'" ,  shell=True )
subprocess.call("echo ''" ,  shell=True )
print(input("Press enter start :- "))

# Taking user input 
subprocess.call("clear " ,  shell=True )
program = input("Which program do you want to uninstall > ")
answer = input("You want to uninstall " + program +" > ")

if answer == "yes":
    print("OK...")

else:
    print(" ")
    print("Exiting")
    subprocess.call("exit",  shell=True )


# Removing progron 
subprocess.call("apt clean ",  shell=True )
subprocess.call("apt remove " + program ,  shell=True )
subprocess.call("apt purge " + program ,  shell=True )
subprocess.call("apt autoremove " ,  shell=True )
subprocess.call("apt autopurge ",  shell=True )
subprocess.call("apt autoclean " ,  shell=True )

# End...
subprocess.call("clear" ,  shell=True )
subprocess.call("figlet 'Al Ghareeb'" ,  shell=True )
subprocess.call("echo ''" ,  shell=True )
