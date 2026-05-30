-- Templates pour les stratégies de backup PostgreSQL
-- Ces requêtes peuvent être utilisées pour déclencher ou vérifier des backups.

-- Démarrer un backup logique manuel (pour une migration)
SELECT pg_start_backup('migration_backup', true);

-- [Vos commandes pg_dump ou pg_basebackup ici]

-- Arrêter le backup logique
SELECT pg_stop_backup();

-- Vérifier la taille de la base
SELECT pg_size_pretty(pg_database_size(current_database()));
