class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        n, counter = len(s), len(t)
        begin, end, head = 0, 0, 0 
        
        # set minimum length to len(string)+1. It cannot be greater than that
        min_len = n+1        
        
        # hashmap to hold character count in T
        dic = dict()
        for ch in t:
            dic[ch] = dic.get(ch, 0)+1        
            
        # Iterate throught the loop till we reach end of string S    
        while end < n:
            
            # 1. if character in S is present in T then 
            # 2. if count of that character in hashmap is greater than zero then decrement the counter
            # 3. Decrement the count for that character in hashmap
            if s[end] in dic:
                if dic[s[end]] > 0:
                    counter -= 1
                dic[s[end]] -= 1
                
            end += 1            

            # While counter is zero (it means we have all characters between begin and end)
            # Calculate the length and min_length
            while counter == 0:
                #print begin, end, dic
                if end - begin < min_len:
                    min_len = end-begin
                    head = begin
                
                # If character at begin index is present in T, then increment its count in hashmap
                # If its count in hashmap is <= 0, then continue the inner while loop until the count is +ve
                # If its count in hashmap is > 0 then increment the counter. It means we have found first character
                # which is in S and T. So we can continue searching for shortest len from begin+1 to ...
                # Check the output below:
                    # 1. First the begin and end window are at idx - 0 and 6
                    #     min_len - 6
                    # 2. Since begin (idx = 0) is `A`, so we set next window from begin+1 to end 
                    #    and continue with the process.
                    # 3. When end idx reaches 11, we have all characters of T in S. We calculate len and compare min_len 
                    # 4. Now, since begin(idx=1) is 'D' which is not in T, we continue in inner while loop until
                    # we set counter to non-zero. Here, we can see than count of B in hashmap is -1 since we 
                    # have 2occurances of B between begin to end. So we have to skip the first occurance.
                #
                #   Input - "ADOBECODEBANC"
                #           "ABC"
                #
                # The output of above commented print statement
                # 0 6 {u'A': 0, u'C': 0, u'B': 0}
                # 1 11 {u'A': 0, u'C': 0, u'B': -1}
                # 2 11 {u'A': 0, u'C': 0, u'B': -1}
                # 3 11 {u'A': 0, u'C': 0, u'B': -1}
                # 4 11 {u'A': 0, u'C': 0, u'B': 0}
                # 5 11 {u'A': 0, u'C': 0, u'B': 0}
                # 6 13 {u'A': 0, u'C': 0, u'B': 0}
                # 7 13 {u'A': 0, u'C': 0, u'B': 0}
                # 8 13 {u'A': 0, u'C': 0, u'B': 0}
                # 9 13 {u'A': 0, u'C': 0, u'B': 0}
                
                if s[begin] in dic:
                    dic[s[begin]] += 1
                    if dic[s[begin]] > 0: 
                        counter += 1                
                begin += 1
        
        # Calculate the min string
        if min_len == n+1:
            return ""
        return s[head: head+min_len]