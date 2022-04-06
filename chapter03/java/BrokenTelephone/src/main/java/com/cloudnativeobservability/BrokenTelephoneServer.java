package com.cloudnativeobservability;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import java.io.IOException;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

public class BrokenTelephoneServer {
    private static final Logger logger = Logger.getLogger(BrokenTelephoneServer.class.getName());

    private Server server;

    private void start() throws IOException {
        /* The port on which the server should run */
        int port = 50051;
        server = ServerBuilder.forPort(port).addService(new BrokenTelephoneImpl()).build().start();
        logger.info("Server started, listening on " + port);
        Runtime.getRuntime().addShutdownHook(new Thread() {
            @Override
            public void run() {
                // Use stderr here since the logger may have been reset by its JVM shutdown
                // hook.
                System.err.println("*** shutting down gRPC server since JVM is shutting down");
                try {
                    BrokenTelephoneServer.this.stop();
                } catch (InterruptedException e) {
                    e.printStackTrace(System.err);
                }
                System.err.println("*** server shut down");
            }
        });
    }

    private void stop() throws InterruptedException {
        if (server != null) {
            server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
        }
    }

    /**
     * Await termination on the main thread since the grpc library uses daemon
     * threads.
     */
    private void blockUntilShutdown() throws InterruptedException {
        if (server != null) {
            server.awaitTermination();
        }
    }

    /**
     * Main launches the server from the command line.
     */
    public static void main(String[] args) throws IOException, InterruptedException {
        final BrokenTelephoneServer server = new BrokenTelephoneServer();
        server.start();
        server.blockUntilShutdown();
    }

    static class BrokenTelephoneImpl extends BrokenTelephoneGrpc.BrokenTelephoneImplBase {

        @Override
        public void saySomething(Brokentelephone.BrokenTelephoneRequest req,
                StreamObserver<Brokentelephone.BrokenTelephoneResponse> responseObserver) {
            Brokentelephone.BrokenTelephoneResponse reply = Brokentelephone.BrokenTelephoneResponse.newBuilder()
                    .setMessage("Hello " + req.getMessage()).build();
            responseObserver.onNext(reply);
            responseObserver.onCompleted();
        }
    }
}
