# 	Standard Communication with Network Elements (scone)
* <IETFschedule meets=true>IETF125: Fri 20 Mar 2026 14:00 - Guangdong</IETFschedule>
* [About SCONE](https://datatracker.ietf.org/doc/charter-ietf-scone/)
* Potentially of interest because: resolves tensions between various actors in the ecosystem and its relation to net neutrality (dare we say it).
* Keywords: access/content interaction, Quality of Experience (QoE).

This is a working group is forming as a follow-up of the SCONEPRO BoF.

For both network management and business motivation networks may impose constrains on the amount bandwidth available to users when e.g. streaming video. Currently, applications will adapt heuristically to this throttling by adapting the bit rate and therefore the quality of video streams. This work seeks to signal a subset of applications (those that use QUIC to transport their content) with a so-called throughput advice. The intent is to improve the overall user experience. 


Path signaling elements may be vectors for control, abuse, and side channel attacks (i.e. learn something about the encrypted traffic).  The working group will therefore determine whether it is necessary for an endpoint to explicitly signal its capability of receiving throughput advice, and whether it is necessary for an endpoint to confirm its receipt of throughput advice.

[RFC8558](https://datatracker.ietf.org/doc/html/rfc8558) and [RFC9419](https://datatracker.ietf.org/doc/html/rfc9419) provides general architectural guidance in this space. 
