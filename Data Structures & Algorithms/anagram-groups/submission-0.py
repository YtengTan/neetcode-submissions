class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def is_anagrams(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            s_char_list = []
            t_char_list = []
            for char_s,char_t in zip(s, t):
                s_char_list.append(char_s)
                t_char_list.append(char_t)        
            
            s_char_list.sort()
            t_char_list.sort()
            for char_s,char_t in zip(s_char_list, t_char_list):
                if char_s != char_t:
                    return False
            
            return True
        
        anagrams_group = []
        n_strs = len(strs)
        paired_idx = []
        for i in range(n_strs-1):
            if i in paired_idx:
                continue
            str_i = strs[i]
            anagrams_subgroup = [str_i]
            for j in range(i+1,n_strs):
                str_j = strs[j]
                if is_anagrams(str_i,str_j):
                    anagrams_subgroup.append(str_j)
                    paired_idx.append(j)
            anagrams_group.append(anagrams_subgroup)

        if n_strs-1 not in paired_idx:
            anagrams_group.append([strs[-1]])
        
        return anagrams_group

        

        