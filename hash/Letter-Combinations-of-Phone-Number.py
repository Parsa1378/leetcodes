class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        combinations = []
        if len(digits)==0:
            return combinations
        else:
            for i in digits:
                ele = list(mappings[i])
                combinations.append(ele)
        return ["".join(i) for i in itertools.product(*combinations)]