# Super Password Generator

A command-line script that generates a random password from lowercase letters, uppercase letters, digits and symbols.

## Requirements

| Requirement | Why it's needed |
|---|---|
| Python 3.10+ | Runs the script |

There are **no third-party packages** to install: the script only uses Python's built-in `random` module, so no `requirements.txt` is needed.

## Usage

```bash
python password_generator.py
```

```
=============== SUPER PASSWORD GENERATOR ===============
Select a number between 6 and 76
Password length: 16
Your password: k#Tq9dZ=xL2_mWb+
```

The length must be between **6** and **76** (the number of available characters). Anything else raises a `ValueError`.

## Character set

- Lowercase: `a-z`
- Uppercase: `A-Z`
- Digits: `0-9`
- Symbols: `! @ # $ % ^ & * ( ) - _ + =`

## Good to know

- Every character is used **at most once** per password (it uses `random.sample`), which is why the maximum length is 76.
- `random` is not cryptographically secure. For passwords you will really use, consider Python's `secrets` module instead, for example:

  ```python
  import secrets
  password = "".join(secrets.choice(all) for _ in range(passwordLength))
  ```