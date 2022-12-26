#Python Project : Clock angle projection.
def findingAngle(hh,mm):
    hh=hh%12                                            #24-Hoours Notation
    h=(hh*360)//12+(mm*360)//(12*60)                    #position of hours hand        
    m=(mm*360)//(60)                                    #position of minutes's hand
    angle=abs(h-m)                                      #calculate angle differences    
    if angle>180:                                       #consider the shorter angle and return it  
        angle=360-angle                                 
    return angle

if __name__=="__main__":                                #Clock Angle Problem  
    hh=12
    mm=00
    print(findingAngle(hh,mm))        