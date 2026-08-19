#!/bin/zsh
# Starts Claude Code with an OpenAI key loaded from the macOS login Keychain.
set -e

cd -- "${0:A:h}"

if [[ "${1:-}" == "--check" ]]; then
  command -v security >/dev/null
  command -v claude >/dev/null
  print "Ready: double-click START-DENTAL-MOCKUP.command"
  exit
fi

if ! command -v claude >/dev/null; then
  print -u2 "Claude Code is not installed. Install it, then run this file again."
  exit 1
fi

if ! security find-generic-password -a "$USER" -s openai.api-key -w >/dev/null 2>&1; then
  print "A secure Keychain prompt is next. Click this Terminal, paste the OpenAI API key, and press Return. The characters will not appear; that is normal."
  print "Nothing will be saved in this folder or sent to Claude Code."
  security add-generic-password -U -a "$USER" -s openai.api-key -w
fi

export OPENAI_API_KEY="$(security find-generic-password -a "$USER" -s openai.api-key -w)"
[[ -n "$OPENAI_API_KEY" ]] || {
  print -u2 "Could not read the OpenAI API key from Keychain."
  exit 1
}

exec claude
