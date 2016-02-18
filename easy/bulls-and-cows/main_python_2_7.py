# -*- coding:utf-8 -*-
# description: 经典的Bull-Cow游戏
# 算法必须是2趟，第一趟剔除Bulls，剩下的Cow候选再就行比较。
from collections import Counter as mset
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #bulls = [val for i, val in enumerate(secret) if secret[i] == guess[i]]
        #print bulls
        #print filter(lambda (i, val): val == secret[i], enumerate(guess))
        #cow_candidates = [(val, guess[i]) for i, val in enumerate(secret) if secret[i] != guess[i]]
        #print cow_candidate

        bulls = [val for i, val in enumerate(secret) if secret[i] == guess[i]]
        secret_cow_candidates = [val for i, val in enumerate(secret) if secret[i] != guess[i]]
        guess_cow_candidates = [val for i, val in enumerate(guess) if secret[i] != guess[i]]
        #print bulls
        #print secret_cow_candidates
        #print guess_cow_candidates
        cows = list( (mset(secret_cow_candidates) & mset(guess_cow_candidates)).elements() )
        return "%dA%dB" % (len(bulls), len(cows))

if "__main__" == __name__:
    s = Solution()
    print s.getHint("1807", "7810")
    print "1A3B is expected"

    print s.getHint("1123", "0111")
    print "1A1B is expected"

    print s.getHint("11123", "00111")
    print "1A2B is expected"
