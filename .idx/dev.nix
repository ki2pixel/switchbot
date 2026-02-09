{ pkgs, ... }: {
  # Les packages système
  packages = [
    pkgs.git
  ];

  # Configuration IDX
  idx = {
    # Extensions VS Code
    extensions = [
      # "pkief.material-icon-theme"
    ];

    # Structure directe (sans 'workspace')
    lifecycle = {
      # S'exécute à chaque démarrage
      onStart = {
        sync-repo = "git pull origin main --no-rebase || true";
      };
    };

    # Configuration des aperçus
    previews = {
      enable = true;
      previews = {};
    };
  };
}