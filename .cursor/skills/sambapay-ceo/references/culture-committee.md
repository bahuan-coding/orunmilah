# Culture committee (agents, not people)

Purpose: own the doctrine of the Welcome Kit, not its grammar. Source of truth: `welcome-kit/`. Same pattern as the licensing committee. The agents design. André Silva decides.

Reconvened 19 Sep 2026 after André Silva's review: the kit was objective and should stay that way; the missing specific was stability, security, who the client is, and why the kit exists.

## Doctrine in one line

We are PaySecure's market enabler in Latin America. We provide always-on payment infrastructure. We do not take our clients' merchants. In each geography where we have structure, the Website Factory serves local merchants. We organise everything we have already discovered, in writing, so every person has the same picture; the deadline is short; Open stays Open.

## Seats

| Seat | Agent | What it refuses to let through |
|---|---|---|
| Chair (decides) | André Silva | — |
| Market-enablement doctrine | `sambapay-opportunities` | Any page that describes a gateway, a PSP or a connector. We create a direct connection; we do not resell a payment-facilitator rail |
| Who the client is | `sambapay-ceo` plus business committee | Any page that disputes a client's merchants. Local merchants on the Website Factory are another niche. Two niches, no conflict of interest |
| PaySecure relationship | `sambapay-governance` | Any page where the reader cannot tell who brings the flow, who opens the rails, and that we run PaySecure's white label (PCI and commercial policies inherited). This premise was the requirement of the system from day one |
| Rate, approval, volume truth | `sambapay-finance` plus business committee | Any page that forgets the scoreboard (approval times margin) or that conflates more than R$ 3 billion already processed with the live book in September (zero). Any page that writes 1 October as a day without volume |
| Always-on engine | personal payment-security skill plus `company-os/product-tech` | Any claim of an SLA percentage, a year count, or a stack we have not named. Years without unavailability is the fact; the number of nines is not |
| Local entity and licence truth | personal PCI / AML / legal skills plus PayFac committee | Any claim of a licence, a PCI status or an entity we do not hold today. Cielo is the Merchant of Record now; we operate as payment facilitator; we will be a sub-acquirer; DD2 is not open yet. Payment facilitator is not sub-acquirer. Platform PCI is PaySecure's, on the white label, not Cielo's Merchant of Record role, and not SambaPay's own SAQ until that scope is closed |
| Clarity for eight people | `sambapay-ceo` | Any sentence that Rafaela and Leandro would read differently, and any word not in `09 Glossary` |

## Tests every Welcome Kit page must pass

1. **The swap test.** Put a competitor's name where SambaPay is. If the sentence is still true, it is generic. Cut it or make it ours.
2. **The PaySecure test.** Can the reader say who brings the volume, who opens the rails, and that operations run on PaySecure's white label?
3. **The scoreboard test.** Are approval and rate named as the two numbers we move?
4. **The obsession test.** Is availability the product? Does the page show why a client lasts (PaySecure: years, several cycles of growth, because the system is stable) rather than selling speed of a ticket?
5. **The "only this" test.** Does the page promise anything outside the rails, the Website Factory, or settlement?
6. **The client test.** Can the reader tell we do not take our clients' merchants, and that local merchants on the Website Factory are another niche?
7. **The transparency test.** Is Open marked Open, and is the kit organising what we already know because the deadline is short?
8. **The status test.** Can the reader say we operate as payment facilitator today and we will be a sub-acquirer, and that those are not the same word? Language: `../sambapay-governance/references/payfac-committee.md`.

## This pass (19 Sep 2026, evening)

André Silva: the kit is objective; keep it; add the specific. Culture of an obsessively online system; years of history without unavailability, twenty-four hours, from everywhere; the service is a URL, a data-centre-level delivery for payments; pay technology means focus, and a focused system is an efficient system; the business model is infrastructure; we do not talk to merchants; clients already have merchants and need stability; they can bring their own payment methods to connect locally in Latin America; they can have payment clients of their own whose volume does not grow without that stability; more than R$ 3 billion already processed on the same architecture; new technology absorbed natively; the most important idea is to organise the company's ideas so everyone has maximum transparency; many points still under discussion; the deadline is short.

Kept: local commercial policy as the product; direct connection versus a rail resold as a payment facilitator; PaySecure brings volume.

## This pass (19 Sep 2026, white label)

We run on PaySecure's white label. Production API keys from the acquirers go to the core team. We configure and reconcile on that instance. Platform PCI is PaySecure's, not Cielo's Merchant of Record role. We inherit PaySecure's commercial policies in other markets. A client with more than one nationality gets one system with local entities and teams already in those markets. Do not write SAQ-B: the page said SAQ-D; the questionnaire type on PaySecure's side remains Open to confirm.

## This pass (19 Sep 2026, two niches)

We do not take our clients' merchants. In each geography where we have structure, the Website Factory serves local merchants. Two niches. No conflict of interest. Do not write "we do not sell to merchants" as if the factory did not exist.

## This pass (20 Sep 2026, how André Silva decides)

André Silva decides. The team elaborated the solution. The deadline is short. He decides by one test: which option brings us closer to revenue from DD2, on the take rate Hansraj proposes, so we cover the company's costs. Write the chain. Do not write that process owners close direction. Do not write command language. The eight must see how he thinks, not a rank.

## This pass (20 Sep 2026, Zoho Mail and Sheila)

Mail is Zoho Mail. Cut Google Workspace. Cut the Tools filler about the company brain and card data in Drive. Sheila Esmeralda is on leave and outside the project. Not in tactical work for now. Correspondence she owned runs through André Silva. Do not invent a new Compliance Officer.

## This pass (20 Sep 2026, André Silva's participation, letters, Sridhar)

André Silva thinks with the team, explores their ideas, and creates solutions with each specialist so we get the best interaction with the entities of each geography and the best commercial conditions for our clients. Institutional relationships: reliability and open doors. We have a strong relationship with our partners, and with our acquirers above all. That relationship is our greatest focus, and our obsession. Never write "getting on with many people". Never write "Being integrated" as the gloss for that. Keep the named processes he already owns.

A letter from Visa, Mastercard or an acquirer is the moment that tells whether this business works. Responsive. Coherent. Facts to André Silva as soon as they exist, so partners can use that speed in our defence. Do not write "André Silva answers; nobody else does" as the whole culture.

Pulse and pack: Sridhar (sri@paysecure.net), Viktoria, Hansraj. Do not write "Sridhar is one person, also called Sri Amit". Do not use viktoria@paysecure.net; write Viktoria.

## This pass (20 Sep 2026, kit for the team)

The Welcome Kit is what the team reads. It never names Company OS. That ledger is the cockpit. Cut from `08`: sharing a password or turning off 2-step verification; speaking for the company without him. Those lines do not go in the email.

## Method

Rewrite the pages the new fact touches. Add glossary terms before using them. Spread the same sentences into `company-os/product-tech`, `company-os/commercial` and `company-os/finance` so the ledger matches the story. One line in the decision log. Run `node scripts/build-kit.mjs check`.
