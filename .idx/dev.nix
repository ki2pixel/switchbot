{ pkgs, ... }: {
  channel = "stable-24.05";

  # Packages à installer dans l'environnement
  packages = [
    pkgs.git
    pkgs.python311Full
    pkgs.python311Packages.pip
    pkgs.python311Packages.pytest
    pkgs.nodejs_20
    pkgs.postgresql_16
  ];

  # Configuration spécifique à IDX
  idx = {
    # Extensions à installer (liste vide ou à remplir)
    extensions = [ ];

    # Configuration de l'espace de travail
    workspace = {
      onCreate = {
        setup-python-env = ''
          set -euo pipefail
          if [ ! -d .venv ]; then
            python -m venv .venv
          fi
          source .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '';
        default.openFiles = [
          "README.md"
          "docs/README.md"
        ];
      };

      # Commandes exécutées à chaque ouverture de l'espace
      onStart = {
        # Synchronisation Git
        # On utilise une chaîne pour la commande
        sync-repo = "git pull origin main --no-rebase || true";
        run-pytest = ''
          if [ -d .venv ]; then
            source .venv/bin/activate
            python -m pytest || true
          else
            python -m pytest || true
          fi
        '';
        launch-flask = ''
          if [ -d .venv ]; then
            source .venv/bin/activate
          fi
          FLASK_APP=app.py flask run --port=5000 || true
        '';
      };
    };

    # Activation des aperçus
    previews = {
      enable = true;
    };
  };
}