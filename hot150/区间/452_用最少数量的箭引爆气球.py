# 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，
# 其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。
#
# 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend，
# 且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。
#
# 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
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



