{ pkgs, ... }: {
  # Les packages système à installer
  packages = [
    pkgs.git
  ];

  # Configuration IDX
  idx = {
    # Extensions VS Code à installer
    extensions = [
      # "pkief.material-icon-theme"
    ];

    # On passe directement de 'idx' à 'lifecycle'
    lifecycle = {
      # S'exécute à chaque démarrage de l'espace de travail
      onStart = {
        # Synchronisation sécurisée
        sync-repo = "git pull origin main --no-rebase || true";
      };
    };

    # Configuration des aperçus (Previews)
    previews = {
      enable = true;
      previews = {};
    };
  };
}