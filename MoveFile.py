import ftplib
import traceback

from config import *

try:
    sftp = ftplib.FTP(FTP_HOST, FTP_ID, FTP_PWD)  # Connect

    cert_file = raw_input("Enter the file name")   #Get file name from user

    source_path = "\Certificates\QCPD-Retired"
    destination_path = "\Certificates\QCPD"

    sep = "\\"

    if cert_file in sftp.nlst(source_path):
        source = source_path + sep + cert_file
        destination = destination_path + sep + cert_file

        sftp.rename(source, destination)
        print "File moved"
    else:
        print "File doesnt exist"

    sftp.quit()

except Exception:
    print (traceback.format_exc())
