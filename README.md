# Dental mockups in Claude Code

No Git knowledge needed.

1. On this GitHub page, click **Code**, then **Download ZIP**. Double-click the downloaded ZIP.
2. Open the new folder and double-click **START-DENTAL-MOCKUP.command**. The first time, macOS may require right-click → **Open**.
3. When Terminal asks, copy and paste the OpenAI API key into its secure Keychain prompt. The key is saved in the Mac login Keychain, never in this folder or Claude chat. Claude Code then opens automatically.
4. Drag the patient photo into Claude Code and paste:

```text
/generate-dental-mockup Full aesthetic upgrade. Line up midlines top and bottom. Improve shade. Improve symmetry. Replace missing tooth. Veneers #3-14.
```

Claude will show the expanded dental prompt before generating one low-quality concept image and ask what should change. Images save locally at `~/Data/dental-mockups/`, never Dropbox.

If Claude Code is already open, close it and start it with `START-DENTAL-MOCKUP.command` so it receives the Keychain-backed API key.
