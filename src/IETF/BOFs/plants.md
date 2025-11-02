# PKI, Logs, And Tree SignaturesBoF{plants}
* <IETFschedule meets=true>IETF124: Tue 04 Nov 2025 17:00 - Place du Canada</IETFschedule>
* [BoF request](https://datatracker.ietf.org/doc/bofreq-westerbaan-pki-logs-and-tree-signatures-plants/)
* Potentially of interest because: Impact of post-quantum signatures on the Internet's authentication infrastructure
* Keywords:  security, encryption, post-quantum

This BOF discusses the issues caused by the overhead when using post-quantum crypography. In the current PKI two system signatures are generated one for the certificate that is produced and one for the transperancy log. The validation of both signatures has notable size and latency impact on the establishment of encrypted connections. 

This BOF builds on work by [D.Benjamin et al](https://datatracker.ietf.org/doc/draft-davidben-tls-merkle-tree-certs/) which seeks to combine the certification and the transperancy logging under one signature thereby reducing overhead.
 
 Because the work is focused on optimizing an operational aspect of certificate management We do not anticipate public policy issues with this work.