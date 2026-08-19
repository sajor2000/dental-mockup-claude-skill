# Dental mockup agent instructions

This repository contains the local `/generate-dental-mockup` skill. Use it for dental concept-photo requests.

- Read `.claude/skills/generate-dental-mockup/SKILL.md` before generating.
- Never request, print, save, or accept an API key in chat. If `OPENAI_API_KEY` is missing, tell the user to close Claude Code and double-click `START-DENTAL-MOCKUP.command`.
- For a patient-specific edit, use the attached patient image or ask for one.
- Keep output local at `~/Data/dental-mockups/`; never write patient images to Dropbox.
