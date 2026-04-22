# 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，
# 其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。
#
# 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend，
# 且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。
#
# 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
"""
1. Problem Description
每个气球对应一个区间 `[start, end]`。在某个 x 坐标射一箭，能引爆所有覆盖这个 x 的气球。
问最少要射几箭才能引爆全部气球。

2. Solution Approach
核心是区间贪心：
- 先按区间左端点排序。
- 维护当前“可共用一箭”的重叠区间边界（主要看最小右边界）。
- 新区间如果和当前重叠，就继续收紧右边界。
- 不重叠就必须新开一箭。
这份代码用 `res` 从总数往下减来统计重叠合并。

3. Code Walkthrough
- `points.sort(key=lambda x: x[0])`：先排序。
- `min_right` 记录当前组可共同命中的最右边界。
- 若 `qvjian[0] > min_right`：当前组结束，开启新组。
- 否则说明重叠，`res -= 1`，并根据更小右边界更新 `min_right`。

4. Key Takeaways
- 区间最少资源问题通常是贪心。
- 时间复杂度 O(n log n)（排序主导），空间复杂度 O(1)~O(n) 视排序实现。
- 容易错在边界：`start == min_right` 也算可被同一箭击中。
- 同类题（会议室、最少分组）都可以借鉴“排序 + 当前可行边界”。
"""
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        l = len(points)
        points.sort(key=lambda x: x[0])
        res = l
        min_right = None
        max_left = None
        if len(points) == 1:
            return 1
        if not points:
            return 0
        for qvjian in points:
            if not min_right and not max_left:
                min_right = qvjian[1]
                max_left = qvjian[0]
                continue
            if qvjian[0] > min_right:
                min_right = qvjian[1]
                max_left = qvjian[0]
                continue
            elif qvjian[0] <= min_right:
                if qvjian[1] <=min_right:
                    res -=1
                    min_right = qvjian[1]
                    max_left = qvjian[0]
                    continue
                else:
                    res -= 1
                    max_left = qvjian[0]



        return res


if __name__ == '__main__':
    points = [[1,2],[2,3],[3,4],[4,5]]
    solution = Solution()
    print(solution.findMinArrowShots(points))
    # 输出：4



