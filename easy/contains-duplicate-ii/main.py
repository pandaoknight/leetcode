class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        import Queue
        #queue = Queue.LifoQueue(k)
        if 0 == k:
            return False
        queue = Queue.Queue(k)
        lookup = {}
        for n in nums:
            if lookup.get(n, True):
                # first clean the queue, then put n in
                if queue.full():
                    clean_target = queue.get()
                    #print "clean:" + str(clean_target) + " size:" + str(queue.qsize())
                    lookup[clean_target] = True # mean could access again
                queue.put(n)
                #print queue.qsize()
                lookup[n] = False
            else:
                #print "True for " + str(n)
                return True
        return False

if "__main__" == __name__:
    s = Solution()
    print s.containsNearbyDuplicate([1,2,3,1,3], 1)
    print s.containsNearbyDuplicate([1,2,3,3,1,3], 1)
    print s.containsNearbyDuplicate([1,2,3,1,3], 2)
    print s.containsNearbyDuplicate([1,2,3,1,0,3], 2)
    print s.containsNearbyDuplicate([1,2,3,1,0,3,0], 2)
    print s.containsNearbyDuplicate([], 2)
    print s.containsNearbyDuplicate([1,2,3,1,0,3,0], 0)
