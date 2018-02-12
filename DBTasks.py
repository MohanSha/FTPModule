import pyodbc
import traceback

from config import *

try:
    def connect_db(db_name):
        if db_name !=CON_STR['db_name']:
            raise ValueError("Couln't connect to the database")

    def get_file_info(timestamp):
        cnxn=pyodbc.connect(CON_STR)
        cur = cnxn.cursor()
        cur.execute("SELECT Certificates.Name,Certificates.RawData,SampleTable.Path  FROM Certificates INNER JOIN CertificateHistory ON CertificateHistory.Certificate = Certificates.id INNER JOIN SampleTable ON SampleTable.Id = Certificates.Id where CertificateHistory.CreatedOn > ? ;",timestamp)

        filelists = []

        for row in cur:
            filelists.append(row)
        cnxn.close()
        return filelists

except pyodbc.Error as ex:
    print ex
except Exception:
    print (traceback.format_exc())
