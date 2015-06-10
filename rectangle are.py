class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlay = min(D-B, H-F, max(D-F,0), max(H-B,0)) * min(C-A, G-E, max(C-E,0), max(G-A,0))
        return (C-A)*(D-B) + (G-E)*(H-F) - overlay
            