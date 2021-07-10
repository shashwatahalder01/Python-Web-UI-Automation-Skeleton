import os
import smtplib
import shutil
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
# from runconfiguration import linux


# Read counter number
def readcounter():
    # read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    # update counter
    newcounter = str(data + 1)
    # write new counter
    f.seek(0)
    f.write(newcounter)
    f.truncate()
    f.close()
    return newcounter


# Read current date
def readdate():
    return str(datetime.today().strftime('%Y-%m-%d'))


# Send mail
def sendmail(senderemail, senderpassword, receiversemail, mailsubject, mailbody, attachedfilepath, bccemail=''):
    # Mail content, format, encoding
    message = MIMEMultipart()
    message['From'] = senderemail
    message['To'] = receiversemail
    message['Subject'] = Header(mailsubject, 'utf-8')
    if bccemail:
        message['Bcc'] = bccemail
    message.attach(MIMEText(mailbody))

    # build the attachment
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(open(attachedfilepath, 'rb').read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attachedfilepath))
    message.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(senderemail, senderpassword)
        server.send_message(message)
        # server.sendmail(senderemail, receivers, message.as_string())
        print("Send email successfully!!!")
        server.close()
    except smtplib.SMTPException:
        print("Failed to send mail!!!")


# Delete Folder and its content except last n number of dirs
def deldir(num_of_dir):
    basedir = Path(__file__).resolve().parent.parent
    dirname = "ReportAllure"
    dirpath = os.path.join(basedir, dirname)
    # print(dirPath)
    # dirList = [f for f in sorted(os.listdir(dirPath))]
    dirlist = [os.path.join(dirpath, f) for f in sorted(os.listdir(dirpath))]
    dirlist = dirlist[:len(dirlist) - num_of_dir]
    # print(dirList)
    for folder in dirlist:
        try:
            shutil.rmtree(folder)
            # print('delete: ' + delDir)
        except OSError as e:
            print("Error: %s : %s" % (folder, e.strerror))
        # print('dir deleted')


# Delete file except last n number of files
def delfile(num_of_file):
    basedir = Path(__file__).resolve().parent.parent
    dirname = "ReportHtml"
    dirpath = os.path.join(basedir, dirname)
    filelist = [os.path.join(dirpath, f) for f in sorted(os.listdir(dirpath))]
    filelist = filelist[:len(filelist) - num_of_file]
    # print(fileList)
    for file in filelist:
        os.remove(file)


def keepreports(number):
    deldir(number)
    delfile(number)


def sendemail(sender, password, receivers):
    bccemail = ''
    emailsubject = 'Test Report'
    emailbody = "Dear Sir, Please check this report."
    attachedfilepath = ''
    attachedfilepath = Path(__file__).parent / f"../ReportHtml/report_{readdate()}_{readcounter()}.html"
    # attachedfilepath = Path(__file__).parent / f"../ReportHtml/report_2021-05-05_47.html"
    sendmail(sender, password, receivers, emailsubject, emailbody, attachedfilepath, bccemail)


# def connectionoff():
#     if linux:
#         # connectionOff = "nmcli networking off"
#         connectionOff = "nmcli r wifi off"
#         os.system(connectionOff)
#     else:
#         connectionOff = "netsh wlan disconnect"
#         os.system(connectionOff)
#
#
# def connectionon():
#     if linux:
#         # connectionOn = "nmcli networking on"
#         connectionOn = "nmcli r wifi on"
#         os.system(connectionOn)
#     else:
#         connectionOn = 'netsh wlan connect name="network_name"'
#         os.system(connectionOn)
