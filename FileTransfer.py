import csv
import os
import shutil

path = "H:\Courses\Data Warehousing & Business Intelligence\Classroom Materials\Week 4"
extension = "csv"
fileList = os.listdir(path)
destDir = "F:\DWBIFiles"
if not os.path.exists(destDir):
    os.mkdir(destDir)

# Copy files which needs to be processed to a new directory
for file in fileList:
    fileName, fileExtension = os.path.splitext(file)
    if fileExtension == ".csv":
        if "Clinic_Group_Practice_Reassignment" in fileName:
            if not os.path.exists(destDir + "\\" + file):
                shutil.copy(path + "\\" + file, destDir)
            else:
                exit(0)

# Check if values in the cell contain any special character ';' and then update the delimiter of the file as ';'
i = 1
for file in os.listdir(destDir):
    src = destDir + "\\" + file
    destFileName = "CGPR_" + str(i) + ".csv"
    dst = destDir + "\\" + destFileName
    with open(src, mode="rU") as inFile:
        reader = csv.reader(inFile, delimiter=",", dialect="excel")
        rows = list(reader)

        for row in rows:
            if ";" in row[2]:
                row[2] = row[2].replace(';', ",")

        with open(dst, mode="w") as outFile:
            writer = csv.writer(outFile, delimiter=";")
            writer.writerows(rows)
    i += 1
