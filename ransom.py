
def ransom(ransom: str, mag: str) -> bool:

    ransom1 = set(ransom)

    for char in ransom1:
        if mag.count(char) < ransom.count(char):
            return False
    return True