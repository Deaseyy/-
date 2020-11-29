### 剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

##### 动态规划：常规解法
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 1.状态：f[i]代表以 prices[i]为结尾的子数组的最大利润, 即前i日的最大利润 
        # 2.转移方程：前i日最大利润f[i]等于 前i−1日最大利润f[i-1] 和 第i日卖出的最大利润中最大值
        # # 前i日最大利润 = max(前(i−1)日最大利润, 第i日价格−前i日最低价格)
        # # 方程为：f[i] = max(f[i−1], prices[i]−min(prices[0:i]))
        # 3.初始状态：f[0] = 0 ，即首日利润为0
        if not prices:
            return 0

        n = len(prices)
        f = [0] * n
        f[0] = 0
        for i in range(1, n):
            f[i] = max(f[i-1], prices[i] - min(prices[0:i]))
        return f[n-1]
```


##### 动态规划：效率优化
时间复杂度降低：
前i日的最低价格 min(prices[0:i])，时间复杂度为 O(i)，而在遍历 prices 时，可以借助一个变量cost，每日更新最低价格；  
优化后的转移方程为：f[i] = max(f[i−1], prices[i] − min(cost, prices[i]))
        
空间复杂度降低：
由于f[i]只与 f[i−1], prices[i], cost相关，因此可使用一个变量（记为利润 profit）代替 f 列表。  
优化后的转移方程为：profit = max(profit, prices[i] − min(cost, prices[i]))
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
```

##### 暴力算法优化o(n)
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        res = [0]  # 以prices[i]价格卖出的最大利润, i=0时，利润为0
        pre_min = prices[0]  # prices[i]前的最小值, i>1
        for i in range(1, len(prices)):
            if prices[i] > pre_min:
                res.append(prices[i] - pre_min)
            else:
                res.append(0) 
            
            pre_min = min(pre_min, prices[i])
        
        return max(res)
```
