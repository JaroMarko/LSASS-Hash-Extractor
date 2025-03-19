# LSASS Hash Extractor

This tool extracts NTLM or SHA1 hashes from a given input file and saves them into individual files named by the sanitized username. It is designed to process output from tools like Mimikatz.

## Features

- Extract NTLM or SHA1 hashes.
- Save hashes in a specified directory.
- Automatically sanitize usernames to create valid filenames.

## Requirements

- Python 3.x

## Usage

Run the script using the following command:

```bash
python lsass-hash-extractor.py -i <input_file> [-d <output_directory>] [--hash <hash_type>]
```

### Arguments

- `-i`, `--input`: **(Required)** Path to the input file containing the hashes.
- `-d`, `--directory`: **(Optional)** Directory to save the extracted hashes. Defaults to `./hashes`.
- `--hash`: **(Optional)** Type of hash to extract. Options are `NTLM` or `SHA1`. Defaults to `NTLM`.

### Example

Extract NTLM hashes from `lsass-dmp.txt` and save them in the default directory:

```bash
python lsass-hash-extractor.py -i lsass-dmp.txt
```

Extract SHA1 hashes and save them in a custom directory:

```bash
python lsass-hash-extractor.py -i lsass-dmp.txt -d ./custom_hashes --hash SHA1
```

## License

This tool is provided as-is for educational and testing purposes.
