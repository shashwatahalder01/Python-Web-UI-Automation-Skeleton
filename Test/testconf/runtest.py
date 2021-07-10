import os
from Utils.uitlsfunction import readdate, readcounter, keepreports

reportFolderName = f"{readdate()}_{readcounter()}"

# For running testCases
command = f"pytest -s --alluredir=ReportAllure/{reportFolderName} --html=ReportHtml/report_{reportFolderName}.html --self-contained-html TestCase"
os.system(command)

#  Send email
sender = 'asif.augmedix@gmail.com'
password = 'asdfqwer#12'
receivers = 'asif.rouf@augmedix.com, rouf.asifur@gmail.com'
# sendemail(sender, password, receivers)

# number of allure & html reports to keep
number = 2
keepreports(number)

# For generating report
command = f"allure serve ReportAllure/{reportFolderName}"
os.system(command)
