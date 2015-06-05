import os
import zipfile
total=0

table = [[0 for i in range(2)] for j in range (30)]




for dirname, dirnames, filenames in os.walk('.',topdown=False):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

#------------------------------------------------------------------------
        #table[total][0]=subdirname

        #total+=1
        #print total


#---------------------------------------------------------------------

        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))


rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)
    total_size=0
    for fname in fileList:
        print('\t%s' % fname)
        fp=os.path.join(dirName,fname)
        total_size+=os.path.getsize(fp)
    table[total][0]=dirName
    table[total][1]=total_size
    total+=1
    print(total_size)

total=total-1
    ## Advanced usage:
    ## editing the 'dirnames' list will stop os.walk() from recursing into there.
#if '.git' in dirnames:
        ## don't go into any .git directories.
        #dirnames.remove('.git')

print table

dirlist=[0 for i in range(total)]

for i in range (total):

    if (table[i][1]<2000000) :
        print table [i][0]
        dirlist[i]=table[i][0]

#total gives the total number of directories that have to be archived
print total
print dirlist
index=0
# total_archive_size is used to check whether every archive created is less than the allowed size. for eg. less than 2MB
total_archive_size=0

count_archive=1 #count of the nos. of archives


index=0
while (total>0):
    total_archive_size=0
    archive='archive'
    archive+=`count_archive`
    count_archive+=1
    archive+='.zip'
    zipg = zipfile.ZipFile(archive, 'w')
    while(total_archive_size+table[index][1]<2000000):
        directory=table[index][0]
        total_archive_size+=table[index][1]
        total-=1
        #print 'directory'+directory
        for root,subdirs,files in os.walk(directory):
            for file in files:
                zipg.write(os.path.join(root,file))
        index+=1
        print total_archive_size+table[index][1]

zipg.close


