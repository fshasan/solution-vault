class Solution(object):
    def peakIndexInMountainArray(self, arr):
        peak = -999999
        start = 0
        end = len(arr) - 1

        while(start <= end):
            if arr[start] >= arr[end]:
                if arr[start] > peak:
                    peak = arr[start]
                    index = start
            elif arr[end] > arr[start]:
                if arr[end] > peak:
                    peak = arr[end]
                    index = end
            start += 1
            end -= 1

        return index
