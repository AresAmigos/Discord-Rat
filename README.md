# Discord-Rat

# Educational purpose only


The file is available only in italian (half Italian and half English, lol)


A rat that uses discord server (discord bot and a discord webhook) as console, obviously it uses discord also as proxy.


This rat work only on windows


First of explicate every single rat command: DON'T USE THIS FOR MAKE ANY BULLSHIT, I DO NOT TAKE ANY RESPONSIBILITY OF THE WAY YOU WILL USE IT.


modify the line 1 and 2 with your bot token and webhook url


The prefiss of every command is: ")"


bomb - fills the pc with garbage files

bomb 100 (it will fill the victim machine with 100 unusefull files)


cd - change directory

cd C:/users/USERNAME (enter the victim machine username instead of USERNAME, can use 'cmd "echo %username%"' to get it)


chromepws - sends with webhook a text file with victim machine chrome password

no parameters


cls - clear every message in the discord chat

no parameters


cmd - sends an input to the cmd and returns the output to a text file sent to discord

cmd dir (without quotation marks if the word is one) else cmd "shutdown -s -t 0" (if there are more words)


cmdput - sends an input to the cmd and executes the command on the victim machine

identical to cmd but the output is done on the victim machine


desktop - sends the input "win + D" to the victim machine keyboard

no parameters


desktopbomb - spams the desktop with x (where x is a number) text file

desktopbomb 4 (will spam the desktop with 4 text file)



download - download a file on victim machine, if the complete path is not specified the file will be downloaded in downloads folder

download link file_path.extension



dstoken - steal the discord token of the victim

no parameters


grab - take a file from the current directory and send it to discord, you can also enter the entire path

grab C:/users/USERNAME/desktop/test.txt  or  grab test.txt if you're already in the file directory


help - shows all commands


no parameters


ifconfig - show ifconfig information except user agent

no parameters


input - sends a input on the victim machine keyboard

input Hello (use curly brackets for special keys, example: {enter} {F4})


lclick - sends x (where x is a number) left click

lclick 20 (will send 20 left clicks)


mousemad - it will drive the mouse crazy for x (where x is a number) seconds

mousemad 4 (it will drive the mouse crazy for 4 seconds)


msgboxE - spam the screen of victim machine with error windows

msgboxE 5 (will spam 5 error messages on the victim machine)


ping - check the connection speed of the victim machine by sending the output to a text file on discord

ping 4 (sends 4 packages)


print - will send the following message to discord

print lol (will send lol on discord) if there are spaces use quotation marks, example: print "Hello world!"


purge - will delete x (where x is a number) messages on the discord channel

purge 5 (will delete 5 messages on the discord channel)


rclick - sends x (where x is a number) right click

rclick 20 (will send 20 right clicks)


screen - make a screenshot of the victim machine screen and will send it on discord

no parameters


sendmsg - will send a message to the victim machine

sendmsg Hello (will send Hello to the victim machine) also here if there are space use quotation marks


shutdown - it will permanently delete the rat from the victim machine without leaving any traces

shutdown bot (bot is the only paremeter) - work in progress


so - will send on discord the operation system of victim machine (pretty unuseful because this rat works only on windows)

no parameters


spamcmd - will spam x (where x is a number) cmd windows

spamcmd 3 (will spam 3 cmd windows)


sysinfo - will send the system info of victim machine

no parameters


wclose - sends the output "alt + F4" on the victim machine

no parameters
