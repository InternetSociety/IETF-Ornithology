# TLS Exported AttestationBoF(expat)
* <IETFschedule>IETF123: Mon 21 Jul 2025 14:30 - Tapices</IETFschedule>
* [BoF request](https://datatracker.ietf.org/doc/bofreq-fossati-tls-exported-attestation-expat/)
* Potentially of interest because: Attestation, when used on the Internet, may lead to gatekeeping and privacy issues.
* Keywords:  security, ioT privacy

In some environments one would want to test the integrity of a system before one allows a connection to it. With trusted computing architecture one can cryptographically proof the integrity of a system and may want to use that information before one allows a connection. Practical use cases may be found in financial service architecture where information is exchanged. There one would like to use all available information to validate if that interconnecting systems have not been tampered with before allowing it to connect. 

This group explores if TLS1.3, one of the main building blocks for secure communication, can be leveraged for the purpose of attestation.

The group focuses on a design within IoT and other closed environments and specifically recognize the risk of attestation on the Internet, [a risk identified by the Internet Architecture Board in 2023](https://datatracker.ietf.org/doc/statement-iab-statement-on-the-risks-of-attestation-of-software-and-hardware-on-the-open-internet/).