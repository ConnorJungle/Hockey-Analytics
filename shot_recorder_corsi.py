import csv

def getShots():

'''    This program takes the analyst input of 5 players on the ice during 5v5 play. Then the 
    program will continuously ask you to enter a Shot For or Shot Against for those players. It 
    will then prompt you to enter if there was a scoring chance. This process will continue in till
    you tell the program to change the players on the ice.
  
    1. Enter 5 players on the ice 
    2. Enter 'f' for Shot For and 'a' for Shot Against
    3. Enter 1 or 0 for scoring chance
    4. If players on the ice change type 'change' when prompted for Shot For or Against'''

    SF = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'12':0,'13':0,'14':0,'16':0,\
          '17':0,'18':0,'19':0,'20':0,'21':0,'23':0,'24':0,'25':0,'26':0,'27':0,'28':0}
    SA = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'12':0,'13':0,'14':0,'16':0,\
          '17':0,'18':0,'19':0,'20':0,'21':0,'23':0,'24':0,'25':0,'26':0,'27':0,'28':0}

    InputOK = False
    while not InputOK:
        try:
            num1= str(input('player on ice: '))
            if num1 == 'end':
                return [['player #','shot'], SF, SA]
            num2= str(input('player on ice: '))
            num3= str(input('player on ice: '))
            num4= str(input('player on ice: '))     
            num5= str(input('player on ice: '))
       
            ShotOK = False
            while not ShotOK:
                try:
                    all_chance_f = 0
                    all_chance_a = 0
                    shot = str(input('Shot For or Shot Against: '))
                    if shot == 'f':
                        chance_f = int(input('scoring chance (1 or 0): '))
                        
                        all_chance_f += chance_f
                       
                        for k,v in SF.items():
                            if num1 == k:
                                SF[k] = v + 1
                            if num2 == k:
                                SF[k] = v + 1
                            if num3 == k:
                                SF[k] = v + 1
                            if num4 == k:
                                SF[k] = v + 1
                            if num5 == k:
                                SF[k] = v + 1

                        ShotOK = False
                    if shot == 'a':
                        chance_a = int(input('scoring chance (1 or 0): '))
                       
                        all_chance_a += chance_a
                       
                        for k,v in SA.items():
                            if num1 == k:
                                SA[k] = v + 1
                            if num2 == k:
                                SA[k] = v + 1
                            if num3 == k:
                                SA[k] = v + 1
                            if num4 == k:
                                SA[k] = v + 1
                            if num5 == k:
                                SA[k] = v + 1

                        ShotOK = False
                    if shot == 'end':
                        
                        return [['player #','shot'], SF, SA]
                        
                        ShotOK = True
                        InputOK = True
                        break
                    if shot == 'change':
                        ShotOK = True
                        InputOK = False
                except ValueError:
                    ShotOK = False
            
                
        except ValueError:
                    ShotOK = False

def writeShots(data, outFile):

    with open(outFile, 'w') as f:
        writer = csv.writer(f)
        wr = csv.writer(f)        
        wr.writerow(data[0])
        for i in range(1,3):
            for key, value in data[i].items():
               writer.writerow([key, value])
    

testreturn = getShots()
#print(len(testreturn))
writeShots(testreturn, 'test_shots.csv')
