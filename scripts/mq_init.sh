rabbitmqctl eval 'rabbit_exchange:declare({resource, <<"/">>, exchange, <<"exchange_logs">>}, topic, true, false, false, []).'

rabbitmqctl eval 'rabbit_amqqueue:declare({resource, <<"/">>, queue, <<"queue_logs">>}, true, false, [], none).'

rabbitmqctl eval 'rabbit_binding:add({binding, {resource, <<"/">>, exchange, <<"exchange_logs">>}, <<"routing_logs">>, {resource, <<"/">>, queue, <<"queue_logs">>}, []}).'