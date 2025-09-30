# Experiment Readout: Address flow improvement (iOS)

Analytics DRI: @Heming.Chen

Working team: Manolo Sañudo (iOS), Amit Handa (BE), Ishaan Kansal (Design), Varun Kerof (PM) , Zohaib Hassan(EM)

Last updated: 09/16/2021

### TL;DR:

Our v1 experiment targeted Cx who did not have an address on file as they launched the iOS app (right after onboarding). We enabled these Cx to use their device location to help in their address entry. The results are as follows:

- Cx who signed in:

  - Stat sig **+1.29%** Conversion (relative., 48.68% > 49.30%) for Cx and

  - Feature usage was **25%** (1 in 4 of Cx found this useful)

  - **+115k:** **orders per year**-**+$3.45M****GMV**- For Guest and newly signed-up Cx saw no stats sig impact. We observed low feature usage in this group (~5% vs 25% for Cx who signed in). The hypothesis is that New Cx hesitate to share their location with us as we don’t explain the purpose well. We need to do more to help them access this.

![Drawing 1](images/image_11.png)**Next:**

- Roll out to 100% by 9/23 (subject to ship review)

- Plan a v2 experiment (Q4 roadmap candidate) to focus on this page from the lens of Cx who are seeing this for the first time

  - UI will be enhanced to give a more welcoming tone, clear explanation of what is needed, the purpose and a more prominent CTA to the feature.

  - We believe we can add **110k new Cx/year (1.7M orders, $50M GMV)**by improving the feature usage of new Cx to 25%.

### Details**Context: The NUX team is on a mission to build the most seamless 1st order experience in the industry.** <mark>This is one of several improvements planned to achieve this mission</mark>

- Problem:

  - New Cx have to type out their full address as they onboard even though the device location is readily available

  - Existing Cx have to type out a new address when they are out range of their default address

  - New Cx are jarringly (unwelcoming UI 💔) asked for address entry with limited context on what and why

![Drawing 2](images/image_8.png)

- Solution: Relocate the request for location sharing to the address entry screen when it is more relevant for a cx

![Drawing 3](images/image_9.png)

**Results Summary**

- Sign-in Cx:

  - Stat sig **+1.29%** Conversion (relative., 48.68% >49.30%) for Cx and

  - Feature usage was **25%** (1 in 4 of Cx found this useful)

  - **+115k:** **orders per year**-**+$3.45M****GMV**

- Sign up Cx & Guest User: <mark>No stats sig impact due to low feature usage (5.4%)
  </mark>

- Auto login Cx: <mark>No stats sig impact on CVR but see directional positive (</mark>**+0.10% (rel.)**<mark>)</mark>

- Check metrics: <mark>Saw no difference in terms of MTO (manual task per order) & Never delivery rate, </mark><mark>**meaning no negative impact on quality of the address.**</mark>**Next step:**

- Roll out to 100% by 9/23 (subject to ship review)

- Plan a v2 experiment (Q4 roadmap candidate) to focus on this page from the lens of Cx who are seeing this for the first time

  - UI will be enhanced to give a more welcoming tone, clear explanation of what is needed, the purpose and a more prominent CTA to the feature.

  - We believe we can add **110k new Cx/year (1.7M orders, $50M GMV)**by improving the feature usage of new Cx to 25%.

<mark>For more details check the </mark><mark>[experiment readout doc](https://docs.google.com/document/d/1dkq5ijshMTSpLCa382kjliwpkeYLRx5Sp4kZcXWS1gg/edit?usp=sharing)</mark>**Problems and Solution**On iOS, Sign in users have a 98% conversion rate from sign in successful page to explore page (no need to input address information).**In comparison, sign up users saw 86% while guest users saw as low as 70%.**These latter users are asked to complete several pages (address entry) before they can explore DoorDash content. We seek to run an experiment on iOS to relocate the request for location sharing to the address entry screen when it is more relevant for a cx, and we believe we can**add 100K-250K New Cx/year**if this is successful in improving the identity success > explore conversion rate.**Problem:**- New Cx have to type out their full address as they onboard even though the device location is readily available

- Existing Cx have to type out a new address when they are out range of their default address

- New Cx are jarringly (unwelcoming UI 💔) asked for address entry with limited context on what and why

![Drawing 4](images/image_6.png)

![Drawing 5](images/image_10.png)**Hypothesis:**Allowing an iOS Cx to use device location to aid with address entry will increase conversion from view address > view Explore by at least**+0.7% abs (signed in New Cx)**and**+1.5% abs. (guest Cx)**on iOS.**Solution:**![Drawing 6](images/image_5.png)![Drawing 7](images/image_2.png)![Drawing 8](images/image_4.png)![Drawing 9](images/image_7.png)*Existing design:*![Drawing 10](images/image_3.png)*New design*

#### Experiment Timeline

![Drawing 11](images/image_1_placeholder.png)

**Test mechanism:**A/B test**Test platform:**iOS**Country:**US, CAN & AUS**Experience:**DoorDash only**Target Population:**Cx without address information**Test duration:**2 weeks experiment**Control/Treatment Split:**90/10

### Result Details

#### Success Metrics

|**Metrics**|**Authorization Method**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- | --- |
| Address page view -> Conversion | Sign in | 49.30% | 48.68% | 1.29% | YES |
| Address page view -> Conversion | Sign up | 43.96% | 43.83% | 0.30% | NO |
| Address page view -> Conversion | Auto login | 59.82% | 59.76% | 0.10% | NO |
| Address page view -> Conversion | Guest Users | 27.88% | 28.58% | -2.45% | NO |
| Address page view -> Explore | Sign up | 94.05% | 94.15% | -0.11% | NO |
| Address page view -> Explore | Guest Users | 89.95% | 89.88% | 0.09% | NO |

#### Check Metrics

|**Metrics**|**Authorization Method**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- | --- |
| Feature Usage | Sign in | 25.96% | NA | NA | NA |
| Feature Usage | Sign up | 4.71% | NA | NA | NA |
| Feature Usage | Auto login | 15.33% | NA | NA | NA |
| Feature Usage | Guest Users | 8.50% | NA | NA | NA |
| MTO | Sign in | 0.08 | 0.08 | 0.78% | NO |
| MTO | Sign up | 0.11 | 0.11 | 2.03% | NO |
| MTO | Auto login | 0.06 | 0.06 | -0.16% | NO |
| MTO | Guest Users | 0.11 | 0.12 | -3.25% | NO |
| Never Delivery Ratio | Sign in | 0.13% | 0.13% | 1.5% | NO |
| Never Delivery Ratio | Sign up | 0.01% | 0.00% | -46.77% | NO |
| Never Delivery Ratio | Auto login | 0.20% | 0.20% | 1.69% | NO |
| Never Delivery Ratio | Guest Users | 0.08% | 0.06% | 32.20% | NO |

### Methodology

#### Overview**Test mechanism:**A/B test**Test platform:**iOS**Country:**US, CAN & AUS**Experience:**DoorDash only**Target Population:**Cx without address information**Test duration:**2 weeks experiment**Control/Treatment Split:**90/10

#### Testing Group & Bucketing

- Treatment (10%): New design of address flow

- Control (90%): Existing design of address flow

- **Test Launch date:** 09/01/2021

### Next Steps

- Roll out to 100% by 9/23 (subject to ship review)

- Plan a v2 experiment (Q4 roadmap candidate) to focus on this page from the lens of Cx who are seeing this for the first time

  - UI will be enhanced to give a more welcoming tone, clear explanation of what is needed, the purpose and a more prominent CTA to the feature.

  - We believe we can add **110k new Cx/year (1.7M orders, $50M GMV)** by improving the feature usage of new Cx to 25%.

### Appendix

[Product Brief](https://docs.google.com/document/d/1VoApXLWE0EfG1hYA4gxKyF_TwyJkMcjixaTaB_NE_i4/edit#)

[Tracking dashboard](https://app.mode.com/doordash/reports/7b33d9501df5)

[NUX Launch Plan](https://docs.google.com/document/d/1lRwjmWl4yybzfb9zLHgYhRSFW4LX74fGaQ_Aix2iRsQ/edit?ts=60649fa8#)
