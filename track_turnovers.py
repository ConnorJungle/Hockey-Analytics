import csv
import numpy as np

def getTurnovers():

    ''' This program takes a user input to track turnovers and the type of turnover. It will return a CSV file '''
    
    data = [['TEAM', 'PLAYER #', '# TURNOVERS', 'KIND OF TURNOVER']]
    InputOK = False
    while not InputOK:
        TeamOK = False
        while not TeamOK:
            try:
                team = str(input('Team: '))
                if team == 'end':
                    return np.array(data)
                    InputOK = True
                    break
                if team == 'q':
                    NumOK = False
                    while not NumOK:
                        try:
                            num = int(input('Player#: '))
                            NumOK = True
                        except ValueError:
                            NumOK = False
                    turnoverOK = False
                    while not turnoverOK:
                        try:
                            turnover = int(input('turnover: '))
                            turnoverOK = True
                        except ValueError:
                            turnoverOK = False
                    kindOK = False
                    while not kindOK:
                        try:
                            kind_turnover = str(input('kind of turnover (blue, bad, reg): '))
                            kindOK = True
                        except ValueError:
                            kindOK = False
                    data.append([team ,num, turnover, kind_turnover])
            except ValueError:
                InputOK = False
                
        

def hockeyFile(my_data, outFile):
    
    a = open(outFile, 'w')
    wr = csv.writer(a)
    for line in my_data:
        wr.writerow(line)
    a.close()
    
lol = getTurnovers()
hockeyFile(lol, 'turnovers_ottawa_1st.csv')
        
            
            
