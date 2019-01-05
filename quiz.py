#For login use admin username as "admin" and admin password as "password"


import os

playerlist = []
questionlist = []
mainchoice = 'y'
usr = "admin"
pas = "password"
qno = 0
while(mainchoice == 'y'):
	print "**************WELCOME**************"
	print "(1). Admin"
	print "(2). Player"
	print "(3). Exit"
	choice = input("Enter your choice : ")
	if(choice == 1):
		os.system('clear')
		print "**************ADMIN LOGIN**************"
		admusrnm = raw_input("Enter username : ")
		admpass = raw_input("Enter password : ")
		if(admusrnm == usr and admpass == pas):
			ch = 'y'
			while(ch == 'y'):
				os.system('clear')
				print "**************ADMIN**************"
				print "(1). Add player"
				print "(2). Update Player"
				print "(3). Delete Player"
				print "(4). Update Admin Profile"
				print "(5). Add questions"
				print "(6). Update question"
				print "(7). Delete question"
				print "(8). Player report"
				print "(9). Search player report"
				print "(10). Logout"
				admch = input("Enter your choice : ")
				if(admch == 1):
					addplayer = 'y' 
					os.system('clear')
					while(addplayer == 'y'):
						print "**************ADD PLAYER**************"
						newplayer = []
						name = raw_input("Enter name : ")
						newplayer.append(name)
						clas = raw_input("Enter class : ")
						newplayer.append(clas)
						reg = input("Enter registration number : ")
						newplayer.append(reg)
						uname = raw_input("Enter username : ")
						newplayer.append(uname)
						upass = raw_input("Enter password : ")
						newplayer.append(upass)
						tmarks = 0;
						newplayer.append(tmarks)
						playerlist.append(newplayer)
						addplayer = raw_input("Do you want to add more player ? (y/n)  ")
				elif(admch == 2):
					updatechoice = 'y'
					while(updatechoice == 'y'):
						os.system('clear')
						print "**************UPDATE PLAYER**************"
						count = 0
						name = raw_input("Enter name of player to update : ")
						for i in range(len(playerlist)):
							if(playerlist[i][0] == name):
								count = 1;
								reg = input("Enter new registration number : ")
								playerlist[i][2] = reg;
						if(count == 0):
							print "Player not found."
						updatechoice  = raw_input("Do you want to update more player ? (y/n) ")
				elif(admch == 3):
					delplayer = 'y'
					while(delplayer == 'y'):
						os.system('clear')
						print "**************DELETE PLAYER**************"
						count = 0
						name = raw_input("Enter name of player to be deleted : ")
						for i in playerlist[:]:
							if(i[0] == name):
								count = 1;
								playerlist.remove(i)
								print "Player Deleted"
						if(count == 0):
							print "Player not found."
						delplayer = raw_input("Do you want to delete more player ? (y/n) ")
				elif(admch == 4):
					os.system('clear')
					print "**************UPDATE ADMIN PROFILE**************"
					usr = raw_input("Enter username : ")
					pas = raw_input("Enter password : ")
					print "Profile updated !"
				elif(admch == 5):
					addq = 'y'
					while(addq == 'y'):
						os.system('clear')
						print "**************ADD QUESTION**************"
						qno += 1
						newquestion = []
						newquestion.append(qno)
						question = raw_input("Enter Question : ")
						newquestion.append(question)
						option1 = raw_input("Enter option 1 : ")
						newquestion.append(option1)
						option2 = raw_input("Enter option 2 : ")
						newquestion.append(option2)
						option3 = raw_input("Enter option 3 : ")
						newquestion.append(option3)
						option4 = raw_input("Enter option 4 : ")
						newquestion.append(option4)
						answer = input("Enter answer : ")
						newquestion.append(answer)
						questionlist.append(newquestion)
						addq = raw_input("Do you want to add more question ? (y/n)  ")
				elif(admch == 6):
					updateq = 'y'
					while(updateq == 'y'):
						os.system('clear')
						print "**************UPDATE QUESTION**************"
						count = 0
						qnumber = input("Enter question number to update : ")
						for i in range(len(questionlist)):
							if(questionlist[i][0] == qnumber):
								count = 1;
								question = raw_input("Enter Question : ")
								questionlist[i][1] = question
								option1 = raw_input("Enter option 1 : ")
								questionlist[i][2] = option1
								option2 = raw_input("Enter option 2 : ")
								questionlist[i][3] = option2
								option3 = raw_input("Enter option 3 : ")
								questionlist[i][4] = option3
								option4 = raw_input("Enter option 4 : ")
								questionlist[i][5] = option4
								answer = input("Enter answer : ")
								questionlist[i][1] = answer
						if(count == 0):
							print "Question not found."
						updateq = raw_input("Do you want to update more question ? (y/n) ")
				elif(admch == 7):
					delq = 'y'
					while(delq == 'y'):
						os.system('clear')
						print "**************DELETE Question**************"
						count = 0
						qnumber = input("Enter question number to be deleted : ")
						for i in questionlist[:]:
							if(i[0] == qnumber):
								count = 1;
								questionlist.remove(i)
								print "Question Deleted"
						if(count == 0):
							print "Question not found."
						delq = raw_input("Do you want to delete more questions ? (y/n) ")
				elif(admch == 8):
					os.system('clear')
					report = 'n'
					while(report == n):
						print "**************PLAYER REPORT**************"
						for i in range(len(playerlist)):
							for j in range(len(playerlist[i])):
								print playerlist[i][j],
							print ""
						report = raw_input("Pree y to exit the player report : ")
				elif(admch == 9):
					src = 'y'
					while(src == 'y'):
						os.system('clear')
						print "**************SEARCH PLAYER REPORT**************"
						reg = input("Enter registration number : ")
						for i in range(len(playerlist)):
							if(playerlist[i][2] == reg):
								print playerlist[i][0],playerlist[i][1],playerlist[i][2],playerlist[i][3],playerlist[i][4],playerlist[i][5]
								break
						src = raw_input("Do you want to search more player ? (y/n) ")
				else:
					os.system('clear')
					print "Thank you!"
					ch = 'n'
		else:
			print "Wrong Credentials !"
	elif(choice == 2):
		os.system('clear')
		print "**************HELLO PLAYER**************"
		flag = 0
		playerusrname = raw_input("Enter your username : ")
		playerusrpass = raw_input("Enter your password : ")
		for i in range(len(playerlist)):
			if(playerlist[i][3] == playerusrname and playerlist[i][4] == playerusrpass):
				print "in if"
				flag = 1
				for j in range(len(questionlist)):
					print "in for"
					print "(", questionlist[j][0], ")", "  ", questionlist[j][1]
					print "      (1). ", questionlist[j][2]
					print "      (2). ", questionlist[j][3]
					print "      (3). ", questionlist[j][4]
					print "      (4). ", questionlist[j][5]
					answer = input("Enter your answer : ")
					if(questionlist[j][6] == answer):
						playerlist[i][5] = playerlist[i][5] + 1
					print "Your current score : ", playerlist[i][5]
				print "Your total score : ", playerlist[i][5]
		if(flag == 0):
			print "Wrong Credentials"
	else:
		os.system('clear')
		mainchoice = 'n'
		print "Thnak you!"
