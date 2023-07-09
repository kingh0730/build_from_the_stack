from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


from collections import defaultdict

def generate_input() -> list:
    res = []
    
    T = gen_pos_int(10)
    res.append(T)
    
    for _ in range(T):
        n = gen_pos_int(2 * 10**5)
        m = gen_pos_int(2 * 10**5)
        res.append([n, m])
        
        tracks = defaultdict(list)
        for _ in range(m):
            x = gen_pos_int(n)
            y = gen_pos_int(n)
            while y == x:
                y = gen_pos_int(n)
            
            tracks[x].append(y)
        
        for x, ys in tracks.items():
            for y in ys:
                res.append([x, y])
    
    return res
