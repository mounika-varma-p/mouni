eid=int(input("Enter eid"))
ename=input("Enter ename")
esal=int(input("Enter esal"))
deptnum=int(input("Enter deptnum"))
comm=int(input("Enter a comm"))
if esal>15000 and deptnum==1 and comm!=0:
    esal=esal+5000
    print(eid,"    ",ename, "    ",esal,"    ",deptnum)
else:
    print("the person is not eligible for incre")