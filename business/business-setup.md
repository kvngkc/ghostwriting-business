# What You Need to Run This as a Real Business

The legal and tax parts below assume you're based in **Nigeria**. Change them if you're not. Most sources found were vendor blogs, not regulators, so check every fee and rule on the official site before acting. This is general information, not legal or tax advice.

## 1. Legal registration

| Item | What | Notes |
|------|------|-------|
| Business name | Register with the Corporate Affairs Commission (CAC) at cac.gov.ng | Sole proprietor business name: no minimum capital, roughly NGN 10,000–25,000 according to unofficial guides, a few days to process. You remain personally liable. |
| Limited company (later) | Private limited company with CAC | Higher cost (roughly NGN 40,000–50,000+ by unofficial estimates) but limits personal liability. Consider it once revenue is steady or clients ask for a company counterparty. |
| Documents | Valid ID (NIN, driver's licence or passport), passport photo, business address, description of activities | |

## 2. Tax

| Item | Notes |
|------|-------|
| Tax Identification Number (TIN) | Free. Needed for a business bank account, proper invoicing and VAT registration where it applies. Check the current issuer and process on the official tax authority site, as Nigeria's tax administration changed under the 2025 tax reform laws. |
| Income tax | Your profit is taxable as personal income while you're a sole proprietor. Keep every invoice and expense record. |
| VAT | Check whether your turnover or services require VAT registration, and how exported services (foreign clients) are treated. |
| Bookkeeping | One spreadsheet or accounting tool from day one: invoices issued, payments received, fees, expenses (software, AI, domains). |

Talk to an accountant once you have recurring revenue. It costs less than fixing mistakes later.

## 3. Banking and getting paid

- **Business bank account** in the registered business name.
- **Foreign clients (USD/GBP/EUR):** commonly used options are Grey, Payoneer and Wise. They give you foreign receiving account details and let you convert to naira. PayPal can't receive into Nigerian accounts. Providers have suspended services before, so keep two set up.
- **Nigerian clients:** Paystack invoices/payment links or bank transfer.
- **Invoicing:** monthly in advance, due on receipt, before work starts. Use clear invoice numbers and the client's legal name.
- **Pricing in USD** for foreign clients avoids exchange-rate risk on your side.

## 4. Contracts

Use `business/client-agreement-template.md` for every client and get it reviewed once by a lawyer. It covers:
- scope and revisions
- payment, late payment and pausing work
- ownership: the client owns the final posts once paid
- confidentiality, both ways
- AI use and disclosure: say plainly that you use AI tools in drafting, that a human edits everything and that the client approves everything
- data handling: what you keep, where, for how long
- client responsibility for approving what is published under their name
- term and termination

## 5. Data protection and privacy

- **Nigeria Data Protection Act (NDPA) 2023:** you process personal data (client interviews, prospect contacts). Have a short privacy notice, collect only what you need, keep it secure and delete it when it's no longer needed. Check NDPC guidance on whether you need to register as a data controller.
- **Clients in the UK/EU:** their data is covered by UK/EU GDPR. Your agreement should say how you handle it.
- **AI tools:** use plans whose terms don't train on your inputs (API or business plans). Never paste client material into a free consumer tool that trains on inputs.
- **Storage:** one place per client (a Google Drive folder or a private repo), two-factor authentication on every account, and remove access when a client leaves.

## 6. Outreach compliance

- **US recipients (CAN-SPAM):** accurate sender, honest subject lines, postal address, working opt-out honoured promptly.
- **UK/EU:** B2B email to company addresses generally relies on legitimate interest, with relevance to their job and an opt-out. UK sole traders need consent.
- **LinkedIn:** scheduling your own posts through the native scheduler or official API partners is generally treated as allowed. Tools that automate connection requests, messages, likes or comments, or that run a logged-in browser session, break the User Agreement and risk a ban. Never put a client's LinkedIn password into a bot.
- Keep a do-not-contact list and honour it.

## 7. Platform access for publishing on clients' accounts

- Best: the client connects their own LinkedIn to your scheduler (Postiz, or Publora's connection links) through official login. You never hold their password.
- Alternative: you send approved posts and the client presses publish, or uses LinkedIn's native scheduler.
- Add to the contract that the client can revoke access at any time.

## 8. Tools and running costs

Check current prices before buying.

| Need | Options |
|------|---------|
| Drafting | Claude (API or paid plan), the voice-profile skill in this folder |
| Transcription | Zoom/Google Meet built-in transcripts, Otter, Fireflies |
| Scheduling | Postiz (self-hosted, free software), Publora, LinkedIn native scheduler |
| Automation | n8n (self-hosted), cron + the `draft_posts.py` script |
| Outreach email | Google Workspace mailbox on a separate domain; Instantly or lemlist once volume grows |
| Tracking | Ghostwriting HQ artifact (pipeline, clients, launch) |
| Contracts & e-sign | Docusign, or a PDF plus email confirmation to start |
| Hosting automation | A small VPS (Hetzner, DigitalOcean) or Railway |
| Domains | Main brand domain plus one outreach domain |

## 9. Brand and proof

- One-page website: who you serve, how it works, samples, testimonials, booking link. Don't list prices or results you can't back up.
- Your own LinkedIn, posting 3–5 times a week. It's your best sales asset.
- Case studies, with permission, once you have results.

## 10. Operating rhythm

| When | What |
|------|------|
| Daily | 10 prospects researched and contacted; reply to every response within hours |
| Weekly | Draft → edit → client approval → schedule for every client; pipeline review |
| Monthly | Client interviews, voice profile updates, client reports, invoices, bookkeeping |
| Quarterly | Review pricing, churn, lost reasons; tax filings as required |

## 11. Risks and how to handle them

| Risk | Mitigation |
|------|------------|
| Post contains a false claim | Only use client-supplied facts; client approves everything; contract makes the client responsible for what they publish |
| Client data leak | Business AI plans, 2FA, one folder per client, delete on exit |
| LinkedIn account restriction | No engagement or connection bots; official schedulers only |
| Payment provider suspends service | Keep two receiving providers active |
| Late payment | Invoice in advance; pause work after a stated number of days unpaid |
| Too dependent on one client | Aim for no client above about 30% of revenue |
| Burnout at 5+ clients | Hire an editor; document the process; use the voice profile skill so others can write in each voice |

## Sources

- [Kolonell: CAC registration for freelancers in Nigeria, 2026](https://kolonell.com/en/blog/register-business-cac-freelancer-nigeria-2026)
- [TechEconomy: CAC step-by-step guide](https://techeconomy.ng/cac-step-by-step-guide-to-register-business-in-nigeria)
- [Condia: payment apps for freelancers in Nigeria 2026](https://thecondia.com/money-transfer-payment-apps-freelancer-nigeria/)
- [brands.ng: receiving dollars in Nigeria compared](https://brands.ng/blog/how-to-receive-dollars-in-nigeria-as-a-freelancer-every-option-compared/)
- [Gotham Ghostwriters: AI guidelines](https://gothamghostwriters.com/ai-guidelines/)
- [Bonsai: ghostwriting agreement template](https://hellobonsai.com/a/ghostwriting-agreement-template)
- [LinkedIn automation: what is safe (2026)](https://linkedinpreview.com/blog/linkedin-automation-guide-2026)
- [Cold outreach laws: CAN-SPAM, GDPR, PECR](https://resources.rework.com/libraries/outbound-prospecting/cold-outreach-laws-explained)
- [BounceZero: cold email law guide 2026](https://bouncezero.io/cold-email-law-guide-2026)
