"""You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 

Example 2:
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Example 4:
Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15

Example 5:
Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843"""

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs = len(jobDifficulty)

        # max_diff[i][j] is max(jobDifficulty[i:j + 1])
        max_diff = [[0] * jobs for _ in range(jobs)]
        for start in range(jobs):
            m = jobDifficulty[start]
            for last in range(start, jobs):
                m = max(m, jobDifficulty[last])
                max_diff[start][last] = m

        dp = [[float('inf')] * jobs for _ in range(d)]
        # Initial states for DP
        for finished in range(jobs):
            dp[0][finished] = max_diff[0][finished]

        # DP process
        for day in range(1, d):
            for lastday_finished in range(day - 1, jobs):
                for finished in range(lastday_finished + 1, jobs):
                    new_diff = max_diff[lastday_finished + 1][finished]
                    dp[day][finished] = min(
                        dp[day][finished],
                        dp[day - 1][lastday_finished] + new_diff
                        )

        result = dp[d - 1][jobs - 1]
        return -1 if result == float('inf') else result

"""Runtime: 824 ms, faster than 75.16% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
Memory Usage: 14.9 MB, less than 41.87% of Python3 online submissions for Minimum Difficulty of a Job Schedule."""