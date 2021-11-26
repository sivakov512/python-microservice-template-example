import logging

import grpc.aio
from asyncpg_engine import Engine

from proto.services.example import service_pb2_grpc

from .handler import Handler, RequiredProcedures

__all__ = ["run"]


async def run(postgres_url: str, port: int) -> None:
    listen_addr = f"[::]:{port}"

    engine = await Engine.create(postgres_url)
    procedures = RequiredProcedures(engine)
    server = grpc.aio.server()

    service_pb2_grpc.add_ExampleServicer_to_server(Handler(procedures), server)
    server.add_insecure_port(listen_addr)

    logging.info("Starting grpc server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
