{ pkgs, ... }: {
  # Les packages système à installer
  packages = [
    pkgs.git
  ];

  # Configuration de l'environnement IDX
  idx = {
    # Recherche d'extensions VS Code
    extensions = [
      # "pkief.material-icon-theme"
    ];

    # C'est ici qu'il fallait ajouter "workspace"
    workspace = {
      lifecycle = {
        # S'exécute à la création du projet
        onCreate = {
          # Exemple : npm-install = "npm install";
        };

        # S'exécute à CHAQUE démarrage
        onStart = {
          # On ajoute "|| true" pour éviter que le build plante si Git a un souci
          sync-repo = "git pull origin main --no-rebase || true";
        };
      };
    };

    # Configuration des aperçus
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