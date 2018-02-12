import ftplib
import datetime
import json

from CreateFile import *
from DBTasks import *

try:
    with open('GetTimeStamp.json','r') as datafile:
        timestamp_obj= json.load(datafile)["date_time"]
        timestamp=timestamp_obj.rstrip("0")


    filelists = get_file_info(timestamp)
    filenames = create_file(filelists)[0]
    filepaths = create_file(filelists)[1]

    sftp = ftplib.FTP(FTP_HOST, FTP_ID, FTP_PWD)  # Connect
    sep='\/'

    print "Uploading Files....."

    for filename,filepath in zip(filenames,filepaths) :
        if filename in sftp.nlst():
            continue
        file_obj = open(filename, 'r')  # file to send
        myfolder =sep+filepath+sep
        sftp.cwd(myfolder)  # Change Directory
        sftp.storbinary('STOR ' + filename, file_obj)
        file_obj.close()  # Close file

    sftp.quit()

    print "Upload completed....."


except ftplib.all_errors as e:
    print "%s" %e
except Exception:
    print (traceback.format_exc())

finally:
    data = {'date_time': str(datetime.datetime.now())}
    with open('GetTimeStamp.json', 'w') as jsonfile:
        timestamp = json.dumps(data)
        jsonfile.write(timestamp)

