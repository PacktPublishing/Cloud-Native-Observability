// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var brokentelephone_pb = require('./brokentelephone_pb.js');

function serialize_BrokenTelephoneRequest(arg) {
  if (!(arg instanceof brokentelephone_pb.BrokenTelephoneRequest)) {
    throw new Error('Expected argument of type BrokenTelephoneRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_BrokenTelephoneRequest(buffer_arg) {
  return brokentelephone_pb.BrokenTelephoneRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_BrokenTelephoneResponse(arg) {
  if (!(arg instanceof brokentelephone_pb.BrokenTelephoneResponse)) {
    throw new Error('Expected argument of type BrokenTelephoneResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_BrokenTelephoneResponse(buffer_arg) {
  return brokentelephone_pb.BrokenTelephoneResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var BrokenTelephoneService = exports.BrokenTelephoneService = {
  saySomething: {
    path: '/BrokenTelephone/SaySomething',
    requestStream: false,
    responseStream: false,
    requestType: brokentelephone_pb.BrokenTelephoneRequest,
    responseType: brokentelephone_pb.BrokenTelephoneResponse,
    requestSerialize: serialize_BrokenTelephoneRequest,
    requestDeserialize: deserialize_BrokenTelephoneRequest,
    responseSerialize: serialize_BrokenTelephoneResponse,
    responseDeserialize: deserialize_BrokenTelephoneResponse,
  },
};

exports.BrokenTelephoneClient = grpc.makeGenericClientConstructor(BrokenTelephoneService);
