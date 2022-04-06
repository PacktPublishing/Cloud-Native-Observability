FROM maven:3.6.0-jdk-11-slim AS build
COPY BrokenTelephone/src /home/app/src
COPY BrokenTelephone/pom.xml /home/app
RUN curl -L https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.7.1/opentelemetry-javaagent-all.jar -o /home/app/opentelemetry-javaagent-all.jar
RUN mvn -f /home/app/pom.xml clean package

FROM openjdk:11-jre-slim
COPY --from=build /home/app/target/brokentelephone-0.0.1-jar-with-dependencies.jar /usr/local/lib/brokentelephone.jar
COPY --from=build /home/app/opentelemetry-javaagent-all.jar /usr/local/lib/
EXPOSE 8080
ENTRYPOINT ["java", \
     "-javaagent:/usr/local/lib/opentelemetry-javaagent-all.jar", \
     "-Dserver.host=0.0.0.0", \
     "-Dotel.resource.attributes=service.name=brokentelephone-java", \
     "-Dotel.metrics.exporter=none", \
     "-jar", "/usr/local/lib/brokentelephone.jar" \
]