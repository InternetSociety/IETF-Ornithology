# PKI, Logs, And Tree Signatures (plants)
* <IETFschedule meets=true>IETF126: Mon 20 Jul 2026 14:00 - Grand Park Hall 3</IETFschedule>
* [About PLANTS](https://datatracker.ietf.org/group/plants/about/)
* Potentially of interest because: Impact of post-quantum signatures on the Internet's authentication infrastructure
* Keywords: security, encryption, post-quantum

This BOF discusses the issues caused by the overhead when using post-quantum cryptography. In the current PKI two system signatures are generated one for the certificate that is produced and one for the transparency log. The validation of both signatures has notable size and latency impact on the establishment of encrypted connections. 

This BOF builds on work by [D. Benjamin et al.](https://datatracker.ietf.org/doc/draft-davidben-tls-merkle-tree-certs/) which seeks to combine the certification and the transparency logging under one signature thereby reducing overhead.
 
 Because the work is focused on optimizing an operational aspect of certificate management We do not anticipate public policy issues with this work.