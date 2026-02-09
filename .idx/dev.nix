{ pkgs, ... }: {
  # 1. Installation des outils (indispensable)
  packages = [
    pkgs.git
  ];

  # 2. Configuration IDX
  idx = {
    # Extensions VS Code
    extensions = [ ];

    # Dans certaines versions, workspace est au même niveau que extensions
    workspace = {
      lifecycle = {
        onStart = {
          sync-repo = "git pull origin main --no-rebase || true";
        };
      };
    };
  };
}