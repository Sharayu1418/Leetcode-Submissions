from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Graph to store the prerequisites and in-degree array to track the number of prerequisites
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)  # Add course to prerequisite's list
            in_degree[course] += 1  # Increment in-degree of the course
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)  
        course_order = []
        
        while queue:
            course = queue.popleft()
            course_order.append(course)
            for next_course in graph[course]:
                in_degree[next_course] -= 1  
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        if len(course_order) == numCourses:
            return course_order  
        else:
            return []  
