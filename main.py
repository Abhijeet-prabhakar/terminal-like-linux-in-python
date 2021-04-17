import webbrowser
import shutil
error1 = ":Command not found"
thankyou = "thanks for using me :), made by abhijeet prabhakar"
java1 = "java download"
python1 = "python download"
help1 = "type help! to see all commands"
duh1 = 'r'

command1 = input("add a command:")
if command1 == "open browser":
    webbrowser.open('https://www.bing.com', new=1)
    print("type help! to see all commands")
    print("thanks for using me :), made by abhijeet prabhakar")

elif command1 == 'help!':
    print('commands: python download, java download, open browser, open browser youtube, open browser github')
    print('open browser spotify, open browser stackoverflow, close, quit, open browser java, open browser jdk')
    print('close, move file, download c#, download donut, download unity c#, open browser gmail')

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

elif command1 == "close":
    print(thankyou)
    quit()

elif command1 == "close": #to close the program
    print("thanks for using me :), made by abhijeet prabhakar")
    quit()

elif command1 == "quit":
    print(thankyou)
    quit()

else:
    print("Please type the write command/",command1,error1)
    print("type help! to see all commands")
    quit()


