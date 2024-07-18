class StringMatching:
    # Returns all occurrences of the pattern in the text
    def naive_matching(self, text, pattern):
        occurrences = []

        for i in range(0, len(text) - len(pattern) + 1):
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    break
                if j == len(pattern) - 1:
                    occurrences.append(i)

        return occurrences


# Example
st = StringMatching()

texto = "This text is a test, so obviously it must contain text :)"
patron = "text"

print(st.naive_matching(texto, patron))

texto = "AABCABBCABBDAABCDABCDAABBDABABCCABBABCABCAAB"
patron = "AAB"

print(st.naive_matching(texto, patron))

texto = "This text is also a test, but it wont have any match :("
patron = "Hello"

print(st.naive_matching(texto, patron))
