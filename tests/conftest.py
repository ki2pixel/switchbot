from __future__ import annotations

from contextlib import ExitStack
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(autouse=True)
def patch_postgres_connection_pool(request):
    """Prevent real PostgreSQL connections during tests (except dedicated store tests)."""
    module_name = getattr(request.module, "__name__", "")
    if module_name.endswith("test_postgres_store"):
        yield
        return

    with ExitStack() as stack:
        mock_pool = stack.enter_context(
            patch("switchbot_dashboard.postgres_store.ConnectionPool")
        )
        stack.enter_context(
            patch("switchbot_dashboard.postgres_store.PostgresStore._ensure_table_exists")
        )

        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        mock_pool.return_value.connection.return_value.__enter__.return_value = mock_connection

        yield
