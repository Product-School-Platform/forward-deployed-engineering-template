# Ledger: FAC-1844

Client: Harbor & Co, `CL-7781`
Facility: `FAC-1844`
Type: revolving credit
Limit: $800,000
Opened: 14 March 2022
Outstanding today, 16 October 2026: $640,000
Requested limit: $4,200,000 (not booked)

## Covenant

Interest coverage, quarterly, floor 2.0x.

| Quarter | Coverage | Status in Ledger |
|---|---|---|
| 2024 Q2 | 2.4x | met |
| 2024 Q3 | 1.6x | breach, flag still open |
| 2024 Q4 | 2.3x | met |
| 2025 Q4 | 2.6x | met |
| 2026 Q2 | 2.5x | met |

The breach flag does not clear itself when later quarters pass. It clears when a waiver document is attached to this facility id, in this legal entity's Vault folder.

## What Ledger will not tell you

- Whether the waiver letter exists
- Who would be paid from the new money
- Screen status
- Whether a committee has approved the increase

Booking the new limit is a write. It is not available in the pilot. Sam Okonkwo's team books it after Ruth Pell has filed the committee minute in Memo.
