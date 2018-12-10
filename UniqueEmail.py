class Solution:
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    def numUniqueEmails(emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for email in emails:
            local, _, domain = email.partition('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)


    ret = numUniqueEmails(emails)
    print(ret)
