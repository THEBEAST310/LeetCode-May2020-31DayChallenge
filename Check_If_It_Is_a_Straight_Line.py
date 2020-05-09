class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        if coordinates[1][0]-coordinates[0][0]!=0:
            slope=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        else:
            for x in range(len(coordinates)-1):
                if coordinates[x][0]!=coordinates[x+1][0]:
                    return False
            return True
        for x in range(len(coordinates)-1):
            if (coordinates[x+1][0]-coordinates[x][0])!=0:
                if ((coordinates[x+1][1]-coordinates[x][1])/(coordinates[x+1][0]-coordinates[x][0]))!=slope:
                    return False
            else:
                for x in range(len(coordinates)-1):
                    if coordinates[x][0]!=coordinates[x+1][0]:
                        return False
                return True    
        return True
