# Dental mockups: start here

## One-time setup

Copy this `generate-dental-mockup` folder into the project you open with Claude Code:

```text
.claude/skills/generate-dental-mockup/
```

Store the OpenAI key in the Mac login Keychain. This prompts securely and never saves the key in the project:

```zsh
security add-generic-password -U -a "$USER" -s openai.api-key -w
```

Start Claude Code with the key available:

```zsh
export OPENAI_API_KEY="$(security find-generic-password -a "$USER" -s openai.api-key -w)"
claude
```

Do not run Claude with `--bare` because project skills will not load.

## Make a mockup

Attach the patient photograph in Claude Code, then paste this prompt:

```text
/generate-dental-mockup Full aesthetic upgrade. Line up midlines top and bottom. Improve shade. Improve symmetry. Replace missing tooth. Veneers #3-14.
```

For a file already on the Mac instead, use its absolute path:

```text
/generate-dental-mockup --input /absolute/path/to/patient.png Full aesthetic upgrade. Line up midlines top and bottom. Improve shade. Improve symmetry. Replace missing tooth. Veneers #3-14.
```

Claude will show the expanded dental prompt before generating, create one low-quality test image, and ask what feels useful, inaccurate, or needs to change. Images save locally in `~/Data/dental-mockups/`, never Dropbox.
