FROM ubuntu:18.04

COPY --from=krallin/ubuntu-tini:trusty /usr/local/bin/tini /usr/local/bin/tini

ENTRYPOINT ["/usr/local/bin/tini", "--"]
CMD ["/bin/bash"]