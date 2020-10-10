# import pandas as pd
# import smtplib

# e = pd.read_excel("email.xlsx")
# emails = e['Emails'].values
# print(emails)

# importing pandas as pd 
import pandas as pd 
import smtplib

# Check the version 
print(pd.__version__) 

server = smtplib.SMTP('localhost',1025)
server.sendmail('abcd.com','xyz.com', 'nice') 
e = pd.read_excel("email.xlsx")
email = e['Emails']

print(email)