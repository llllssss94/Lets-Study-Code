from typing import *
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(lambda x: list(x), permutations(nums)))
    
