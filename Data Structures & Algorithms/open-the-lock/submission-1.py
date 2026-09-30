class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target=="0000":
            return 0
        
        visited = set(deadends)
        if "0000" in visited:
            return -1

        begin = {"0000"}
        end = {target}
        steps = 0
        
        while begin and end:
            if len(begin)>len(end):
                begin, end = end, begin
            
            steps += 1
            temp = set()
            for lock in begin:
                for i in range(4):
                    for j in [-1,1]:
                        pos = int(lock[i])
                        pos = (pos+j+10)%10
                        tmp_lock = lock[:i]+str(pos)+lock[i+1:]
                        if tmp_lock in end:
                            return steps
                        if tmp_lock in visited:
                            continue
                        temp.add(tmp_lock)
                        visited.add(tmp_lock)
            begin = temp
        return -1
        # -1 if one up or one down in every position compared to target
        # def find_deadends():
        #     ans = []
        #     for i,char in enumerate(target):
        #         num = int(char)
        #         tmp_char = str(num-1)
        #         new_str=target[:i]+tmp_char+target[i+1:]
        #         ans.append(new_str)
        #         tmp_char = str(num+1)
        #         new_str=target[:i]+tmp_char+target[i+1:]
        #         ans.append(new_str)
        #     return ans

        # possible_deadends = find_deadends()
        # print(possible_deadends)

        # options = []
        # for possible_deadend in possible_deadends:
        #     if possible_deadend in deadends:
        #         continue
        #     options.append(possible_deadend)
        
        # print(options)
        # if not options:
        #     return -1
    

