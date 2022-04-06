#!/usr/bin/env python3

from concurrent import futures
import logging
import os

import grpc
import brokentelephone_pb2
import brokentelephone_pb2_grpc


def send_request(message):
    with grpc.insecure_channel(
        os.environ.get("NEXT_PLAYER", "localhost:50051")
    ) as channel:
        stub = brokentelephone_pb2_grpc.BrokenTelephoneStub(channel)
        response = stub.SaySomething(
            brokentelephone_pb2.BrokenTelephoneRequest(message=message)
        )
        return response


class Player(brokentelephone_pb2_grpc.BrokenTelephoneServicer):
    def SaySomething(self, request, context):
        return send_request(request.message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    brokentelephone_pb2_grpc.add_BrokenTelephoneServicer_to_server(Player(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
