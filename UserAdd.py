import os
import subprocess
import csv
import re
def main():
    with open('Lab02_Usernames.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        IDNums=[]
        lastNames=[]
        firstNames=[]
        offices=[]
        phoneNums=[]
        departments=[]
        groups=[]
        fields=[]
        fields.extend([IDNums,lastNames,firstNames,offices,phoneNums,departments,groups])
        usernames=[]
        passnum=1;
        for row in readCSV:
            if passnum==1:
                passnum += 1
                pass
            else:
                for x in range(0,len(fields)):
                    fields[x].append(row[x])
        for x in range(0,len(fields[1])):
            if firstNames[x]!="" and lastNames[x]!="":
                username=firstNames[x][0]+lastNames[x]
                username=username.lower()
                username=re.sub("[^a-z]","",username)
                while True:
                    if username in usernames:
                        username+="1"
                    else:
                        usernames.append(username)
                        break
            else:
                usernames.append("")
                pass
        for x in range(0,len(fields)):
            case=0
            for y in range(0,len(fields[x])):
                if fields[y][x]=="" and y!=3 and y!=4:
                    print("BAD RECORD: Employee ID= " + IDNums[x])
                    case=1
                else:
                    pass
            if case!=1:
                try:
                    subprocess.run(["sudo", "-S", "groupadd", "-f", groups[x]])
                    subprocess.run(["sudo", "useradd", "-m", "-d", "/home/"+groups[x]+"/"+usernames[x],"-s", "/bin/bash", "-g", groups[x], "-c", "\""+firstNames[x]+" "+lastNames[x]+"\"", usernames[x]])
                    subprocess.run(["sudo", "passwd", "--stdin", usernames[x]])
                    subprocess.run(["sudo", "passwd", "-e", usernames[x]])
                except:
                    print("BAD RECORD: Employee ID= "+IDNums[x])

main()