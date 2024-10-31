class Solution:
    def losingPlayer(self, x: int, y: int) -> str:

        alice_win = False
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            alice_win = not alice_win
        return "Alice" if alice_win else "Bob"
        