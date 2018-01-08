import os
import datetime

os.chdir('Q:/DCIM/test/dcim')
# os.chdir('Q:/DCIM/')

# Am I in the correct directory?
# print(os.getcwd())

# print(dir(os))

# Print all the current file names
for f in os.listdir(os.getcwd()):
    # If .DS_Store file is created, ignore it
    if f[0] == '.':
        continue

    file_name, file_ext = os.path.splitext(f)
    print(file_name)
    ymd = file_name.split(' ') 

    # One way to do this
    f_year, f_month, f_day = ymd[0].split('-')
    f_month = f_month + ' ' + datetime.date(2000, int(f_month), 1).strftime('%B')
    new_name = f_year + '/' + f_month + '/' + file_name + file_ext
    if not os.path.exists(f_year + '/' + f_month):
        os.makedirs(f_year + '/' + f_month)
    print(new_name)
    #os.rename(fn, new_name)
    os.rename(f, new_name)


# print(len(os.listdir()))
