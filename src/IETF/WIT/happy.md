# Heuristics and Algorithms to Prioritize Protocol deploYment (happy)
* <IETFschedule>IETF123: Thu 24 Jul 2025 09:30 - Hidalgo</IETFschedule>
* [About HAPPY](https://datatracker.ietf.org/group/happy/about/)
* Keywords: IPv6 deployment, encryption

When clients connect to servers they apply a number of heuristics to determine the 'best' way to connect. The first iterations of the 'happy eyeballs' protocol was used to determine whether a connection to a service over IPv6 could be established with the same experience as over IPv4.

This working group updates the 'happy eyeballs' protocol to version 3. It will need to work with QUIC a recent transport protocol, make use of signals that can be made available in the DNS, and to prepare the protocol to be able to work with Encrypted Client Hello.