import os
import datetime
import exifread

# Set Directory
os.chdir('Q:/DCIM/test/dcim')
# Am I in the correct directory?
# print(os.getcwd())
# print(dir(os))

for f in os.listdir(os.getcwd()):
    # Skip system files and folders
    if f[0] == '.':
        continue
    if os.path.isdir(f):
        continue
    try:
        # Get file properties
        file_name, file_ext = os.path.splitext(f)
        file_ext = file_ext.lower()

        jpg_file = open(f, 'rb')
        jpg_tags = exifread.process_file(jpg_file, details=False, stop_tag='EXIF DateTimeOriginal')
        jpg_file.close()
        print(file_name + file_ext)
        # Extract date and time into individual components
        date, time = str(jpg_tags['EXIF DateTimeOriginal']).split()
        ymd = date.split(":")
        hms = time.split(":")
        # Format new name
        new_name = "%s-%s-%s %s.%s.%s" % (ymd[0], ymd[1], ymd[2], hms[0], hms[1], hms[2])
        # Format new path
        month_long = ymd[1] + ' ' + datetime.date(2000, int(ymd[1]), 1).strftime('%B')
        new_path = ymd[0] + '/' + month_long
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        # Note the slash between path and name
        print("%s/%s%s" % (new_path, new_name, file_ext))
##        # Auto-renames "duplicate" files
##        suffixN = 0
##        suffix = ""
##        while suffixN < 10:
##            if os.path.exists((new_path + "/" + new_name + suffix + file_ext)):
##                suffixN += 1
##                suffix = "-" + str(suffixN)
##            else:
##                os.rename(f, "%s/%s%s%s" % (new_path, new_name, suffix, file_ext))
##                break
        os.rename(f, "%s/%s%s" % (new_path, new_name, file_ext))
    except WindowsError, e:
        print e
    except KeyError, e:
        print "[KeyError] " + str(e) + " not found"
    
