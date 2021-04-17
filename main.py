import webbrowser
import shutil
import random
import os
error1 = ":Command not found"
thankyou = "thanks for using me :), made by abhijeet prabhakar"
java1 = "java download"
python1 = "python download"
help1 = "type help! to see all commands"
duh1 = 'r'
exit1 = "press any key to close"

print("type 'help!' to see all commands :)")
command1 = input("add a command:")
if command1 == "open browser":
    webbrowser.open('https://www.bing.com', new=1)
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'help!':
    print('commands: python download, java download, open browser, open browser youtube, open browser github')
    print('open browser spotify, open browser stackoverflow, close, quit, open browser java, open browser jdk')
    print('gmail login, close, move file, download c#, download donut, download unity c#, open browser gmail')
    print("open browser fiverr, open browser itch, open browser blender, copy file, creator, who is your creator")
    print("choose random num, choose random number")
    input('press any key to end the program')

elif command1 == 'creator':
    print('Made by Abhijeet Prabhakar')
    input('press any key to exit')
    quit()

elif command1 == 'who is your creator':
    print('Made by Abhijeet Prabhakar')
    input('press any key to exit')
    quit()

elif command1 == 'open browser youtube':
    webbrowser.open_new_tab('https://www.youtube.com')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'open browser github':
    webbrowser.open_new_tab('https://www.github.com')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'open browser stackoverflow':
    webbrowser.open_new_tab('https://www.stackoverflow.com')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'open browser fiverr':
    webbrowser.open_new_tab('https://www.fiverr.com')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'open browser itch':
    webbrowser.open_new_tab('https://www.itch.io')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'open browser blender':
    webbrowser.open_new_tab('https://www.blender.org')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'open browser python':
    webbrowser.open_new_tab('https://www.python.org')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'open browser jdk':
    webbrowser.open_new_tab('https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'open browser java':
    webbrowser.open_new_tab('https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html')
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == java1:
    webbrowser.open_new_tab('https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html')
    print("type help! to see all commands")
    print(thankyou)

elif command1 == python1:
    webbrowser.open_new_tab('https://www.python.org')
    print("type help! to see all commands")
    print(thankyou)

elif command1 == 'open browser spotify':
    webbrowser.open_new_tab('https://www.spotify.com')
    print(help1)
    print(thankyou)

elif command1 == 'download c#':
    webbrowser.open_new_tab('https://dotnet.microsoft.com/download/dotnet-framework')
    print(help1)
    print(thankyou)

elif command1 == 'download donut':
    webbrowser.open_new_tab('https://dotnet.microsoft.com/download/dotnet-framework')
    print(help1)
    print(thankyou)

elif command1 == 'download unity c#':
    webbrowser.open_new_tab('https://dotnet.microsoft.com/download/dotnet-framework')
    print(help1)
    print(thankyou)

elif command1 == 'open browser gmail':
    webbrowser.open_new_tab('https://mail.google.com')
    print(help1)
    print(thankyou)

elif command1 == 'gmail login':
    webbrowser.open_new_tab('https://accounts.google.com/')
    print(help1)
    print(thankyou)

elif command1 == "move file":
    origin1 = input('origin:')
    target1 = input('target:')
    shutil.move(origin1,target1)
    print(thankyou)
    print(help1)
    input('press any key to exit')

elif command1 == "copy file":
    origin2 = input('origin:')
    target2 = input('target:')
    shutil.copy(origin2, target2)
    print(thankyou)
    print(help1)
    input('press any key to exit')

elif command1 == "close":
    print(thankyou)
    quit()

elif command1 == "choose random num":
    print(random.randrange(1, 1000000))
    print("tadha i am good at maths boiiiii")
    print(help1)
    print(thankyou)
    print(help1)
    input('press any key then enter to exit')

elif command1 == "choose random number":
    random_num1 = input("add first number:")
    random_num2 = input("add second number:")
    random_num3 = input("add third number:")
    random_num4 = input("add fourth number")
    random_num5 = input("add fifth num")
    list = [random_num1, random_num2, random_num3, random_num4, random_num5]
    random_number = random.choice(list)
    print(random_number)
    print(thankyou)
    print(help1)
    input(exit1)

elif command1 == "read file":
    readfile1 = input('input file name:')
    file = open(readfile1)
    print(file.read())
    input(exit1)

elif command1 == "write file":
    writefile1 = input('input file name:')
    text2 = input('input what you wanna write in that file:')
    file = open(writefile1,"w")
    print(file.write(text2))
    input(exit1)

elif command1 == "open file":
    openfile1 = input('input your file name')
    file = open(openfile1,"w")

elif command1 == "open new file":
    opennewfile = input('input your new file name')
    file = open(opennewfile,"w")

elif command1 == "close": #to close the program
    print("thanks for using me :), made by abhijeet prabhakar")
    quit()

elif command1 == "quit":
    print(thankyou)
    quit()

else:
    print("Please type the write command/",command1,error1)
    print("type help! to see all commands")
    input('press any key to close')
    quit()


