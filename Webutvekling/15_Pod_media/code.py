# Swedish alphabet decryption: columnar transposition (block=4) + Caesar

SWEDISH = "abcdefghijklmnopqrstuvwxyzåäö"
ALPHABET_SIZE = 29


def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypts text using Caesar cipher (shift backwards) with Swedish alphabet.
    Non-alphabet characters are kept unchanged.
    """
    if shift == 0:
        return text

    result = []
    shift = shift % ALPHABET_SIZE

    for char in text.lower():
        if char in SWEDISH:
            idx = SWEDISH.index(char)
            new_idx = (idx - shift) % ALPHABET_SIZE
            result.append(SWEDISH[new_idx])
        else:
            result.append(char)

    return "".join(result)


def undo_columnar_transposition(ciphertext: str, block_size: int = 4) -> str:
    """
    Reverses a simple columnar transposition where:
    - Plaintext was written into a grid row by row
    - Ciphertext was read column by column
    """
    n = len(ciphertext)
    if n == 0 or block_size < 2:
        return ciphertext

    # Number of rows needed
    rows = (n + block_size - 1) // block_size

    # Create grid
    grid = [[''] * block_size for _ in range(rows)]

    # Fill grid column by column (this is how ciphertext was read)
    idx = 0
    for col in range(block_size):
        for row in range(rows):
            if idx < n:
                # Only fill existing cells
                if row < rows - 1 or col < (n % block_size) or n % block_size == 0:
                    grid[row][col] = ciphertext[idx]
                    idx += 1

    # Read row by row to recover original order
    plaintext = []
    for row in grid:
        for char in row:
            if char:  # skip empty cells
                plaintext.append(char)

    return "".join(plaintext)


def decrypt_block4_then_caesar(ciphertext: str):
    """
    1. Removes everything except Swedish letters
    2. Undoes columnar transposition with block size 4
    3. Tries all 29 possible Caesar shifts
    4. Shows results sorted by number of vowels (rough quality indicator)
    """
    # Keep only valid Swedish letters
    cleaned = "".join(c for c in ciphertext.lower() if c in SWEDISH)

    if not cleaned:
        print("No valid Swedish letters found in the input.")
        return

    print(f"\nInput length (cleaned): {len(cleaned)} letters\n")

    # Step 1: undo columnar transposition (block size 4)
    after_block = undo_columnar_transposition(cleaned, block_size=4)

    print("After undoing columnar transposition (block size 4):")
    print(after_block[:400] + ("..." if len(after_block) > 400 else ""))
    print("\n" + "─" * 80 + "\n")

    # Step 2: try all Caesar shifts
    results = []

    for shift in range(ALPHABET_SIZE):
        decrypted = caesar_decrypt(after_block, shift)

        # Rough quality score: number of vowels in first 200 chars
        vowels = "aeiouyåäö"
        score = sum(1 for c in decrypted[:200] if c in vowels)

        preview = decrypted[:110] + ("..." if len(decrypted) > 110 else "")

        results.append({
            "shift": shift,
            "score": score,
            "text": decrypted,
            "preview": preview
        })

    # Sort by vowel count (higher = usually more promising)
    results.sort(key=lambda x: x["score"], reverse=True)

    print("All possible decryptions (sorted by vowel frequency):\n")

    for i, res in enumerate(results, 1):
        print(f"{i:2d}.  shift = {res['shift']:2d}   vowels = {res['score']:3d}")
        print(f"     {res['preview']}\n")


if __name__ == "__main__":
    print("Swedish alphabet – columnar transposition (block=4) + Caesar decrypt\n")
    print("Tries all 29 possible shifts after removing transposition\n")

    text = input("Enter or paste the ciphertext:\n> ").strip()

    if text:
        print("\n" + "═" * 90 + "\n")
        decrypt_block4_then_caesar(text)
    else:
        print("No text entered.")