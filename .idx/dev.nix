{ pkgs, ... }: {
  # Les packages système à installer (ex: nodejs, python, go, etc.)
  packages = [
    pkgs.git
    # pkgs.nodejs_20 # Décommentez si vous utilisez Node.js
  ];

  # Configuration des variables d'environnement
  env = {};

  idx = {
    # Recherche d'extensions VS Code à installer par défaut
    extensions = [
      # "pkief.material-icon-theme"
    ];

    # Le cycle de vie de votre environnement
    lifecycle = {
      # S'exécute uniquement à la création du projet
      onCreate = {
        # npm-install = "npm install";
      };

      # S'exécute à CHAQUE démarrage de votre Firebase Studio
      onStart = {
        # Synchronisation automatique avec GitHub au démarrage
        sync-repo = "git pull origin main";
      };
    };

    # Configuration des aperçus (Previews)
    previews = {
      enable = true;
      previews = {
        # web = {
        #   command = ["npm" "run" "dev"];
        #   manager = "web";
        # };
      };
    };
  };
}