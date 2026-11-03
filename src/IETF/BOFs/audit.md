# MTA Hooks (audit)
<IETFschedule meets=false></IETFschedule>
* [Charter Proposal](https://datatracker.ietf.org/doc/charter-ietf-mtahooks/)
* Potentially of interest because: we see no public policy issues.
* Keywords: mail processing, mail filtering, MTA extensibility
 
This is a working group forming BOF.S

Mail Transfer Agents (MTAs) are responsible for transferring email on behalf of users. During this process, MTAs may perform or delegate functions such as spam and malware filtering, policy enforcement, cryptographic signing, content transformation, and routing decisions. MTA Hooks proposes a standardized HTTP-based (RESTful) protocol through which an MTA can delegate such per-message processing decisions to external services throughout the lifetime of a message.