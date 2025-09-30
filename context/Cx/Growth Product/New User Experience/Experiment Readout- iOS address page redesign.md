# Experiment Readout: iOS address page redesign

Analytics DRI: Heming Chen

Working team: Manolo Sanudo (eng), Jason Dimitriou (eng), Aniket Patil (eng), Gandhi amar (eng) Zohaib Hassan (eng), Saur Vasil (Product), Steph Chiu (Product)

Last updated: 09/01/2022

### TL;DR

**Context:**The Address/Geo and Growth-NUX team have been partnering on the Address Redesign project on iOS. The goals of this project were:

- **Tailwind to ND rate:** (Never Delivery Rate) given the address entry experience has improved, including validation banners.

- **Introduce DP upsell messaging to guest users:** , future proofing the address flow for future enhancements

- Rewrite Address flows to align with the new architecture for iOS (it’s one of the last remaining modules to finish)

- Create more contextually aware and frictionless address flow, empowering teams like Growth & Hyperlocal to build features relying on address

- Decouple Google entirely from the client for Address flows

- Complete domain knowledge and stability going forward

**Results Summary**iOS address page redesign drove +9k incremental Dashpass trial over a 1-week experiment period,**leading to an estimated 245k incremental Dashpass trial/year, which translates to annualized $52M GMV/year:**- Estimated annualized GMV:**+$52M**

- Success metrics:

  - **+4.06% rel. (stats sig) Dashpass Trial:** -**+245k incremental Dashpass trial/yr**

- Check metrics:

  - Subpremise Rate (Apt/Suit number): +9.23%

  - Never delivery Rate: +0.91% (not stats sig)

  - Order Rate: flat

  - New Cx CVR: flat

- International impact summary:

  - **CAN:** <mark>: Observed positive lift in DP trial but not stats sig
    </mark>

  - **AUS:** <mark>: Observed positive lift in DP trial but not stats sig</mark>*50% haircut applies to MAU & GMV given mutual exclusive from other experiments

| **Treatment**|
| --- |
| ![Drawing 1](images/image_2.png) ![Drawing 2](images/image_1.png)![Drawing 3](images/image_4.png) ![Drawing 4](images/image_5.png) |
|**Control**|
| ![Drawing 5](images/image_3.png) ![Drawing 6](images/image_8.png) ![Drawing 7](images/image_6.png) |**Next steps:**

- <mark>Fast follow sizing bug that is resulting in the minor negative trend for ND. More details, including reasoning for the ship decision, can be found here </mark><mark>. (ETA: 2 weeks)
  </mark>

- <mark>Use this infrastructure to launch
  </mark>

  - <mark>Explore Instantly (NUX/Growth)
    </mark>

  - <mark>Hyperlocal Explore Around Me</mark>

For the full readout, please check out the [experiment result doc](https://docs.google.com/document/d/173tWQLqTL0w2n-4NoO9NgE1T856Y86v467csKis4aJY/edit?usp=sharing)

**Result Details**[Mode Dashboard](https://app.mode.com/doordash/reports/93bb014b3878) (The migration from Mode to Curie still in progress, we are working on Curie metrics pack and aim for completion in Q3)

[Curie Dasboard for quality metrics](https://admin-gateway.doordash.com/tools/decision-systems/experiments/b46ed0c3-bc0c-4da7-9103-0e0a602d4342)

### Experiment Timeline

![Drawing 8](images/image_7_placeholder.png)

### Methodology

#### Overview**Test mechanism:**A/B test**Test platform:**iOS**Country:**Global**Experience:**DoorDash only**Target Population:**Cx who landed on Address page**Test duration:**1 weeks experiment**Control/Treatment Split:**50/50

#### Testing Group & Bucketing

- Treatment (50%): New address page design + DP upsell banner

- Control (50%): Existing address page

- **Test Launch date:** 08/15/2022

### Result Details

#### Success Metrics (Treatment vs Control)

|**Metrics**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- |
| DP trial signup | 0.7563% | 0.7268% | 4.06% | YES |
| Never Delivery Rate | 0.5418% | 0.5369% | 0.91% | NO |
| Subprimise Rate | 4.91% | 4.49% | 9.23% | YES |
| Order Rate | 1.1045 | 1.1060 | -0.13% | NO |
| New Cx Rate | 2.16% | 2.17% | -0.36% | NO |

#### Check Metrics

|**Metrics**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- |
| DP paid sign up | 0.06% | 0.06% | 0.00% | NO |
| HQDR (High quality delivery Ratio) | 93.56% | 93.57% | -0.01% | NO |
| Cancellation | 2.57% | 2.58% | -0.07% | NO |
| Missing & Incorrect | 3.83% | 3.83% | 0.06% | NO |
| Latness | 2.23% | 2.23% | 0.05% | NO |
| MTO | 0.5418% | 0.5369% | 0.91% | NO |

#### Success Metrics by country

|**Country**|**Metrics**|**Treatment**|**Control**|**% Change**|
| --- | --- | --- | --- | --- |
| US | DP trial sign up | 54,568 | 52,604 | 3.73% |
| AUS | DP trial sign up | 1,725 | 1,486 | 16.08% |
| CAN | DP trial sign up | 3,599 | 3,449 | 4.35% |**Next steps:**

- <mark>Fast follow sizing bug that is resulting in the minor negative trend for ND. More details, including reasoning for the ship decision, can be found here </mark><mark>. (ETA: 2 weeks)
  </mark>

- <mark>Use this infrastructure to launch
  </mark>

  - <mark>Explore Instantly (NUX/Growth)
    </mark>

  - <mark>Hyperlocal Explore Around Me
    </mark>
