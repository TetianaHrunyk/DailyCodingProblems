"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

def permutations(l: list):
    perms = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            perm = l.copy()
            perm[i], perm[j] = perm[j], perm[i]
            if perm not in perms:
                perms.append(perm)
            perm = perm[::-1]
            if perm not in perms:
                perms.append(perm)
    return perms

if __name__ == "__main__":
    print(permutations([1,2,3]))
            