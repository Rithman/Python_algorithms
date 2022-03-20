class Solution(object):
    def reversePrefix(self, word, ch):
        l = 0
        r = 0
        word = list(word)
        for i, char in enumerate(word):
            if char == ch:
                r = i
                break
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1

        return ''.join(word)

# Догадываюсь, что можно как-то за один проход сделать, но пока не придумал как.
