import traceback
import binascii
import textwrap
import sys

try:
    def create_file(filelists):
        if not filelists:
            print "No file exists"
            sys.exit(0)

        filenames = []
        filepaths=[]
        extension='.pem.cert'

        for filelist in filelists:
            with open(filelist[0]+extension, 'w') as file_obj:
                data=filelist[1]
                dec_data=binascii.b2a_base64(data)
                pem_data = '\n'.join(textwrap.wrap(dec_data, 64))
                file_obj.write("-------BEGIN CERTIFICATE-------\n")
                file_obj.write(pem_data)
                file_obj.write("\n-------END CERTIFICATE-------")
                filenames.append(filelist[0]+extension)
                filepaths.append(filelist[2])
        return filenames,filepaths

except IOError as e:
    print "I/O Error"
except Exception:
    print (traceback.format_exc())