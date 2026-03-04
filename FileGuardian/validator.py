def check_integrity(current_hash, stored_hash):
    if stored_hash is None:
        return "NEW"
    elif current_hash == stored_hash:
        return "MATCH"
    else:
        return "CORRUPTED"