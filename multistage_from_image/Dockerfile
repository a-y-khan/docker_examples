FROM ubuntu:18.04 as builder

RUN apt-get update && apt-get install -y \
    build-essential

WORKDIR /opt/build

COPY binomial.cpp .

RUN g++ -o binomial binomial.cpp


FROM ubuntu:18.04

WORKDIR /opt/app

# also works:
#COPY --from=0 /opt/build/binomial .
COPY --from=builder /opt/build/binomial .

CMD ["./binomial"]
