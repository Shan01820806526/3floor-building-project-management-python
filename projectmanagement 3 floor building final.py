'''This is a code for a civil construction project where 
a 3 floor house is need to be built. The 
resource are limited, this code will give over view of project'''
import math
masoncapacityperdayplastering=90 #sft of wall/day
masoncapacityperdaybricklaying=100
labourcapacityperday=300  #sft of wall/day
mixercapacityperday=500 #sft of wall/day
numofmasonsavailable=3
numoflaboursavailable=6
numofmixersavailable=2

def List_Project_Resources(duration,totalwallarea):
    reportfile=open("Projectreport.txt","w")
    dayspermason= totalwallarea/masoncapacityperdayplastering
    numofmasonsreq= math.ceil(dayspermason/duration)
    print(f"Mason # available: {numofmasonsavailable}",file=reportfile)
    if (numofmasonsreq<=numofmasonsavailable):
        print(f"{numofmasonsreq} Masons req for the plastering ",file=reportfile)
    else:
        print(f"{numofmasonsreq-numofmasonsavailable} Extra mason needed",file=reportfile)
    
    dayspermason= totalwallarea/masoncapacityperdaybricklaying
    numofmasonsreq= math.ceil(dayspermason/duration)
    print(f"Mason # available: {numofmasonsavailable}",file=reportfile)
    if (numofmasonsreq<=numofmasonsavailable):
        print(f"{numofmasonsreq} Masons req for the bricklaying ",file=reportfile)
    else:
        print(f"{numofmasonsreq-numofmasonsavailable} Extra mason needed",file=reportfile)
    
    
    daysperlabour= totalwallarea/labourcapacityperday
    numoflaboursreq= math.ceil(daysperlabour/duration)
    print(f"Labour # available: {numoflaboursavailable}",file=reportfile)
    if (numoflaboursreq<=numoflaboursavailable):
        print(f"{numoflaboursreq} Labour req for the project",file=reportfile)
    else:
        print(f"{numoflaboursreq-numoflaboursavailable} Extra labour needed",file=reportfile)
    
    dayspermixer= totalwallarea/mixercapacityperday
    numofmixersreq= math.ceil(dayspermixer/duration)
    print(f"Mixer # available: {numofmixersavailable}",file=reportfile)
    if (numofmixersreq<=numofmixersavailable):
        print(f"{numofmixersreq} Mixer req for the project",file=reportfile)
    else:
        print(f"{numofmixersreq-numofmixersavailable} Extra mixer needed",file=reportfile)

List_Project_Resources(300,(1220+550)*2*45)