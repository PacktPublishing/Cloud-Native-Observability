FROM golang:1.17
WORKDIR /go/src/github.com/PacktPublishing/Cloud-Native-Observability/chapter3/go/
COPY . ./
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o brokentelephone .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/PacktPublishing/Cloud-Native-Observability/chapter3/go/brokentelephone ./
CMD ["./brokentelephone"]
