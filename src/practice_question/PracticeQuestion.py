class PracticeQuestion(object):

    def __init__(self):
        self.list_2 = None
        self.list_1 = None

    def next_question(self):
        pass

    def find_anagram_words(self):
        list1 = self.list_1
        list2 = self.list_2

        # Create sets of sorted tuples
        sorted_tuples_1 = set(tuple(sorted(word)) for word in list1)
        sorted_tuples_2 = set(tuple(sorted(word)) for word in list2)

        # Find common tuples (anagrams)
        common_tuples = sorted_tuples_1 & sorted_tuples_2

        # Collect original words from list_1 that match common tuples
        output = [word for word in list1 if tuple(sorted(word)) in common_tuples]
        return output
