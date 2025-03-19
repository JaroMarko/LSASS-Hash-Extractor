import sys
import re
import os
import argparse

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def process_file(input_file, output_dir, hash_type):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Create a directory to store the hashes, ignore if it exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for i in range(2, len(lines)):
            if hash_type in lines[i]:
                match = re.search(r'{}\s*:\s*(\S+)'.format(hash_type), lines[i])
                if match:
                    extracted_hash = match.group(1)
                    username_line = lines[i - 2]
                    if username_line.startswith("         * Username"):
                        username = username_line.split(":")[1].strip()
                        sanitized_username = sanitize_filename(username)
                        
                        # Save the hash to a file named by the sanitized username
                        output_path = os.path.join(output_dir, "{}-{}.hash".format(sanitized_username, hash_type.lower()))
                        
                        if os.path.exists(output_path):
                            print("File already exists: {}".format(output_path))
                        else:
                            with open(output_path, 'w') as output_file:
                                output_file.write(extracted_hash)
        
        print("Processing complete. {} hashes saved.".format(hash_type))
    except Exception as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Extract hashes from input file.",
            epilog="Use -h or --help to display this help message."
        )
        parser.add_argument("-i", "--input", required=True, help="Path to the input file.")
        parser.add_argument("-d", "--directory", default="./hashes", help="Directory to save the extracted hashes.")
        parser.add_argument("--hash", choices=["NTLM", "SHA1"], default="NTLM", help="Type of hash to extract (default: NTLM).")
        
        args = parser.parse_args()
        
        input_file = args.input
        output_dir = args.directory
        hash_type = args.hash
        
        process_file(input_file, output_dir, hash_type)
    except Exception as e:
        print(str(e))