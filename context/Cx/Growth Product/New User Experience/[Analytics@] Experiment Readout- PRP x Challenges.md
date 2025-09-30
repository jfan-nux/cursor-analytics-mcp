# Experiment Readout: PRP x Challenges

Analytics DRI: [Heming Chen](mailto:heming.chen@doordash.com)

Working team: [AG Wright](mailto:annagrace.wright@doordash.com) (Marketing), [Yifan Xiang](mailto:yifan.xiang@doordash.com) (Eng), [Tony Caletti](mailto:tony.caletti@doordash.com) (Ax), [Julie Powers](mailto:julie.powers@doordash.com) (S&O), [Saur Vasil](mailto:saur.vasil@doordash.com)(Product), [Kristin Mendez](mailto:kristin.mendez@doordash.com) (Marketing), [Razeen Jivani](mailto:razeen.jivani@doordash.com) (Growth Product), Journey Platform Team

Last updated: 2/4/2025

### TL;DR

In Q3’24 we launched the Purchaser Retention Program (PRP) x Challenges test, which tested 4 offer structures on PRP: 30% off 3 (current offer), place 2 orders in 2 weeks to get 75% off 1 (14D Challenge), place 3 orders in 4 weeks to get 75% off 2 (28D Challenge), get 30% off 1 for 2 weeks and then place 2 orders in 2 weeks to get 75% off 1 (PRP + 14D Challenge). PRP is a Tranche 5 program (no payback) so the main goal of this test was to find a more efficient offer to move us closer to Tranche 1 (2-year payback).

Based on the results, the 28d Challenge variant drove the highest 28D OR and OF lifts, with an estimated **+$10.2M in annualized incremental GMV**at a**$5.93 28d CPIO and a $2.91 56d CPIO.**However, there was too much noise in the data on the PRP variant to feel confident about the comparison between PRP and the 28D Challenge. Therefore, we recommend testing these two variants head-to-head to get a true apples-to-apples comparison.

### Next Steps:

- **[2/25] Test PRP head-to-head with 28D Challenge:** This will give us a clear base of comparison between these two offer structures so that we can understand the tradeoffs between growth and efficiency. The test will run for 13 weeks.

- **[05/27] Readout & go-forward decision:** Review readout with key XFN partners and align on a go-forward decision based on results.

- **[Q2/H2] Optimizations:** Continue to test into different offer structures and targeting, including NV challenges and focusing on specific pockets of SUMA**.**### Background
Purchaser Retention Program (PRP) is an evergreen Cx retention program that targets New Cx who are not eligible for Adaptive FMX because they are either SUMA (34% of all New Cx) or DashPass subscribers. The program does not pay back (Tranche 5) and we hypothesized that utilizing a Challenges offer structure (placing an order to unlock a promo) would help to improve payback, reduce promo abuse, and deepen engagement. In Q3’24, we launched a test that compared 3 different Challenges offer constructs against the existing PRP offer.

For this test, we focused on SUMA Cx only as DashPass subscribers already were exposed to a Challenges offer structure via a separate program.**Allocation Breakdown**| Variant | D0 - 14 Offer | D 15 - 28 Offer | Experiment Allocation |
| --- | --- | --- | --- |
|**PRP**| 30% off 3 orders<br>30SAVED | | 22.5% |
|**14D Challenge**| Place 2 orders in 2 weeks, get 75% off 1 order<br>75OFFT2 | | 22.5% |
|**28D Challenge**| Place 3 orders in 4 weeks,<br>get 75% off for 2 orders within next 2 weeks<br>75OFFT3 | | 22.5% |
|**PRP + 14D Challenge**| 30% off 1 order (PRP)<br>30DEAL1 | Place 2 orders in 2 weeks,<br>get 75% off 1 order<br>75OFFT4 | 22.5% |
|**Control**| N/A | N/A | 10% |**Key Results** (Curie Dashboard: [Link](https://admin-gateway.doordash.com/decision-systems/experiments/c97359b7-dd75-4aa6-bce9-9089b9ebdfe4?analysisId=e1016d2b-7d36-4b16-9bd3-1951864389b8))

### <mark>The recommendation is to move 100% of the treatment group to the 28D Challenge offer structure. This variant drove </mark><mark>**+$1.16M GMV**</mark><mark>and +</mark><mark>**33k incremental orders** </mark><mark>in-campaign.

</mark>

### <mark>By shifting to 28D Challenge, we’d be able to drive an </mark>**annualized GMV of +$10.21M**and**+292k incremental orders**at a**$5.93 28D CPIO**and**$2.91 56D CPIO**.

<mark>The PRP program is notably efficient, offering immediate payback within the first 28d. However, for this audience, it typically involves a $10 28-day CPIO and doesn't achieve payback. The likely cause is VP variance, given the wide confidence intervals in absolute VP change. Additionally, its impact on the 3-month order rate is lower than the winning group in our milestone challenge, indicating that while PRP boosts short-term order rates, it doesn't encourage long-term habituation.</mark>

**28D Results (winner highlighted in green)**| Variant | 28D Order Rate Lift | 28D Order Frequency Lift | 28D CPIO | D28 Retention Lift | 28D DP Adoption Rate Lift |
| --- | --- | --- | --- | --- | --- |
| PRP | 3.80% | 1.22% (Not SS) | Paid back |**2.54%**| Not SS |
| 14D Challenge | 2.90% | 1.57% (Not SS) | $7.14 | 1.32%(Not SS) | Not SS |
| 28D Challenge |**4.56%**|**3.35%**|**$5.93**| 1.17% (Not SS) | Not SS |
| PRP + 14D Challenge | 3.56% | 1.43% (Not SS) | Paid back | 2.10% | Not SS |**56D Results (winner highlighted in green)**| Variant | 56D Order Rate Lift | 56D Order Frequency Lift | 56D CPIO | D56 Retention Lift | 56D DP Adoption Rate Lift |
| --- | --- | --- | --- | --- | --- |
| PRP | 1.97% (Not SS) | 0.60% (Not SS) | Paid back |**1.36%**| Not SS |
| 14D Challenge | 1.94% (Not SS) | 1.41% (Not SS) | $3.10 (Not SS) | 0.52% (Not SS) | Not SS |
| 28D Challenge |**3.31%**|**2.82%**|**$2.91**| 0.48% (Not SS) | Not SS |
| PRP + 14D Challenge | 2.58% (Not SS) | 1.25% (Not SS) |**$1.95**| 1.32% | Not SS |

- MAU: not statistical significant

- NV MAU: not statistical significant

- Dashpass paid balance: not statistical significant

- Dashpass signup: not statistical significant

### Key Learnings

- **Milestone challenge helps users form habits and encourages repeat engagement.:** The winning group had a challenge program lasting up to 6 weeks, while we observed users keep returning and placing more orders during weeks 7-12, which is a promising indicator of habituation. We should continue to monitor this closely to determine how long we can sustain the impact, as this will affect both payback and long-term value

- We should conside**r testing other milestone challenges to extend the challenge period.**This could further encourage habituation and improve long-term retention rates.

### Methodology

Test mechanism: A/B test

Test platform: All Platform

Country: US

Experience: DoorDash only

Target Population: SUMA Cx who placed 1st order

Test duration: 8-week experiment (09/23/2024 - 11/29/2024 with another 8 weeks monitoring)

Control/Treatment 1/ Treatment 2/Treatment 3/Treatment 4 Split: 10%/22.5%/22.5%/22.5%/22.5%

### Result Details

#### Success Metric

|**Metric Name**|**Treatment**|**Control**|**Absolute Change (UB, LB)**|**Relative Change (UB, LB)**|**P-Value**|
| --- | --- | --- | --- | --- | --- |
| 28-day Order Rate | 1.542808 | 1.475556 | +0.067262 [+0.031681, +0.102844] | +4.5584% [+2.147%, +6.9698%] | 0.000211 |
| 56-day Order Rate | 2.850459 | 2.759184 | +0.09129 [+0.026417, +0.156163] | +3.3086% [+0.9574%, +5.6598%] | 0.005814 |
| CRM promo spend 30d | 0.953495 | 0 | N/A | N/A | N/A |
| CRM promo spend 56d | 1.035569 | 0 | N/A | N/A | N/A |
| 84-day Order Rate | 4.114697 | 3.992619 | +0.122091 [-0.000964, +0.245145] | +3.0579% [-0.0241%, +6.14%] | 0.051821 |

#### Check Metrics

|**Metric Name**|**Treatment**|**Control**|**Absolute Change (UB, LB)**|**Relative Change (UB, LB)**|**P-Value** |
| --- | --- | --- | --- | --- | --- |
| 28 Day Order Frequency | 3.860092 | 3.734862 | +0.125157 [+0.0487, +0.201614] | +3.351% [+1.3039%, +5.3982%] | 0.001335 |
| MAU | 0.298527 | 0.296934 | +0.001593 [-0.003016, +0.006202] | +0.5365% [-1.0157%, +2.0887%] | 0.498149 |
| MTO | 0.098813 | 0.089412 | +0.009395 [+0.000863, +0.017927] | +10.508% [+0.9656%, +20.0504%] | 0.030905 |

### Experiment Timeline

![Drawing 1](images/image_1_placeholder.png)

### Appendix

[Curie Link](https://admin-gateway.doordash.com/decision-systems/experiments/c97359b7-dd75-4aa6-bce9-9089b9ebdfe4?analysisId=e1016d2b-7d36-4b16-9bd3-1951864389b8)

[Campaign Launch Brief](https://docs.google.com/document/d/1DTAuehiMaVl9-5OjszUsZI0E8rRDTWt9VkQzauWH4IA/edit?tab=t.0)
