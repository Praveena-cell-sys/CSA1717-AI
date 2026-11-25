# PROGRAM
import math

pruned = 0

def alphabeta(depth, node_index, is_max, scores, height, alpha, beta):
    global pruned
    if depth == height:
        return scores[node_index]
    if is_max:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, scores, height, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                pruned += 1
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, scores, height, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                pruned += 1
                break
        return best

scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = int(math.log2(len(scores)))
print("Leaf node values:", scores)
print("The optimal value is:", alphabeta(0, 0, True, scores, height, -math.inf, math.inf))
print("Number of pruned branches:", pruned)

# OUTPUT
# Leaf node values: [3, 5, 6, 9, 1, 2, 0, -1]
# The optimal value is: 5
# Number of pruned branches: 2
