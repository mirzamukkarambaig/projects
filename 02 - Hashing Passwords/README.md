# Secure Password Management and File Encryption in Python
This project demonstrates how to securely manage passwords and sensitive data in Python. It covers the following:

- Password hashing using the bcrypt library
- Saving hashed passwords and salt in a JSON configuration file
- File encryption using Fernet symmetric encryption provided by the cryptography library
- File decryption and loading of hashed passwords and salt
- Verification of user-entered passwords against stored hashed passwords

Please remember, this project is for demonstration purposes and does not consider other important aspects of security such as secure handling of encryption keys and secure storage of hashed passwords.

## Requirements
The project requires Python 3.6 or later. The following libraries are also required:

- bcrypt
- json
- getpass
- cryptography.fernet
- cryptography.hazmat.primitives
- cryptography.hazmat.primitives.kdf.pbkdf2
- cryptography.hazmat.primitives.asymmetric
- base64
- os

You can install these libraries using pip:

```bash
pip install bcrypt cryptography
```

## Usage
1. Key Generation for Encryption: The notebook generates an encryption key using a password-based key derivation function (PBKDF2) with HMAC and SHA-256.

2. Password Hashing and Saving: The user is prompted to enter a password, which is then hashed and saved, along with a salt, to a JSON configuration file.

3. File Encryption: The JSON configuration file is encrypted using the previously generated key.

4. File Decryption and Password Loading: The encrypted JSON file is loaded, decrypted, and the hashed password and salt are loaded.

5. Password Verification: The user is prompted to enter a password, which is then checked against the stored hashed password.

You can run the project in Jupyter Notebook by opening the Hashing Passwords.ipynb file.

## License
This project is open source, under the terms of the MIT License.

## Contact
If you have any questions, feel free to contact me at "mirza.mukkaram.baig@outlook.com".