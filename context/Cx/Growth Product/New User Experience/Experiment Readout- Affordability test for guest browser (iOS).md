# Experiment Readout: Affordability test for guest browser (iOS)

Analytics DRI: Heming Chen

Working team: Amit Handa (BE), Manolo Sañudo (iOS), Jayesh Elamgodil (iOS), Zohaib Hassan(EM), Ishaan Kansal (Design), Varun Kerof (PM)

Last updated: 08/18/2021

### TL;DR:

iOS “$0 delivery fee, 1st order” messaging for guest Cx has a stat sig **+28%**New Cx CVR (relative., 24% > 30%). This will add $6.9M in annualized variable profit based +258K incremental New Cx and 59K orders from existing Cx. We plan to ramp to 50% by 8/20 and to 100% by 9/17.**Context: The NUX team is on a mission to build the most seamless 1st order experience in the industry.**<mark>This is one of several improvements planned to achieve this mission</mark>

- Problem: We observed that New Cx who browse as a guest on iOS see higher delivery fees likely resulting in sticker shock.

- Solution: Improve first order affordability messaging for guest browsers. by showcasing $0.00 delivery fee pricing as they browse

- Hypothesis: Improving affordability messaging for iOS Guest Cx on Explore, Store and Cart will increase new Cx conversion of this path by at least 25% [23% to 29%] and will contribute > 250K New Cx/ year.**Results Summary**- Estimated annualized variable profit:**$6.9M**- Annualized VP for 258k incremental new Cx:**$6.7M**- Annualized VP for 59k incremental orders for existing Cx:**$167k**

- New Cx:

  - **+28.28% (rel.) new Cx:** conversion rate via guest browsing (control 23.73% vs treatment 30.44%).

  - **258k incremental new Cx:** -**+2.11% (rel.) overall iOS new Cx CVR.**-**5.6M incremental orders**annually on a rolling basis

- Existing Cx:**+14.62% (rel.) existing Cx conversion rate**via guest browsing (control 10.53% vs treatment 12.07%). This translates to**+59k****incremental orders/year**- MTO (manual task per order): <mark>Saw no difference between treatment and control (</mark><mark>control 0.1187 vs treatment 0.1141 </mark><mark>), </mark><mark>**meaning no significant surge of Cx complaints on free delivery eligibility.**</mark>

- International impact summary (per observed conversion improvements):

  - **Overall:** <mark>: +41k incremental New Cx per year, +5k incremental orders for existing Cx per year
    </mark>

  - **CAN:** <mark>: +14k incremental New Cx per year, +4k incremental orders for existing Cx per year
    </mark>

  - **AUS:** <mark>: +25k incremental New Cx per year, +1k incremental orders for existing Cx per year
    </mark>

  - **JPN:** <mark>: +1k incremental New Cx per year, \<1k incremental orders for existing Cx per year
    </mark>

**Next step:**

- Roll out plans

  - By 9/20*, ramp to 50% (*assuming no objections)

  - By 9/17, ramp to 100% (includes consistent store page delivery fee copy)

- Rerun [skip prominence experiment](https://docs.google.com/document/u/0/d/1X_vHoepLdl_dHvO-uNzph4X-gMlmaGKGaLTN2gua42o/edit): ETA 9/1

  - This will significantly reduce bounce rate (-26%) at onboarding and increase Explore visits (+13%).

  - We believe we can **add 350k to 1M New Cx /year with this change**

**Problems and Solution**The guest path attracts approximately 6.2M visits (6.3% of DoorDash new visits) per year and contributes ~1M New Cx. This path has a New Cx CVR of 15% compared to 42% for New Cx who registered before browsing. We believe there is opportunity to improve this conversion rate and significantly contribute at least additional 250K New Cx annually from this path.**Problem:**Cx who browse as a guest on iOS (i.e. skip sign-up at onboarding) see higher delivery fees on Explore, Store and Cart likely resulting in sticker shock. See below for what these Cx see:

![Drawing 1](images/image_2.png)

New Cx who browse in a signed-in state in contrast get clear messaging that highlights free delivery fee on their order.

![Drawing 2](images/image_3.png)**Hypothesis:**Improving affordability messaging for iOS Guest Cx on Explore, Store and Cart will increase new Cx conversion of this path by at least 25% [23% to 29%] and will contribute > 250K New Cx/ year.**Solution:**

- Show Guest Cx “$0.00 delivery fee, first order” similar to logged in New Cx on Explore. We will also persist the free delivery fee on Store and Cart

![Drawing 3](images/image_4.png)

- Key bug fixes resolved for guest Cx (both control and treatment)

  - A user that has skipped sign-up and closes the app is forced to start all over

  - Non loading explore page on app close + reopen (e.g after 3 days)

  - Payment entry bug for guest / new Cx (only Apple Pay was shown)

  - Event logging issue preventing funnel analysis

#### Experiment Timeline

![Drawing 4](images/image_1_placeholder.png)

**Test mechanism:**A/B test**Test platform:**iOS**Country:**Global**Experience:**DoorDash only**Target Population:**Guest Cx**Test duration:**1 weeks experiment**Control/Treatment Split:**90/10

### Result Details

#### Success Metrics (Treatment vs Control)

|**Metrics**|**Treatment**|**Control**|**Abs Change**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- | --- |
| Existing Cx Conversion rate:<br>Explore > Checkout | 12.07% | 10.53% | 1.54% | 14.62% | YES |
| New Cx Conversion rate: Explore > New Cx checkout | 30.44% | 23.73% | 6.71% | 28.28% | YES |

#### Check Metrics

|**Metrics**|**Treatment**|**Control**|**Abs Change**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- | --- |
| CTR: explore page > store page | 88.05% | 84.12% | 3.93% | 4.67% | YES |
| CTR: store page ><br>cart page | 79.73% | 72.68% | 7.05% | 9.70% | YES |
| CTR: cart page > checkout page | 77.14% | 71.22% | 5.92% | 8.31% | YES |
| MTO | 0.1187 | 0.1141 | 0.0046 | 4.03% | NO |

#### ---

#### Success Metrics by country (Treatment vs Control)

|**Country**|**Metrics**|**Treatment**|**Control**|**Abs Change**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- | --- | --- |
| US | Existing Cx Conversion rate:<br>Explore > Checkout | 12.81% | 11.33% | 1.48% | 13.06% | YES |
| US | New Cx Conversion rate: Explore > New Cx checkout | 31.78% | 25.21% | 6.57% | 26.06% | YES |
| CAN | Existing Cx Conversion rate:<br>Explore > Checkout | 8.43% | 6.75% | 1.68% | 24.89% | YES |
| CAN | New Cx Conversion rate: Explore > New Cx checkout | 25.36% | 18.29% | 7.07% | 38.66% | YES |
| AUS | Existing Cx Conversion rate:<br>Explore > Checkout | 3.79% | 3.27% | 0.52% | 15.90 | YES |
| AUS | New Cx Conversion rate: Explore > New Cx checkout | 32.90% | 21.37% | 11.53% | 53.95% | YES |
| <mark>JPN </mark> | <mark>Existing Cx Conversion rate: </mark><br><mark> Explore > Checkout </mark> | <mark>0.47% </mark> | <mark>0% </mark> | <mark>0.47% </mark> | <mark>N/A </mark> | <mark>NO </mark> |
| <mark>JPN </mark> | <mark>New Cx Conversion rate: Explore > New Cx checkout </mark> | <mark>21.21% </mark> | <mark>15.14% </mark> | <mark>6.07% </mark> | <mark>40.09% </mark> | <mark>NO </mark> |

### Methodology

#### Overview**Test mechanism:**A/B test**Test platform:**iOS**Country:**Global**Experience:**DoorDash only**Target Population:**Guest Cx**Test duration:**1 weeks experiment**Control/Treatment Split:**90/10

#### Testing Group & Bucketing

- Treatment (10%): see “$0 delivery fee, first order” on Explore, Store and Cart

- Control (90%): see delivery fee (e.g. $7.99) on Explore, Store and Cart

- **Test Launch date:** 08/07/2021

### Next Steps

- **\[:** Need discussion with Varun\]

### Appendix

[Launch Plan](https://docs.google.com/document/d/1lRwjmWl4yybzfb9zLHgYhRSFW4LX74fGaQ_Aix2iRsQ/edit?ts=60649fa8#)

[Experiment Launch doc](https://docs.google.com/document/d/1R4AytCDHc977tB1cACVjEr8xXU-Vr5kRgY57BFaiW5w/edit#heading=h.a808l0l87qci)

[Tracking dashboard](https://app.mode.com/doordash/reports/df91570420aa)
