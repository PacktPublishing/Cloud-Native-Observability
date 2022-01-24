const api = require('@opentelemetry/api');
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');
const { ConsoleSpanExporter } = require('@opentelemetry/sdk-trace-base');

const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { CollectorTraceExporter } = require('@opentelemetry/exporter-collector');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
const { GrpcInstrumentation } = require('@opentelemetry/instrumentation-grpc');
const { SimpleSpanProcessor } = require('@opentelemetry/sdk-trace-base');
const { registerInstrumentations } = require('@opentelemetry/instrumentation');

var url = 'http://localhost:55681/v1/trace';
if (process.env.OTEL_EXPORTER_OTLP_ENDPOINT) {
  url = process.env.OTEL_EXPORTER_OTLP_ENDPOINT;
}

const collectorOptions = {
  url: url,
};

const exporter = new CollectorTraceExporter(collectorOptions);
const provider = new NodeTracerProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'brokentelephone-js',
  }),
});
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));
provider.addSpanProcessor(new SimpleSpanProcessor(new ConsoleSpanExporter()));
provider.register();
['SIGINT', 'SIGTERM'].forEach(signal => {
  process.on(signal, () => provider.shutdown().catch(console.error));
});

registerInstrumentations({
  instrumentations: [new GrpcInstrumentation()]
});

var messages = require('./brokentelephone_pb');
var services = require('./brokentelephone_grpc_pb');

var grpc = require('@grpc/grpc-js');

async function main() {
  while (true) {
    const span = api.trace.getTracer('testing').startSpan('brokentelephone.js:main()');
    api.context.with(api.trace.setSpan(api.context.active(), span), () => {
      var target;
      if (process.env.NEXT_PLAYER) {
        target = process.env.NEXT_PLAYER;
      } else {
        target = 'localhost:50051';
      }
      var client = new services.BrokenTelephoneClient(target,
                                              grpc.credentials.createInsecure());
      var request = new messages.BrokenTelephoneRequest();
      var message = "This is a message";
      request.setMessage(message);
      client.saySomething(request, function(err, response) {
        if (response == null) {
          console.log("Invalid response from:", target)
        } else {
          console.log('Response from server:', response.getMessage());
        }

      });
    });
    await new Promise(r => setTimeout(r, 1000));
  }
}

main();
