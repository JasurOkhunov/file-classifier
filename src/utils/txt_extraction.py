def extract_text_from_txt(file_bytes: bytes) -> str:
    """
    Extracts text from a bytes object representing the contents of a text file.

    Attempts to decode the bytes using UTF-8 encoding first. If decoding fails due to a UnicodeDecodeError,
    it falls back to decoding with 'latin1' encoding, ignoring any errors.

    Args:
        file_bytes (bytes): The bytes content of the text file.

    Returns:
        str: The decoded text as a string.
    """
    try:
        return file_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return file_bytes.decode("latin1", errors="ignore")