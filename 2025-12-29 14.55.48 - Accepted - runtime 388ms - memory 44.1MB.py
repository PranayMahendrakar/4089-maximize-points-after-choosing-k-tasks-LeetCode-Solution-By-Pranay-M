class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        
        # For each task, calculate the difference (benefit of using technique1 over technique2)
        # diff[i] = technique1[i] - technique2[i]
        # If diff > 0, technique1 is better; if diff < 0, technique2 is better
        
        # Create pairs of (diff, idx) and sort by diff descending
        diffs = [(technique1[i] - technique2[i], i) for i in range(n)]
        diffs.sort(reverse=True)
        
        # Assign technique1 to the k tasks with highest diff (or all if k >= n)
        # Then for remaining tasks, pick the better one
        
        total = 0
        for j in range(n):
            idx = diffs[j][1]
            if j < k:
                # Must use technique1
                total += technique1[idx]
            else:
                # Use whichever is better
                total += max(technique1[idx], technique2[idx])
        
        return total