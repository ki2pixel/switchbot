{ pkgs, ... }: {
  # 1. Installation des outils
  packages = [
    pkgs.git
  ];

  # 2. Configuration spécifique à IDX
  idx = {
    # Extensions VS Code
    extensions = [
      # "pkief.material-icon-theme"
    ];

    # On utilise "workspace" comme conteneur principal (Re-tentative propre)
    workspace = {
      # C'est ici que se trouve le cycle de vie dans la version stable
      lifecycle = {
        onStart = {
          sync-repo = "git pull origin main --no-rebase || true";
        };
      };
    };
  };
}