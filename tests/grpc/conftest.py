from unittest import mock

import pytest
from asyncpg_engine import Engine

from example.grpc.handler import RequiredProcedures


class MockedProcedures(RequiredProcedures):
    def __init__(self, db: Engine):
        pass


@pytest.fixture()
def procedures() -> MockedProcedures:
    return MockedProcedures(mock.MagicMock())
