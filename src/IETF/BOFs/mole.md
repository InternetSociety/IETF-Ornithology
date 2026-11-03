# Moderation Of unLinkable Endorsements (mole)
* <IETFschedule meets=true>IETF127: Thu 19 Nov 2026 14:00 - Continental 6</IETFschedule>
* [BoF request](https://datatracker.ietf.org/doc/bofreq-thomson-moderation-of-unlinkable-endorsements-mole/)
* Potentially of interest because: Tokens may be gating access to the web, token provision provides potential control points for users to access services.
* Keywords: privacy, centralization, bots.

This working group forming BOF around the following problem.

Websites do not know if a new visitor is a friendly fresh set of eyes, a content scraping agent, a bot searching for vulnerability, or a bot that is in another way troublesome. Traditionally CAPTCHAs were supposed to help, but they are unfriendly to users, and bots are getting exceedingly good solving them. 

MOLE proposes giving browsers something like a digital“good visitor” token. A website could check properties of that token when deciding whether to trust or provide service to a visitor. The system aims to make these tokens unlinkable across different contexts, limiting what websites can learn about the person using them.

To prevent someone from simply resetting their reputation and obtaining endless fresh tokens, MOLE proposes a second, scarce endorsement token. Obtaining one might be tied to something concrete, such as a digital identity, payment system, or user account. The architecture allows different entities to issue these tokens, with the explicit goal of limiting centralization. When an endorsement token is redeemed, the party accepting it would not learn which entity originally issued it.

MOLE is trying to help websites tell trusted visitors from troublesome bots, without making people give up their privacy.