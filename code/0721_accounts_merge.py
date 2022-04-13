class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        uf = {}
        
        def find(x):
            uf[x] = uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        # connect accounts, store email to name dict
        for account in accounts:
            name = account[0]
            emails = account[1:]
            
            p_first = find(emails[0])
            email_to_name[emails[0]] = name
            for i in range(1, len(emails)):
                email_to_name[emails[i]] = name
                p_email = find(emails[i])
                uf[p_email] = p_first
                
        res = collections.defaultdict(list)
        for email in uf.keys():
            res[find(email)].append(email)
        return [[email_to_name[k]] + sorted(v) for k, v in res.items()]
            