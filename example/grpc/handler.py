from dataclasses import dataclass

from asyncpg_engine import Engine

from proto.services.example import service_pb2_grpc

__all__ = ["Handler", "RequiredProcedures"]


class RequiredProcedures:
    def __init__(self, db: Engine):
        pass


@dataclass
class Handler(service_pb2_grpc.ExampleServicer):
    procedures: RequiredProcedures
