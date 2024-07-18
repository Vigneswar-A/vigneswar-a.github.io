class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        text = s.replace("-", "").upper()
        firstlength = len(text)%k
        first = text[:firstlength] + ('-' if 0 < firstlength < len(text) else '')
        return first + '-'.join(text[i:i+k] for i in range(firstlength, len(text), k))

        