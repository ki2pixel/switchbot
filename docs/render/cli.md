# The Render CLI

Manage your Render resources from the command line.

Use the Render CLI to manage your Render services and datastores directly from your terminal:

![Render CLI Terminal Interface](https://via.placeholder.com/600x300.png?text=Interface+terminal+du+Render+CLI)

Among many other capabilities, the CLI supports:
*   Triggering service deploys, restarts, and one-off jobs
*   Opening a `psql` session to your database
*   Viewing and filtering live service logs

The CLI also supports **non-interactive use** in scripts and CI/CD.

> ℹ️ Please submit bugs and feature requests on the CLI's [public GitHub repository](https://github.com/render-oss/cli).

## Setup

### 1. Install

**Linux/MacOS** (Exemple)

Run the following command:
```bash
curl -fssL https://raw.githubusercontent.com/render-oss/cli/refs/heads/main/install.sh | sh
```

After installation completes, open a new terminal tab and run `render` with no arguments to confirm.

### 2. Log in

The Render CLI uses a **CLI token** to authenticate with the Render platform. Generate a token with the following steps:

1.  Run the following command:
    ```bash
    render login
    ```
    Your browser opens a confirmation page in the Render Dashboard.

2.  Click **Generate token**.
    The CLI saves the generated token to its [local configuration file](#local-config).

3.  When you see the success message in your browser, close the tab and return to your terminal.

4.  The CLI prompts you to set your active workspace.
    You can switch workspaces at any time with `render workspace set`.

You're ready to go!

## Common commands

> ℹ️ **This is not an exhaustive list of commands.**
> * Run `render` with no arguments for a list of all available commands.
> * Run `render help <command>` for details about a specific command.
> * When the Render Shell is unavailable (plan Free), use the HTTP debug route described below to inspect `config/state.json`.

| COMMAND | DESCRIPTION |
| :--- | :--- |
| `login` | Opens your browser to authorize the Render CLI for your account. Authorizing generates a CLI token that's saved locally. If the CLI already has a valid CLI token or [API key](https://render.com/docs/api#authentication), this command instead exits with a zero status. |
| `workspace set` | Sets the CLI's active workspace. CLI commands always operate on the active workspace. |
| `services` | Lists all services and datastores in the active workspace. Select a service to perform actions like deploying, viewing logs, or opening an SSH/psql session. |
| `deploys list [SERVICE_ID]` | Lists deploys for the specified service. Select a deploy to view its logs or open its details in the Render Dashboard. If you don't provide a service ID in interactive mode, the CLI prompts you to select a service. |
| `deploys create [SERVICE_ID]` | Triggers a deploy for the specified service. If you don't provide a service ID in interactive mode, the CLI prompts you to select a service. In [non-interactive mode](#non-interactive-mode), helpful options include:<br>• `--wait` to block until the deploy completes (a failed deploy exits with a non-zero status)<br>• `--commit [SHA]` to deploy a specific commit (Git-backed services only)<br>• `--image [URL]` to deploy a specific Docker image tag or digest (image-backed services only) |
| `psql [DATABASE_ID]` | Opens a psql session to the specified PostgreSQL database. If you don't provide a database ID in interactive mode, the CLI prompts you to select a database. |
| `ssh [SERVICE_ID]` | Opens an SSH session to a running instance of the specified service. If you don't provide a service ID in interactive mode, the CLI prompts you to select a service. |

### Debugger HTTP (fallback sans Shell)

Lorsque l'accès Shell Render n'est pas disponible, vous pouvez exposer temporairement l'état persistant via l'endpoint protégé `/debug/state` :

1. Définir un jeton fort dans l'environnement Render : `STATE_DEBUG_TOKEN=...`
2. Déployer la nouvelle version du dashboard.
3. Appeler l'URL `https://<service>/debug/state?token=<votre_token>` pour récupérer `config/state.json` en JSON.
4. **Désactiver** ou régénérer le jeton après utilisation afin de limiter la surface d'exposition.

L'endpoint retourne `404` si le token est absent ou invalide et ne doit être utilisé que pour du troubleshooting ponctuel.

## Non-interactive mode

By default, the Render CLI uses interactive, menu-based navigation. This default is great for manual use, but not for scripting or automation.

Configure the CLI for non-interactive use in CI/CD and other automated environments with the following steps:

### 1. Authenticate via API key

The Render CLI can authenticate using an API key instead of `render login`. Unlike CLI tokens, API keys do not periodically expire. For security, use this authentication method only for automated environments.

1.  Generate an API key with [these steps](https://render.com/docs/api#authentication).
2.  In your automation's environment, set the `RENDER_API_KEY` environment variable to your API key:
    ```bash
    export RENDER_API_KEY=rnd_RUExip...
    ```

> ℹ️ If you provide an API key this way, it always takes precedence over CLI tokens you generate with `render login`.

### 2. Set non-interactive command options

Set the following options for *all* commands you run in non-interactive mode:

| FLAG | DESCRIPTION |
| :--- | :--- |
| `-o / --output` | Sets the output format. For automated environments, specify `json` or `yaml`. Also supports `text` for unstructured text output, along with the default value `interactive`. |
| `--confirm` | Skips any confirmation prompts that the command would otherwise display. |

**Example: List services in JSON format**
```bash
render services --output json --confirm
```

## Example: GitHub Actions

This example action provides similar functionality to Render's [automatic Git deploys](https://render.com/docs/deploys). You could disable auto-deploys and customize this action to trigger deploys with different conditions.

To use this action, first set the following secrets in your repository:

| SECRET | DESCRIPTION |
| :--- | :--- |
| `RENDER_API_KEY` | A valid Render [API key](https://render.com/docs/api#authentication) |
| `RENDER_SERVICE_ID` | The ID of the service you want to deploy |

**Workflow YAML:**
```yaml
name: Render CLI Deploy
run-name: Deploying via Render CLI
# Run this workflow when code is pushed to the main branch.
on:
  push:
    branches:
      - main
jobs:
  Deploy-Render:
    runs-on: ubuntu-latest
    steps:
      # Downloads the Render CLI binary and adds it to the PATH.
      # To prevent breaking changes in CI/CD, we pin to a
      # specific CLI version (in this case 1.1.0).
      - name: Install Render CLI
        run: |
          curl -L https://github.com/render-oss/cli/releases/download/v1.1.0/render-linux-amd64.zip -o render.zip
          unzip render.zip
          sudo mv cli_v1.1.0 /usr/local/bin/render
      - name: Trigger deploy with Render CLI
        env:
          # The CLI can authenticate via a Render API key without logging in.
          RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
          CI: true
        run: |
          render deploys create ${{ secrets.RENDER_SERVICE_ID }} --output json --confirm
```

## Local config

By default, the Render CLI stores its local configuration at the following path:
```text
$HOME/.render/cli.yaml
```
You can change this file path by setting the `RENDER_CLI_CONFIG_PATH` environment variable.

## Managing CLI tokens

For security, CLI tokens periodically expire. If you don't use the Render CLI for a while, you might need to re-authenticate with `render login`.

View a list of your active CLI tokens from your [Account Settings page](https://dashboard.render.com/settings) in the Render Dashboard. You can manually revoke a CLI token that you no longer need or that might be compromised. Expired and revoked tokens do not appear in the list.