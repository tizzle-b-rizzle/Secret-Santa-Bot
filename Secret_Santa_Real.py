import random
import smtplib

array_of_emails = [
"tylerrooker@hotmail.com",
"lukehudson66@gmail.com",
"christindall11@hotmail.com",
"louiehaslamchance@gmail.com"
]

array_of_emails.remove("tylerrooker@hotmail.com") #gives me mine
rec_email_tyler = array_of_emails[random.randint(0,2)]

array_of_emails = [ #gives me Luke's
"tylerrooker@hotmail.com",
"lukehudson66@gmail.com",
"christindall11@hotmail.com",
"louiehaslamchance@gmail.com"
]
if rec_email_tyler == "lukehudson66@gmail.com":
    rec_email_luke = array_of_emails.remove("lukehudson66@gmail.com")
if rec_email_tyler != "lukehudson66@gmail.com":
    array_of_emails.remove("lukehudson66@gmail.com")
    rec_email_luke = array_of_emails.remove(rec_email_tyler)
rec_email_luke = array_of_emails[random.randint(0, len(array_of_emails) - 1)]

array_of_emails = [ #gives my Louie's
"tylerrooker@hotmail.com",
"lukehudson66@gmail.com",
"christindall11@hotmail.com",
"louiehaslamchance@gmail.com"
]
if rec_email_tyler == "louiehaslamchance@gmail.com":
    array_of_emails.remove("louiehaslamchance@gmail.com")
    array_of_emails.remove(rec_email_luke)
elif rec_email_luke == "louiehaslamchance@gmail.com":
    array_of_emails.remove("louiehaslamchance@gmail.com")
    array_of_emails.remove(rec_email_tyler)
elif rec_email_tyler != "louiehaslamchance@gmail.com" and rec_email_luke != "louiehaslamchance@gmail.com":
    array_of_emails.remove("louiehaslamchance@gmail.com")
    array_of_emails.remove(rec_email_tyler)
    array_of_emails.remove(rec_email_luke)
rec_email_louie = array_of_emails[random.randint(0, len(array_of_emails) - 1)]

array_of_emails = [ #gives me Chris'
"tylerrooker@hotmail.com",
"lukehudson66@gmail.com",
"christindall11@hotmail.com",
"louiehaslamchance@gmail.com"
]
if rec_email_tyler == "christindall11@hotmail.com":
    array_of_emails.remove("christindall11@hotmail.com")
    array_of_emails.remove(rec_email_luke)
    array_of_emails.remove(rec_email_louie)
elif rec_email_louie == "christindall11@hotmail.com":
    array_of_emails.remove("christindall11@hotmail.com")
    array_of_emails.remove(rec_email_luke)
    array_of_emails.remove(rec_email_tyler)
elif rec_email_luke == "christindall11@hotmail.com":
    array_of_emails.remove("christindall11@hotmail.com")
    array_of_emails.remove(rec_email_louie)
    array_of_emails.remove(rec_email_tyler)
rec_email_chris = array_of_emails[0]

sender_email= "tizsecretsantabot@gmail.com"
password = input("Please type in your password:\n")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
print("Login successful")
server.sendmail(sender_email, "tylerrooker@hotmail.com", "Your secret santa person is " + rec_email_tyler)
server.sendmail(sender_email, "lukehudson66@gmail.com", "Your secret santa person is " + rec_email_luke)
server.sendmail(sender_email, "louiehaslamchance@gmail.com", "Your secret santa person is " + rec_email_louie)
server.sendmail(sender_email, "christindall11@hotmail.com", "Your secret santa person is " + rec_email_chris)
print("Done!")


