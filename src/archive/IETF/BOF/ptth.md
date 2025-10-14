# Protocol for Transposed Transactions over HTTP(ptth)
<IETFschedule>* Schedule Unknown</IETFschedule>
* [BoF request](https://datatracker.ietf.org/doc/bofreq-rosomakho-protocol-for-transposed-transactions-over-http/)
* Potentially of interest because: A solution in this space may reduce cross vendor service migration costs.
* Keywords: cloud, web services

Normally a web client that connects to a server will initiate a transport connection over TCP or QUIC to a server and then also initiate a web (HTTP) request over to the server. 

This is a non-working group forming BOF to explore use cases where web servers (HTTP) need to contact their client. These use cases usually take place in closed (corporate or cloud) environments. These are often implemented using proprietary protocols and often cause friction during cross-vendor migration. 