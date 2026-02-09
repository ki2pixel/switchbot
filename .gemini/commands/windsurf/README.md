# Windsurf Gemini CLI Custom Commands

This directory contains custom slash commands for Gemini CLI that implement the Windsurf workflows.

## Installation

1. Ensure Gemini CLI is installed (version 0.23.0+):
   ```bash
   npm install -g @google/gemini-cli@latest
   ```

2. These commands are already placed in the correct location for this project.

## Available Commands

### `/windsurf:commit-push`
Commits changes and pushes to remote following Windsurf workflow standards.

Usage:
```bash
/windsurf:commit-push fix: Remove unnecessary debug log output
```

### `/windsurf:pull-latest`
Synchronizes local branch with origin/main following Windsurf workflow.

Usage:
```bash
/windsurf:pull-latest
```

### `/windsurf:enhance`
Enhances a prompt with project context, advanced techniques, and specialized skills.

Usage:
```bash
/windsurf:enhance Debug the temperature sensor reading issue
```

## Usage in Project IDX

1. Open terminal in Project IDX
2. Start Gemini CLI:
   ```bash
   gemini
   ```
3. Use any of the commands above with `/windsurf:command-name`

## Command Structure

Each command follows the Windsurf workflow specifications:
- Loads relevant project context
- Executes steps systematically  
- Provides clear output and confirmation
- Integrates with Memory Bank where applicable

## Customization

You can modify the `.toml` files to adapt prompts or add new commands following the same namespace pattern.
