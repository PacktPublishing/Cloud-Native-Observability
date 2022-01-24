package com.cloudnativeobservability;

import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;
import io.grpc.BindableService;

/**
 */
@javax.annotation.Generated(value = "by gRPC proto compiler", comments = "Source: brokentelephone.proto")
public final class BrokenTelephoneGrpc {

  private BrokenTelephoneGrpc() {
  }

  public static final String SERVICE_NAME = "BrokenTelephone";

  // Static method descriptors that strictly reflect the proto.
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<Brokentelephone.BrokenTelephoneRequest, Brokentelephone.BrokenTelephoneResponse> METHOD_SAY_SOMETHING = io.grpc.MethodDescriptor.<Brokentelephone.BrokenTelephoneRequest, Brokentelephone.BrokenTelephoneResponse>newBuilder()
      .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
      .setFullMethodName(generateFullMethodName("BrokenTelephone", "SaySomething"))
      .setRequestMarshaller(
          io.grpc.protobuf.ProtoUtils.marshaller(Brokentelephone.BrokenTelephoneRequest.getDefaultInstance()))
      .setResponseMarshaller(
          io.grpc.protobuf.ProtoUtils.marshaller(Brokentelephone.BrokenTelephoneResponse.getDefaultInstance()))
      .build();

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static BrokenTelephoneStub newStub(io.grpc.Channel channel) {
    return new BrokenTelephoneStub(channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output
   * calls on the service
   */
  public static BrokenTelephoneBlockingStub newBlockingStub(io.grpc.Channel channel) {
    return new BrokenTelephoneBlockingStub(channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the
   * service
   */
  public static BrokenTelephoneFutureStub newFutureStub(io.grpc.Channel channel) {
    return new BrokenTelephoneFutureStub(channel);
  }

  /**
   */
  public static abstract class BrokenTelephoneImplBase implements BindableService {

    /**
     */
    public void saySomething(Brokentelephone.BrokenTelephoneRequest request,
        io.grpc.stub.StreamObserver<Brokentelephone.BrokenTelephoneResponse> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_SAY_SOMETHING, responseObserver);
    }

    @java.lang.Override
    public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor()).addMethod(METHOD_SAY_SOMETHING,
          asyncUnaryCall(
              new MethodHandlers<Brokentelephone.BrokenTelephoneRequest, Brokentelephone.BrokenTelephoneResponse>(this,
                  METHODID_SAY_SOMETHING)))
          .build();
    }
  }

  /**
   */
  public static final class BrokenTelephoneStub extends io.grpc.stub.AbstractStub<BrokenTelephoneStub> {
    private BrokenTelephoneStub(io.grpc.Channel channel) {
      super(channel);
    }

    private BrokenTelephoneStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected BrokenTelephoneStub build(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new BrokenTelephoneStub(channel, callOptions);
    }

    /**
     */
    public void saySomething(Brokentelephone.BrokenTelephoneRequest request,
        io.grpc.stub.StreamObserver<Brokentelephone.BrokenTelephoneResponse> responseObserver) {
      asyncUnaryCall(getChannel().newCall(METHOD_SAY_SOMETHING, getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class BrokenTelephoneBlockingStub extends io.grpc.stub.AbstractStub<BrokenTelephoneBlockingStub> {
    private BrokenTelephoneBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private BrokenTelephoneBlockingStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected BrokenTelephoneBlockingStub build(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new BrokenTelephoneBlockingStub(channel, callOptions);
    }

    /**
     */
    public Brokentelephone.BrokenTelephoneResponse saySomething(Brokentelephone.BrokenTelephoneRequest request) {
      return blockingUnaryCall(getChannel(), METHOD_SAY_SOMETHING, getCallOptions(), request);
    }
  }

  /**
   */
  public static final class BrokenTelephoneFutureStub extends io.grpc.stub.AbstractStub<BrokenTelephoneFutureStub> {
    private BrokenTelephoneFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private BrokenTelephoneFutureStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected BrokenTelephoneFutureStub build(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new BrokenTelephoneFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Brokentelephone.BrokenTelephoneResponse> saySomething(
        Brokentelephone.BrokenTelephoneRequest request) {
      return futureUnaryCall(getChannel().newCall(METHOD_SAY_SOMETHING, getCallOptions()), request);
    }
  }

  private static final int METHODID_SAY_SOMETHING = 0;

  private static final class MethodHandlers<Req, Resp> implements io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final BrokenTelephoneImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(BrokenTelephoneImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
      case METHODID_SAY_SOMETHING:
        serviceImpl.saySomething((Brokentelephone.BrokenTelephoneRequest) request,
            (io.grpc.stub.StreamObserver<Brokentelephone.BrokenTelephoneResponse>) responseObserver);
        break;
      default:
        throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
      default:
        throw new AssertionError();
      }
    }
  }

  private static final class BrokenTelephoneDescriptorSupplier implements io.grpc.protobuf.ProtoFileDescriptorSupplier {
    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return Brokentelephone.getDescriptor();
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (BrokenTelephoneGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new BrokenTelephoneDescriptorSupplier()).addMethod(METHOD_SAY_SOMETHING).build();
        }
      }
    }
    return result;
  }
}
