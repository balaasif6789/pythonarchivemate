import os
import zipfile

table=[[0 for i in range(2)]for j in range(30)]
dirs=os.walk('.').next()[1]
total=0
index=0

for dir in dirs:

    total+=1
    total_size=0

    for root, dirs, files in os.walk(dir):
        for file in files:
            fp=os.path.join(root,file)
            total_size+=os.path.getsize(fp)
    table[index][0]=dir
    table[index][1]=total_size
    index+=1

index=0
archive_number=0
while (total>0):
    archive_number+=1
    archive='POC'+`archive_number`+'.zip'
    zipg=zipfile.ZipFile(archive,'w')
    archive_size=0

    while(archive_size+table[index][1]<2000000):
        directory=table[index][0]
        for root, dirs, files in os.walk(directory):
            for file in files:
                zipg.write(os.path.join(root,file))
        archive_size+=table[index][1]
        index+=1
        total-=1
        if total==0:
            break
