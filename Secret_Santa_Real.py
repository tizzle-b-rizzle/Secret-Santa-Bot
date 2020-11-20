import random #allows me to get random numbers
import smtplib #allows me to send emails

array_of_emails = [ #the list of mine and my friend's email addresses
"tylerrooker@hotmail.com",
"lukehudson66@gmail.com",
"christindall11@hotmail.com",
"louiehaslamchance@gmail.com"
]

array_of_emails.remove("tylerrooker@hotmail.com") #takes my email out of the list, and then gives me a random email from what's left
rec_email_tyler = array_of_emails[random.randint(0,2)]

array_of_emails = [ #re-setting the email list for Luke's secret santa person
"tylerrooker@hotmail.com",
"lukehudson66@gmail.com",
"christindall11@hotmail.com",
"louiehaslamchance@gmail.com"
]
if rec_email_tyler == "lukehudson66@gmail.com": #if my (Tyler's) person was Luke, only take Luke's email out of the list
    rec_email_luke = array_of_emails.remove("lukehudson66@gmail.com")
if rec_email_tyler != "lukehudson66@gmail.com": #if my person WASN'T Luke, take out Luke's email, and then whoever my person was
    array_of_emails.remove("lukehudson66@gmail.com")
    rec_email_luke = array_of_emails.remove(rec_email_tyler)
rec_email_luke = array_of_emails[random.randint(0, len(array_of_emails) - 1)] #Luke gets a random email from whatever's in the list

array_of_emails = [ #re-setting the email list for Louie's secret santa person
"tylerrooker@hotmail.com",
"lukehudson66@gmail.com",
"christindall11@hotmail.com",
"louiehaslamchance@gmail.com"
]
if rec_email_tyler == "louiehaslamchance@gmail.com": #if my person was Louie, take out Louie's email, and Luke's person from the list
    array_of_emails.remove("louiehaslamchance@gmail.com")
    array_of_emails.remove(rec_email_luke)
elif rec_email_luke == "louiehaslamchance@gmail.com": #if Luke's person was Louie, take out Louie's email and my person from the list
    array_of_emails.remove("louiehaslamchance@gmail.com")
    array_of_emails.remove(rec_email_tyler)
elif rec_email_tyler != "louiehaslamchance@gmail.com" and rec_email_luke != "louiehaslamchance@gmail.com": #if both mine AND Luke's person were not Louie,
    array_of_emails.remove("louiehaslamchance@gmail.com")                                                  #take out my person, Luke's person, and then Louie's email 
    array_of_emails.remove(rec_email_tyler)
    array_of_emails.remove(rec_email_luke)
rec_email_louie = array_of_emails[random.randint(0, len(array_of_emails) - 1)] #Louie gets a random email from what's left

array_of_emails = [ #re-setting the email list for Chris' secret santa person
"tylerrooker@hotmail.com",
"lukehudson66@gmail.com",
"christindall11@hotmail.com",
"louiehaslamchance@gmail.com"
]
if rec_email_tyler == "christindall11@hotmail.com": #If my person was Chris, remove Chris' email, and then Luke and Louie's people
    array_of_emails.remove("christindall11@hotmail.com")
    array_of_emails.remove(rec_email_luke)
    array_of_emails.remove(rec_email_louie)
elif rec_email_louie == "christindall11@hotmail.com":
    array_of_emails.remove("christindall11@hotmail.com") #If Louie's person was Chris, Remove Chris' email, and then Luke's and my people
    array_of_emails.remove(rec_email_luke)
    array_of_emails.remove(rec_email_tyler)
elif rec_email_luke == "christindall11@hotmail.com": #If Luke's person was Chris, remove Chris' email, then Louie's then mine
    array_of_emails.remove("christindall11@hotmail.com")
    array_of_emails.remove(rec_email_louie)
    array_of_emails.remove(rec_email_tyler)
rec_email_chris = array_of_emails[0] #There's only one person left, so Chris gets whoever that is

sender_email= "tizsecretsantabot@gmail.com" #the email of the bot
password = input("Please type in your password:\n") #asks for my password (if you decide to use the bot, I'll give you the password of course)
server = smtplib.SMTP("smtp.gmail.com", 587) #connects to gmail server
server.starttls() #starts going on the gmail server
server.login(sender_email, password) #logs into gmail using the email address of the bot, and the password I/you typed in
print("Login successful") #If it logs in fine, you get this message
server.sendmail(sender_email, "tylerrooker@hotmail.com", "Your secret santa person is " + rec_email_tyler) #emails me "Your secret santa person is " and then who I got
server.sendmail(sender_email, "lukehudson66@gmail.com", "Your secret santa person is " + rec_email_luke) #These next three are the same but for Luke, Louie, and Chris respectivley
server.sendmail(sender_email, "louiehaslamchance@gmail.com", "Your secret santa person is " + rec_email_louie)
server.sendmail(sender_email, "christindall11@hotmail.com", "Your secret santa person is " + rec_email_chris)
print("Done!") #if that works, you get this message


