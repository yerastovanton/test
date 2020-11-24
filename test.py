rule_add = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

rule_div = {
    ('I', 'V'): 3,
    ('I', 'X'): 8,
    ('X', 'L'): 30,
    ('X', 'C'): 80,
    ('C', 'D'): 300,
    ('C', 'M'): 800,
}

    
class Solution:
     def romanToInt(self, s: str) -> int:
        self.number = 0
        prev_literal = None
        for literal in s:
            if prev_literal and rule_add[prev_literal] < rule_add[literal]:
                self.number += rule_div[(prev_literal, literal)]
            else:
                self.number += rule_add[literal]
            prev_literal = literal
        return self.number