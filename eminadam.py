#########################
#__ .     ¨   ~     . ¨ #
#  \__  By Vahema    ___#
#     \     ¨  .    /   #
#########################

from func import *

os.system("sudo echo \"\"")
banner()

print("Type \"help\" for help")
msg = random.choice(range(4))

if msg == 2:
	print(f"Did {fred}u know?{fwhite}, shell is a simple \"calculator\"\n")
elif msg == 4:
	print(f"{fred}Eminadam{fwhite} is the one who hacks google")

run = True
while run:
	ui = input("EMN> ")
	command_error = f"\n{fred}[E]{fwhite} Command \"{ui}\" not found\n"

	if ui == "help":
		help()
	elif ui == "restart":
		restart()
	elif ui == "update":
		update()
	elif ui == "clear":
		clear()
	elif "echo" in ui:
		print(ui[4:])
	elif ui == "dos":
		dos()
	elif ui == "exit":
		os.system("clear")
		run = False
	elif "+" in ui or "-" in ui or "/" in ui or "*" in ui:
		print(eval(ui))
		if "%" in ui:
			print(f"{fred}Simple{fwhite} calculator")
	elif ui == "instappi":
		instappi()
	#elif ui == "ip":
	#	instappi2()

	else:
		print(command_error)

os.system("clear")