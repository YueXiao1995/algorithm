"""
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

Example 1:
    Input: "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
    Input: "AAABBC"
    Output: 188

Note:
    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.
"""

def numTilePossibilities(tiles):
    if len(tiles) == 1:
        return 1
    num_of_sequences = 0
    unique_tiles = set(tiles)
    for tile in unique_tiles:
        new_tiles = list(tiles)
        new_tiles.remove(tile)
        num_of_sequences += numTilePossibilities(new_tiles) + 1
    return num_of_sequences

tiles = "AAB"
print(numTilePossibilities(tiles))

tiles = "AAABBC"
print(numTilePossibilities(tiles))

