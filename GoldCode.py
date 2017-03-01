import numpy as np

SV = {
     1: 1023 -   5 ,
     2: 1023 -   6 ,
     3: 1023 -   7 ,
     4: 1023 -   8 ,
     5: 1023 -  17 ,
     6: 1023 -  18 ,
     7: 1023 - 139 ,
     8: 1023 - 140 ,
     9: 1023 - 141 ,
     10: 1023 - 251 ,
     11: 1023 - 252 ,
     12: 1023 - 254 ,
     13: 1023 - 255 ,
     14: 1023 - 256 ,
     15: 1023 - 257 ,
     16: 1023 - 258 ,
     17: 1023 - 469 ,
     18: 1023 - 470 ,
     19: 1023 - 471 ,
     20: 1023 - 472 ,
     21: 1023 - 473 ,
     22: 1023 - 474 ,
     23: 1023 - 509 ,
     24: 1023 - 512 ,
     25: 1023 - 513 ,
     26: 1023 - 514 ,
     27: 1023 - 515 ,
     28: 1023 - 516 ,
     29: 1023 - 859 ,
     30: 1023 - 860 ,
     31: 1023 - 861 ,
     32: 1023 - 862 ,
}

ca_code_states = (
    (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1),
    (0,0), (0,0), (0,1), (1,0), (1,1), (1,1), (0,0), (0,1), (0,0), (1,0),
    (0,1), (0,0), (1,1), (1,0), (1,1), (0,1), (1,1), (1,1), (0,0), (0,1),
    (1,0), (0,1), (1,0), (0,0), (1,0), (1,0), (1,0), (0,1), (1,1), (1,1),
    (1,1), (1,1), (0,0), (1,1), (0,0), (1,1), (0,0), (0,1), (0,0), (1,1),
    (1,1), (1,0), (1,1), (0,0), (1,0), (0,0), (0,0), (1,0), (0,1), (1,0),
    (0,1), (1,0), (0,0), (0,1), (0,1), (0,1), (0,0), (1,1), (0,1), (1,1),
    (1,0), (1,0), (1,1), (1,0), (1,0), (1,0), (1,0), (0,1), (1,1), (0,0),
    (1,1), (0,0), (1,0), (0,0), (1,1), (0,1), (1,0), (1,0), (1,1), (1,1),
    (0,1), (1,1), (0,1), (0,0), (0,1), (0,1), (1,1), (1,1), (1,0), (0,1),
    (1,1), (0,0), (0,1), (1,0), (0,0), (0,1), (0,1), (1,1), (1,1), (0,0),
    (0,0), (1,1), (0,0), (1,1), (1,0), (0,0), (1,0), (0,1), (1,1), (1,1),
    (0,1), (0,0), (1,1), (1,1), (1,0), (1,0), (0,0), (1,1), (0,0), (1,0),
    (1,1), (0,0), (0,1), (0,1), (1,1), (1,1), (0,0), (0,1), (1,1), (1,1),
    (1,1), (1,1), (1,1), (1,0), (0,1), (0,0), (1,0), (0,1), (1,0), (0,0),
    (1,1), (0,0), (1,1), (0,1), (0,0), (1,1), (1,1), (0,0), (0,0), (1,1),
    (1,0), (0,0), (0,0), (1,0), (0,0), (1,1), (0,1), (0,0), (1,1), (1,0),
    (1,1), (1,0), (1,0), (0,0), (1,1), (0,0), (0,0), (1,0), (1,0), (1,1),
    (0,0), (0,1), (0,0), (0,0), (1,0), (0,1), (0,0), (0,1), (1,0), (1,1),
    (0,0), (1,1), (1,1), (0,1), (0,1), (1,1), (0,1), (0,1), (0,0), (1,1),
    (0,0), (1,1), (0,1), (0,1), (1,1), (1,0), (0,0), (1,0), (1,0), (1,1),
    (1,1), (0,0), (1,1), (1,1), (1,0), (0,1), (1,0), (0,0), (1,0), (0,1),
    (1,0), (1,0), (1,1), (0,0), (0,0), (1,1), (1,0), (0,0), (0,1), (1,1),
    (1,0), (1,0), (0,0), (1,1), (1,0), (1,1), (0,0), (1,1), (1,1), (1,1),
    (0,0), (0,0), (1,0), (1,1), (1,0), (0,0), (1,1), (0,1), (1,1), (0,0),
    (0,0), (1,0), (1,0), (1,0), (0,0), (1,0), (0,1), (0,0), (0,0), (0,1),
    (0,0), (1,1), (1,0), (1,1), (1,0), (0,1), (1,0), (1,1), (0,0), (1,0),
    (1,0), (1,1), (0,1), (0,0), (0,1), (0,1), (1,0), (1,0), (0,0), (0,1),
    (0,1), (1,0), (0,0), (0,1), (1,0), (0,1), (1,0), (0,0), (0,1), (1,1),
    (0,0), (1,0), (1,0), (0,0), (0,0), (1,0), (1,1), (0,0), (1,1), (0,0),
    (0,1), (0,1), (1,0), (0,0), (0,1), (0,1), (1,0), (0,0), (1,1), (1,0),
    (0,0), (1,1), (0,1), (0,1), (1,1), (0,1), (1,1), (1,0), (1,0), (0,1),
    (1,1), (0,1), (0,0), (1,1), (1,0), (0,0), (0,1), (0,0), (1,1), (0,1),
    (1,1), (1,0), (0,0), (0,0), (0,0), (0,0), (0,1), (0,0), (1,0), (0,1),
    (1,1), (0,1), (0,1), (1,0), (0,1), (0,1), (1,1), (0,0), (1,1), (1,0),
    (1,1), (1,0), (1,0), (0,1), (1,0), (1,1), (1,0), (1,0), (0,1), (0,0),
    (0,0), (1,1), (1,1), (0,1), (0,0), (0,1), (1,0), (1,1), (0,1), (1,1),
    (1,0), (1,0), (0,1), (1,1), (1,1), (0,1), (0,0), (0,1), (0,0), (1,1),
    (1,1), (1,0), (1,1), (0,1), (0,1), (1,1), (0,0), (0,0), (1,0), (1,1),
    (1,1), (0,0), (0,1), (1,0), (0,1), (1,1), (1,0), (0,1), (0,0), (0,1),
    (1,0), (0,1), (0,1), (0,0), (0,0), (1,0), (1,1), (0,1), (1,1), (1,0),
    (1,0), (1,1), (1,0), (1,0), (1,1), (0,0), (0,0), (1,0), (1,1), (1,1),
    (0,1), (0,1), (0,1), (1,1), (1,0), (0,1), (1,1), (0,0), (1,0), (0,1),
    (0,1), (1,1), (0,1), (1,0), (0,0), (0,0), (0,0), (0,0), (1,1), (0,1),
    (0,0), (0,0), (0,0), (1,0), (0,1), (0,1), (1,0), (0,0), (1,1), (1,1),
    (0,0), (1,1), (1,0), (1,1), (1,0), (1,1), (0,0), (1,0), (0,1), (1,1),
    (1,0), (1,1), (0,0), (0,1), (0,1), (1,1), (0,1), (1,1), (1,0), (1,1),
    (0,1), (0,0), (1,1), (0,1), (0,0), (0,0), (0,0), (1,0), (1,1), (1,1),
    (1,1), (1,0), (0,0), (1,0), (1,1), (0,1), (1,1), (0,0), (1,1), (0,1),
    (1,1), (0,1), (0,0), (0,0), (1,1), (0,1), (1,0), (1,1), (1,0), (1,0),
    (0,0), (1,0), (1,1), (0,1), (0,1), (1,0), (1,1), (1,0), (0,0), (0,0),
    (1,0), (1,0), (1,0), (1,0), (1,0), (0,1), (0,1), (0,1), (0,0), (0,0),
    (1,1), (1,1), (1,0), (0,0), (0,1), (1,1), (0,0), (0,0), (1,0), (0,0),
    (1,1), (0,0), (1,0), (1,1), (0,0), (0,0), (1,0), (0,0), (1,1), (1,0),
    (1,0), (1,0), (0,1), (0,1), (1,0), (0,0), (1,0), (1,1), (1,0), (0,0),
    (0,0), (0,0), (0,0), (0,0), (1,0), (0,1), (1,1), (0,0), (1,0), (1,1),
    (0,0), (1,0), (1,0), (0,1), (0,0), (1,0), (1,0), (0,1), (0,1), (0,1),
    (0,0), (1,1), (1,0), (0,1), (1,0), (0,1), (1,1), (1,1), (0,0), (1,1),
    (1,0), (1,0), (0,1), (1,1), (0,1), (0,0), (0,0), (1,1), (0,0), (1,1),
    (0,1), (1,1), (1,1), (1,1), (1,1), (1,0), (1,0), (0,0), (1,1), (0,0),
    (0,1), (0,0), (1,0), (1,1), (1,0), (0,1), (0,1), (1,0), (1,0), (0,1),
    (1,1), (1,1), (1,0), (0,0), (0,1), (1,1), (0,1), (1,0), (0,0), (0,0),
    (0,1), (1,0), (1,1), (0,1), (1,0), (0,0), (0,1), (0,0), (0,1), (0,1),
    (0,1), (1,0), (1,1), (0,0), (0,1), (1,1), (0,0), (0,0), (1,1), (0,0),
    (0,0), (0,1), (1,0), (0,1), (0,0), (0,0), (0,0), (0,0), (1,1), (0,0),
    (0,0), (1,1), (1,1), (0,0), (1,1), (1,1), (0,0), (1,0), (0,1), (0,1),
    (1,0), (1,1), (1,1), (1,1), (0,1), (0,0), (1,1), (1,0), (0,0), (1,0),
    (0,1), (1,1), (0,1), (1,0), (1,0), (0,0), (0,0), (0,1), (0,0), (1,1),
    (0,0), (1,1), (1,0), (1,0), (0,1), (1,0), (1,0), (0,0), (1,1), (0,0),
    (0,1), (0,0), (1,0), (1,0), (0,0), (0,0), (0,0), (0,1), (1,0), (0,0),
    (0,0), (1,0), (1,0), (1,1), (1,0), (1,0), (1,0), (1,1), (0,0), (1,0),
    (1,1), (1,1), (0,0), (0,0), (0,1), (1,1), (1,1), (1,0), (1,1), (0,1),
    (0,0), (0,0), (0,1), (0,0), (0,1), (1,0), (1,1), (1,1), (0,0), (1,1),
    (1,1), (0,0), (1,1), (1,1), (0,1), (0,1), (0,1), (1,0), (0,1), (1,0),
    (0,0), (0,0), (0,0), (1,1), (0,0), (0,1), (1,1), (1,0), (0,1), (0,0),
    (1,1), (0,1), (0,1), (0,0), (0,1), (0,1), (1,0), (1,0), (0,0), (1,0),
    (0,0), (0,1), (1,0), (0,1), (0,1), (1,0), (1,0), (1,0), (1,0), (0,0),
    (1,0), (1,0), (1,0), (1,0), (1,1), (0,0), (0,1), (0,1), (1,1), (0,0),
    (1,1), (0,1), (1,1), (0,0), (1,1), (1,1), (0,1), (1,1), (0,1), (0,0),
    (0,0), (0,0), (1,1), (0,1), (1,1), (0,1), (0,1), (0,0), (0,0), (0,0),
    (0,0), (0,1), (1,0), (0,0), (1,0), (1,0), (0,1), (1,1), (1,1), (0,1),
    (1,1), (1,1), (1,1), (1,1), (0,0), (0,1), (1,1), (1,1), (1,0), (1,0),
    (0,0), (0,0), (0,1), (1,1), (0,1), (0,1), (0,0), (1,1), (1,0), (1,0),
    (1,1), (1,1), (1,0), (0,0), (1,1), (1,0), (0,1), (0,1), (0,0), (1,0),
    (1,0), (1,1), (0,0), (1,1), (0,1), (1,1), (1,0), (0,0), (1,1), (0,0),
    (1,1), (0,0), (0,1), (0,0), (0,0), (1,0), (1,0), (0,1), (0,1), (1,0),
    (1,0), (0,0), (1,1), (1,1), (0,0), (0,1), (0,1), (0,1), (0,0), (1,1),
    (1,0), (0,0), (0,0), (0,1), (0,0), (0,1), (0,1), (0,1), (0,1), (1,0),
    (1,0), (0,1), (1,0), (1,0), (0,0), (1,1), (1,1), (0,0), (1,1), (0,0),
    (1,0), (1,1), (1,1), (0,0), (1,1), (0,1), (1,1), (1,0), (1,0), (1,0),
    (0,1), (0,1), (0,0), (0,0), (1,0), (0,0), (1,0), (0,1), (1,1), (0,1),
    (0,0), (1,1), (0,1), (0,0), (0,1), (0,1), (1,1), (0,0), (1,1), (1,1),
    (0,0), (0,1), (1,0), (0,1), (0,1), (1,0), (1,0), (0,0), (0,0), (0,1),
    (0,0), (0,1), (1,1), (0,1), (0,1), (0,1), (1,0), (0,0), (0,1), (1,1),
    (0,0), (0,0), (0,0), (0,1), (0,1), (0,1), (1,1), (0,0), (0,0), (0,1),
    (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (1,0), (0,0), (0,0), (1,0),
    (0,0), (0,0), (1,1), (0,1), (0,1), (1,1), (1,0), (0,0), (1,0), (0,1),
    (0,0), (1,0), (1,0), (0,1), (1,0), (0,1), (1,1), (1,0), (1,1), (1,1),
    (1,1), (0,0), (0,0), (1,1), (1,1), (0,0), (0,1), (0,1), (1,0), (1,1),
    (1,1), (1,0), (1,1), (0,0), (0,1), (1,0), (0,0), (0,1), (0,1), (1,1),
    (1,1), (1,1), (0,0), (1,0), (1,1), (1,0), (1,0), (1,1), (1,1), (0,0),
    (0,1), (0,0), (0,0), (1,1), (1,0), (1,0), (0,0), (0,0), (0,0), (0,0),
    (0,1), (0,1), (0,0),
)

chips_per_code = 1023
max_sv = 32


#Internal function. The codes class calls this to generate its list of codes.
def cacode(chip, sv):
    assert(sv >= 1 and sv <= max_sv)
    g2chip = chip + SV[sv]
   
    if g2chip >= chips_per_code:
        g2chip -= chips_per_code
    return ca_code_states[chip][0] ^ ca_code_states[g2chip][1]

class codes():
    def __init__(self, zeros=False):
        self._codes = {k:None for k in SV.keys()}

        for k in self._codes.keys():
            c = [cacode(i,k) for i in range(chips_per_code)]
            if zeros is False:
                self._codes[k] = [-1 if val is 0 else 1 for val in c]
            else:
                self._codes[k] = c
            
        self._len = chips_per_code

    def __call__(self, sv, chip):
        return self._codes[sv][chip % self._len]
