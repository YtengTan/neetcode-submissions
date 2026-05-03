class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
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

        

        # is_anagram = True
        # for character in t:
        #     if character not in s_char_list:
        #         is_anagram = False
        #         break

        # return is_anagram


        