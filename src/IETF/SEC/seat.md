# Secure Evidence and Attestation Transport (seat)


* <IETFschedule>IETF124: Tue 04 Nov 2025 11:30 - Laurier</IETFschedule>
* [About SEAT](https://datatracker.ietf.org/wg/seat/about/)
* Of interest because: Attestation, when used on the Internet, may lead to gatekeeping and privacy issues.
* Keywords:  security, ioT privacy

In some environments one would want to test the integrity of a system before one allows a connection to it. With trusted computing architecture one can cryptographically proof the integrity of a system and may want to use that information before one allows a connection. Practical use cases may be found in financial service architecture where information is exchanged. There one would like to use all available information to validate if that interconnecting systems have not been tampered with before allowing it to connect. 

This group will extend (D)TLS1.3, one of the main building blocks for secure communication, so that it can be leveraged on attestation.

The [bof request (expat)](https://datatracker.ietf.org/doc/bofreq-fossati-tls-exported-attestation-expat/) specifically recognized the risk of attestation on the Internet, [a risk identified by the Internet Architecture Board in 2023](https://datatracker.ietf.org/doc/statement-iab-statement-on-the-risks-of-attestation-of-software-and-hardware-on-the-open-internet/). The BOF therefore focused on closed environment. That focus is not explicit in working group charter.