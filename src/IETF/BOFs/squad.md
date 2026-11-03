# Scalable QUIC-Assisted Distribution (SQUAD) 
* <IETFschedule meets=true>IETF127: Mon 16 Nov 2026 14:00 - Continental 6</IETFschedule>
* [BoF request](https://datatracker.ietf.org/doc/bofreq-franke-scalable-quic-assisted-distribution-squad/)
* Potentially of interest because: We do not perceive public policy issues
* Keywords: one-to-many, efficiency, security

While a lot, if not most, of the traffic on the Internet is one-to-one, multicast is network-layer mechanism that allows for one-to-many delivery of content. It has its use-cases in media distribution, software updates and video conferencing. Applications that want to use multicast in addition to unicast will have to implement a number of features that are readily available in the unicast network stack. For instance, conventional QUIC gives each receiver authentication, congestion control, loss recovery, etc., whereas applications using IP multicast generally have to provide security, receiver feedback, reliability, congestion response, and fallback themselves.

This non-WG-forming BoF explores the problem and possible approaches, with at least two proposals to extend QUIC so that it can optionally use multicast delivery. The goal is for multicast-enabled QUIC to provide transparent data reception, so that applications do not need to treat data differently depending on whether it is received via multicast or unicast.

