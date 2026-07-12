# Kemal's Password Manager Project

## The App
A terminal password manager where you can save, look up, and delete login info for your favorite sites — all stored in a dictionary and saved to a file so your passwords don't disappear when you close the program.

## What You'll Build (Phase by Phase)

### Phase 1 — Dictionary + Menu Loop
Store passwords in a dictionary. Build a while loop menu to add, look up, and delete entries.

### Phase 2 — Save to a File
Use Python's `json` module to save your dictionary to a file so your data persists between runs.

### Phase 3 — Master Password
Add a master password at the start of the app. If the user gets it wrong, the app closes. If they get it right, they're in.

## Example Output (Phase 1)

```
Welcome to your Password Manager!

What do you want to do?
1. Add a login
2. Look up a login
3. Delete a login
4. Quit

If user clicks choice 1:
Choice: 1
Site: Instagram
Username: kemal123
Password: abc123
Saved!

If a user clicks choice: 2
Site: Instagram
Username: kemal123 | Password: abc123

If a user clicks choice: 4
Goodbye!
```

## Tech You'll Use
- Dictionaries
- While loops
- Functions
- `json` module