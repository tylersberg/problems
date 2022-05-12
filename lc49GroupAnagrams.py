# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grams = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in grams:
                grams[key].append(word)
            else:
                grams[key] = [word]
        return grams.values()
