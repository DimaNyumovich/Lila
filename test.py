from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    j = 0
    res = []
    while True:
        for i in range(1, len(strs)):
            if j < len(strs[i]):
                if strs[0][j] != strs[i][j]:
                    return ''.join(res)
            else:
                return ''.join(res)
        res.append(strs[0][j])
        j += 1





if __name__ == '__main__':
    print(longestCommonPrefix(["fliower","fliodfsdf","flioght"]))