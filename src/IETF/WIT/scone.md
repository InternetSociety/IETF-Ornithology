# 	Standard Communication with Network Elements (scone)
* <IETFschedule>IETF124: Tue 04 Nov 2025 17:00 - Viger</IETFschedule>
* [About SCONE](https://datatracker.ietf.org/doc/charter-ietf-scone/)
* Keywords: access/content interaction, Quality of Experience (QoE), net neutrality (dare we say it)

This is a working group is forming as a follow up of the SCONEPRO BoF.

For both network management and business motivation networks may impose constrains on the amount bandwidth available to users when e.g. streaming video. Currently, applications will adapt heuristically to this throttling by adapting the bit rate and therefore the quality of video streams. This work seeks to signal a subset of applications (those that use QUIC to transport their content) with a so-called throughput advice. The intent is to improve the overall user experience. 


Path signaling elements may be vectors for control, abuse, and side channel attacks (i.e. learn something about the encrypted traffic).  The working group will therefore determine whether it is necessary for an endpoint to explicitly signal its capability of receiving throughput advice, and whether it is necessary for an endpoint to confirm its receipt of throughput advice.

[RFC8558](https://datatracker.ietf.org/doc/html/rfc8558) and [RFC9419](https://datatracker.ietf.org/doc/html/rfc9419) provides general architectural guidance in this space. 
