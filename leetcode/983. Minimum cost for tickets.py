from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0] * (last_day + 1)  # полная стоимость плана поездок на текущий день включительно
        set_days = set(days)  # для проверки путешествуем в этот день
        for i in range(1, last_day + 1):
            if i in set_days:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
