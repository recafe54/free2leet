# SOL 1
class Solution:
    def isValid(self, s: str) -> bool:
        opening_list = ["{", "(", "["]
        closing_list = ["}", ")", "]"]
        bracket_dict = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for idx, ch in enumerate(s):
            if ch in bracket_dict.keys():
                if idx == 0:
                    return False
                else:
                    print(f"idx {idx} ch {ch}")
                    if s[idx-1] == bracket_dict[ch]:
                        #s.pop(idx-1)
                        #s.pop(idx-1)
                        s = s[:idx-1] + s[idx:]
                        print('s: ',s)
                        s = s[:idx-1] + s[idx:]
                        print('s: ',s)
                        if len(s) == 0:
                            return True
                    else:
                        return False
        
        
        return False
    
"""
s = "()[]{}"


Stdout:

idx 1 ch )
s:  )[]{}
s:  []{}
idx 3 ch ]

Output: false
Expected: true
Comment: For using the index of old string --> incorrect on newer string (be edited)

"""