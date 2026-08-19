---
name: generate-dental-mockup
description: "Generate or edit dental patient concept photos with OpenAI GPT Image 2 through the approved BAA-covered API endpoint. Use when testing dental-image prompts, making a patient-specific mockup, applying a prompt to a patient reference image, comparing prompt variants, or preparing an image to collect patient feedback."
---

# Generate Dental Mockup

Use the caller's prompt as the test artifact. Do not silently change it; show the expanded API prompt before generating so feedback stays attributable to the original request.

The image task is `$ARGUMENTS`. If it is empty, ask for an image prompt. If it contains `--input PATH`, use that patient image and treat the rest as the image prompt.

Before generating, read `${CLAUDE_SKILL_DIR}/references/dental-anatomy.md`. Expand terse clinician language into tooth anatomy and rendering constraints without changing the requested scope or making treatment recommendations. Show both the original request and expanded prompt.

## API key

Start Claude Code from a terminal with the key set for that session. This keeps the key out of chat, the repository, and shell history:

```zsh
read -rs "OPENAI_API_KEY?OpenAI API key: "
print
export OPENAI_API_KEY
claude
```

Do not use `--bare`: it does not load project skills.

## Generate

Use the approved `https://api.openai.com` endpoint configured by the bundled script; do not redirect patient data elsewhere.

- If `--input` is absent, use the one patient image already attached or referenced. If there is no unambiguous patient image, ask for one before a patient-specific edit.
- Resolve an ambiguous numbering system or missing-tooth site first. A `#` range such as `#3-14` means the Universal permanent-tooth system unless stated otherwise.
- Make the first test one low-quality `1024x1024` image. Use medium or high only when requested or creating a selected final candidate.
- Run:

  ```bash
  python3 "${CLAUDE_SKILL_DIR}/scripts/generate_mockup.py" \
    --prompt "PROMPT" \
    --quality low \
    --size 1024x1024
  ```

  Add `--input path/to/patient-reference.png` for a patient-specific mockup.

- Report the original request, expanded prompt, model, quality, size, and absolute output path; display or link the image when supported.
- Label the result: `AI-generated concept preview; not a diagnosis or prediction of treatment outcome.`

## Prompt feedback

Generate one image at a time unless the user explicitly asks for variants. For comparisons, change one prompt element at a time and clearly label each output.

Offer these three feedback questions:

- What feels useful or realistic?
- What feels inaccurate or misleading?
- What one change would make this more helpful?

Never diagnose, recommend treatment, guarantee an outcome, or describe the mockup as an expected result.

## Check

Run the offline self-check without an API key:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/generate_mockup.py" --self-check
```
