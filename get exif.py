import exifread

jpg_file = open("Q:/DCIM/test/dcim/100B7692.JPG", 'rb')
tags = exifread.process_file(jpg_file)
date, time = str(tags['EXIF DateTimeOriginal']).split()
ymd = date.split(":")
hms = time.split(":")
print "%s-%s-%s %s.%s.%s" % (ymd[0], ymd[1], ymd[2], hms[0], hms[1], hms[2])
