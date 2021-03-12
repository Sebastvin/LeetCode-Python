class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = ['.-', '-...', "-.-.", '-..', ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                '--..']

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']

        result = []

        morseCode = []
        invidualValue = []

        for i in range(0, len(words)):
            result.append(list(words[i]))

        for i in range(0, len(result)):
            for j in range(0, len(result[i])):
                invidualValue.append(code[alphabet.index(result[i][j])])

            morseCode.append(invidualValue)
            invidualValue = []

        for i in range(0, len(morseCode)):
            morseCode[i] = "".join(morseCode[i])


        score = set(morseCode)

        return len(score)
