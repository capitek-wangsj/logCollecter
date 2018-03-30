tsdb mkmetric metric.log

curl -i -X POST –d '{"metric":"metric.log","timestamp": 1483399261, "value":6, "tags":{"host":"10.0.101.145"}}' http://localhost:4242/api/put?summary

curl -i -X POST -d '{"metric":"metric.log", "timestamp":1483399262, "value":8, "tags": {"host":"10.0.101.145"}}' http://localhost:4242/api/put?details

curl http://localhost:4242/api/query?start=2h-ago&m=sum:rate:proc.stat.cpu{h
ost=foo,type=idle

curl http://localhost:4242/api/search/tsmeta?query=&limit=3&start_index=0

curl curl http://localhost:4242/api/metadata/metric