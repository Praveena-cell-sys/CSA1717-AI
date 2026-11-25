# PROGRAM
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domain = ['Red', 'Green', 'Blue']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def is_consistent(var, color, assignment):
    for n in neighbors[var]:
        if assignment.get(n) == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment
    var = next(v for v in variables if v not in assignment)
    for color in domain:
        if is_consistent(var, color, assignment):
            assignment[var] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]
    return None

solution = backtrack({})
if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(f"{region} -> {color}")
else:
    print("No solution exists")

# OUTPUT
# Map Coloring Solution:
# WA -> Red
# NT -> Green
# SA -> Blue
# Q -> Red
# NSW -> Green
# V -> Red
# T -> Red
