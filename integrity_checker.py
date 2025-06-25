import hashlib
import os

def calculate_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print("❌ File not found.")
        return None

def save_hash(file_path, hash_value):
    """Save the hash to a .hash file."""
    with open(file_path + ".hash", "w") as f:
        f.write(hash_value)

def load_saved_hash(file_path):
    """Load previously saved hash."""
    try:
        with open(file_path + ".hash", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def check_file_integrity(file_path):
    """Main function to check file integrity."""
    print(f"🔍 Checking file: {file_path}")

    current_hash = calculate_hash(file_path)
    if not current_hash:
        return

    saved_hash = load_saved_hash(file_path)

    if not saved_hash:
        print("📦 No previous hash found. Saving current hash...")
        save_hash(file_path, current_hash)
        print("✅ Hash saved. You can now monitor this file.")
    else:
        if current_hash == saved_hash:
            print("✅ File is unchanged.")
        else:
            print("⚠️ WARNING: File has been modified!")

# Example usage
if __name__ == "__main__":
    file_to_check = input("Enter the path to the file you want to monitor: ").strip()
    check_file_integrity(file_to_check)
