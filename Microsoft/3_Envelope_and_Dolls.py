from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x:(x[0], -x[1]))

        heights = [envelope[1] for envelope in envelopes]

        lis = []
        for height in heights:
            pos = bisect_left(lis, height)
            if pos == len(lis):
                lis.append(height)
            else:
                lis[pos] = height

                return len(lis)