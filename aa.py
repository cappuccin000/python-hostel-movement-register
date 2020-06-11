import datetime
import os
def write():
    count=int(raw_input("How many students:"))
    fo=open("student10.det","a")
    for i in range(count):
        print"Enter details:"
        branch=raw_input("Enter branch:")
        roomno=int(raw_input("roomno:"))
        name=raw_input("name:")
        c=datetime.datetime.now()
        d=str(c)
        num1=branch.upper()
        num2=name.upper()
        rec="Branch:"+num1+"    ,   "+"Room No:"+str(roomno)+" ,   "+"Name:"+num2+"    ,   "+"Date&Time:"+d+'\n'        
        fo.write(rec)
    fo.close()
def read():
    fi=open("student10.det","r")
    str=" "
    while str:
        str=fi.readline()
        print str,
    fi.close()



def write1():
    count=int(raw_input("How many students:"))
    fo=open("student20.det","a")
    for i in range(count):
        print"Enter details:"
        branch=raw_input("Enter branch:")
        roomno=int(raw_input("roomno:"))
        name=raw_input("name:")
        c=datetime.datetime.now()
        d=str(c)
        num1=branch.upper()
        num2=name.upper()
        rec="Branch:"+num1+"    ,   "+"Room No:"+str(roomno)+" ,   "+"Name:"+num2+"    ,   "+"Date&Time:"+d+'\n'        
        fo.write(rec)
    fo.close()


def read1():
    fi=open("student20.det","r")
    str=" "
    while str:
        str=fi.readline()
        print str,
    fi.close()


def del1(q):
    fi=open("student10.det","r")
    ft=open("temp.det","w")
    count=0
    rec=" "
    while rec:
        rec=fi.readline()
        count=count+1
        if count==q:
            pass
        else:
            ft.write(rec)
    fi.close()
    ft.close()
    os.remove("student10.det")
    os.rename("temp.det","student10.det")



def del2(c1):
    fi=open("student20.det","r")
    ft=open("temp1.det","w")
    count=0
    rec=" "
    while rec:
        rec=fi.readline()
        count=count+1
        if count==q:
            pass
        else:
            ft.write(rec)
    fi.close()
    ft.close()
    os.remove("student20.det")
    os.rename("temp1.det","student20.det")
    


  #------------------------------------main  program-------------------------------


print"Hostel Movement  Register:"
print"********************************"
while (True):
    print "0.Exit","\n1.Admin","\n2.Student"

    k=int(raw_input("Enter your choice:"))
    if k==0:
        print"Thanks For Using"
        break
    elif k==1:
        print "Welcome Admin:"
        print"Press 1. to View Entry Register:"
        print"Press 2. to View Exit Register:"
        print"Press 3. to Delete Entries:"
        n=int(raw_input("Enter your choice:"))
        if n==1:
            m=raw_input("Enter password:")
            if m=="****":
                read()
        elif n==2:
            m=raw_input("Enter password:")
            if m=="****":
                read1()
            else:
                print"incorrect password"
        elif n==3:
            p=raw_input("Enter password:")
            if p=="****":
                choice=int(raw_input("1.Entry\n2.Exit\n==>"))
                if choice==1:
                    q=int(raw_input("Enter the column to be deleted:"))
                    r=raw_input("Do you really want to delete entry?(y/n):")
                    if r=="y":
                        del1(q)
                        read()
                    else:
                        continue
                elif choice==2:
                    c1=int(raw_input("Enter the column to be deleted:"))
                    r1=raw_input("Do you really want to delete entry?(y/n):")
                    if r1=="y":
                        del2(c1)
                        read1()
                    else:
                        continue
                else:
                    print"Enter valid choice:"
                    continue
            else:
                print "incorrect password"
    elif k==2:
        print"Welcome :"
        print"1.Entry\n2.Exit"
        z=int(raw_input("Enter your choice:"))
        if z==1:
            write()
        elif z==2:
            write1()
        else:
            print"Invalid Entry"
            continue
        
            


