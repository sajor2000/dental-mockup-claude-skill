# Dental Mockup Claude Code Skill

Clone this repository, open it in Claude Code, and use the `/generate-dental-mockup` command to create or edit dental concept previews with OpenAI GPT Image 2.

## Two-minute setup

```zsh
git clone https://github.com/sajor2000/dental-mockup-claude-skill.git
cd dental-mockup-claude-skill
security add-generic-password -U -a "$USER" -s openai.api-key -w
export OPENAI_API_KEY="$(security find-generic-password -a "$USER" -s openai.api-key -w)"
claude
```

The Keychain command securely prompts for the API key once; never paste a key into Claude or save it in this repository.

Attach a patient photograph, then paste:

```text
/generate-dental-mockup Full aesthetic upgrade. Line up midlines top and bottom. Improve shade. Improve symmetry. Replace missing tooth. Veneers #3-14.
```

For a local reference image, add `--input /absolute/path/to/patient.png`. Read [START-HERE.md](.claude/skills/generate-dental-mockup/START-HERE.md) for the full guide. Outputs are local at `~/Data/dental-mockups/`; never use Dropbox.
