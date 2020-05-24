class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def helper(ip, track):
            if len(track) > 4:
                return
            if not ip:
                if len(track) == 4:
                    res.append(".".join([str(i) for i in track]))
                return
            # 1 digit
            helper(ip[1:], track + [int(ip[0])])
            # 2 digits, first digit != 0
            if len(ip) >= 2 and ip[0] != '0':
                helper(ip[2:], track + [int(ip[:2])])
            # 3 digits, first digit != 0 and less than 256
            if len(ip) >= 3 and ip[0] != '0' and int(ip[:3]) <= 255:
                helper(ip[3:], track + [int(ip[:3])])
                
        helper(s, [])
        return res
            
            