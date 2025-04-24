from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Directions we can move in: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize the queue to keep track of rotten oranges and count of fresh oranges
        rotten_oranges = deque()
        fresh_count = 0
        
        # Step 1: Loop through the grid to find all rotten oranges (value = 2)
        # and fresh oranges (value = 1), and add rotten ones to the queue.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))  # Add rotten orange coordinates to the queue
                elif grid[i][j] == 1:
                    fresh_count += 1  # Count fresh oranges
        
        # Edge case: if no fresh oranges exist, no rotting needs to happen
        if fresh_count == 0:
            return 0
        
        minutes_passed = 0
        
        # Step 2: Start the rotting process, spreading the rot to adjacent fresh oranges.
        while rotten_oranges:
            # Track the number of rotten oranges at this minute
            size = len(rotten_oranges)
            rotten_found_this_minute = False  # To track if we rot any oranges this minute
            
            for _ in range(size):
                i, j = rotten_oranges.popleft()  # Get the current rotten orange
                
                # Spread rot to 4 adjacent directions (up, down, left, right)
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    # Check if the new position is within the grid and contains a fresh orange
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2  # Turn the fresh orange into rotten
                        fresh_count -= 1  # Decrease the count of fresh oranges
                        rotten_oranges.append((ni, nj))  # Add this new rotten orange to the queue
                        rotten_found_this_minute = True
            
            # Only increment the time if we actually spread rot this minute
            if rotten_found_this_minute:
                minutes_passed += 1
        
        # If there are still fresh oranges left, return -1 (impossible case)
        return minutes_passed if fresh_count == 0 else -1
