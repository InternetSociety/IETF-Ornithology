# Protocol for Transposed Transactions over HTTP (ptth)
* <IETFschedule meets=true>IETF126: Mon 20 Jul 2026 16:30 - Grand Park Hall 3</IETFschedule>
* [BoF request](https://datatracker.ietf.org/doc/bofreq-rosomakho-protocol-for-transposed-transactions-over-http-ptth/)
* Potentially of interest because: except for a protocol offering another tool in the cybersecurity toolbox for server maintainers, we do not identify public policy links.
* Keywords: http, zero-trust

This BoF intends to form a working group to standardize a protocol where HTTP servers can initiate connections to clients. This is relevant for very specific use cases, examples of which are enumerated in the BoF request:

* Servers that are only publicly reachable via a CDN or DDoS defense service, to avoid unauthorized access and DDoS attacks on the backend server.
* Servers whose IP address changes frequently, and rely on an HTTP gateway to provide a stable destination for clients.
* “Hidden services” whose server location is a secret, concealed by an anonymizing transport proxy service.
* On-premise corporate servers, answering queries from an approved externally hosted service.
* Untrusted clients that need access to specific resources but are not permitted to initiate outgoing connections.

A draft charter is available [on GitHub]{https://github.com/ietf-wg-ptth/charter/blob/main/charter.md} 
