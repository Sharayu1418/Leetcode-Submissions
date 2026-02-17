
    def canPlace(self, stalls, cows, d):
    
        count = 1
        lastPos = stalls[0]

        # Try placing remaining cows
        for i in range(1, len(stalls)):
            # If current stall is at least 'd' away from last cow
            if stalls[i] - lastPos >= d:
                # Place a cow here
                count += 1
                lastPos = stalls[i]
            # If all cows placed successfully
            if count >= cows:
                return True
        # Not possible to place all cows
        return False

    
    def aggressiveCows(self, stalls, cows):
        # Sort stall positions
        stalls.sort()

        # Get the maximum possible distance
        maxDist = stalls[-1] - stalls[0]
        ans = 0

        # Try all possible distances from 1 to maxDist
        for d in range(1, maxDist + 1):
            # If cows can be placed with distance d
            if self.canPlace(stalls, cows, d):
                ans = d

        # maximum valid distance should be returned
        return ans