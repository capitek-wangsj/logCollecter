tsdb mkmetric metric.log.input
tsdb mkmetric metric.log.output


# curl -i -X POST -d '{"metric":"metric.log", "timestamp":1483399262, "value":8, "tags": {"host":"10.0.101.145"}}' http://localhost:4242/api/put?details
# curl -i -X GET http://localhost:4242/api/query?m=sum:metric.log

