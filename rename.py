import os

# === EDIT THIS TO YOUR FOLDER PATH ===
FOLDER = "/Users/oliviamaltz/Downloads/Temple Items/GLINT_kids/lookit-stimuli-novel-glint/img"

# Mapping from old prefix to new prefix
PREFIX_MAP = {
    "rik": "zib",
}

def main():
    for filename in os.listdir(FOLDER):
        old_path = os.path.join(FOLDER, filename)

        # Skip directories
        if not os.path.isfile(old_path):
            continue

        # Find which prefix (if any) this filename starts with
        for old_prefix, new_prefix in PREFIX_MAP.items():
            prefix_with_underscore = old_prefix + "_"
            if filename.startswith(prefix_with_underscore):
                # Build the new filename: replace only the prefix
                rest = filename[len(prefix_with_underscore):]  # everything after "mipen_", etc.
                new_filename = new_prefix + "_" + rest
                new_path = os.path.join(FOLDER, new_filename)

                # If there's already a file with the new name, don't overwrite
                if os.path.exists(new_path):
                    print(f"Skipping (target exists): {filename} -> {new_filename}")
                else:
                    print(f"Renaming: {filename} -> {new_filename}")
                    os.rename(old_path, new_path)

                # Important: break so we don't try other prefixes on this file
                break

if __name__ == "__main__":
    main()
