# Experiment Readout: Easy-Scroll Checkout on Android [US only]

Analytics DRI: Heming Chen

Working team: [David Zou](mailto:david.zou@doordash.com) (Android), [Denis Soldatenko](mailto:denis.soldatenko@ext.doordash.com) (design), [Zohaib Sibté Hassan](mailto:zohaib.hassan@doordash.com) (EM), [Saur Vasil](mailto:saur.vasil@doordash.com) (PM)

One-team one-fight shoutout to: legal ([Julia Kripke](mailto:julia.kripke@doordash.com)[Andrew Lim](mailto:andrew.lim@doordash.com)), Order Experience ([Parag Dhanuka](mailto:parag.dhanuka@doordash.com)[Khalid Ashour](mailto:khalid.ashour@doordash.com)[Harsh Alkutkar](mailto:harsh.alkutkar@doordash.com)), Pricing/Promo ([Meghan Desai](mailto:meghan.desai@doordash.com)[Anh Nguyen](mailto:anh.nguyen@doordash.com)[Phil von Keitz](mailto:phil.vonkeitz@doordash.com)), [Carla Sneider](mailto:csneider@doordash.com) (Analytics) [Jimmy Liu](mailto:jl@doordash.com), and more!

Last updated: 09/25/2022

### TL;DR

**Problem:**The existing checkout flows highlight prices on both the order cart page & checkout page by displaying totals on the “continue” & “place order” buttons, this causes:

- **keeps the user’s focus on the price they need to pay rather than the delight of their food:** .

- Price breakdown can only be seen upon scrolling down, **which shocks users by how much extra they need to pay for the food**. For example, if user add a $10.75 cookie into their cart, the first thing they observe on cart page is the red button showing “continue with $14.70” with minimal explanation of the price increase, while users need to scroll down to understand where that $4 increase coming from (delivery fee + service fee + tax).**Solution:**Remove price from both buttons, in favor of requiring users to scroll/click “Next” on checkout to see their full pricing breakdown. This emphasizes:

- Users’ focus on the delight of food instead of price on the cart page

- Greater transparency of fees

- Reduced points of pricing friction

- Better segmentation of checkout experience**Results Summary**Easy-Scroll Checkout on Android drove a +1.59M incremental GMV over a 2-week experiment period,**leading to an estimated +$34M GMV/year**(from subtotal lift + cancellation drop + DP trial subscription lift),**+504k VP lift from decreasing cancellation rate by 1.8 bps, and +100k DashPass trial subscriptions:**- Estimated annualized GMV:**+$34M/year**

- Success Metrics:

  - Subtotal: **+9 cents/order (+0.53% rel.)**

  - Cancellation:

    - **-1.8 bps drop in the US:** +**+$504k/yr VP improvement**+**+20k incremental orders/yr,** translates to $700k GMV

  - DashPass Trial Subscription: **+100k/yr (+4% rel),** translates to $13M GMV

- Check metrics:

  - Tips: -3 cents/order (-0.24% rel.) due to cannibalization

  - Other quality metrics: flat

\*50% haircut applies to MAU & GMV given mutual exclusive from other experiments

| **Before**| ![Drawing 1](images/image_1.png) |
| --- | --- |
|**After**| ![Drawing 2](images/image_3.png) |**Next steps:**

- <mark>Ramp-up plan: Ramped up to 90% treatment + 10% long-term holdout on 09/17
  </mark>

- <mark>Follow-up experiment:
  </mark>

  - <mark>Expand to international markets
    </mark>

  - <mark>Expand to iOS & Web
    </mark>

  - <mark>Highlighting DP trial subscription on the checkout page</mark>

For the full readout, please check out the [experiment result doc](https://docs.google.com/document/d/1aoU0D7IjkhBGm2S4zrrwB9BNwYjmjV1NmOCcdh3pkRM/edit#)
---
**Result Details:** [Mode Dashboard](https://app.mode.com/doordash/reports/2c491ffe4c17) (The migration from Mode to Curie still in progress, we are working on Curie metrics pack and aim for completion in Q4)

[Curie Dashboard](https://admin-gateway.doordash.com/tools/decision-systems/experiments/64c2bfe8-d875-4445-b037-37c34758fe44?analysisId=2fda5680-7d90-492c-98c5-872610f53458) for quality metrics

[Product Doc](https://docs.google.com/document/d/1WN2YDSzsbMIQg8R_-pRelKcsqc-oHzLTswA_UWLrlFM/edit#heading=h.etaqjr1ijy0o)

### Experiment Timeline

![Drawing 3](images/image_2_placeholder.png)

### Methodology

#### Overview**Test mechanism:**A/B test**Test platform:**Android only**Country:**US only**Experience:**DoorDash only**Target Population:**Every Android users**Test duration:**2 weeks**Control/Treatment Split:**50/50

#### Testing Group & Bucketing

- Treatment (50%): New design of order cart page & checkout page

- Control (50%): Existing design

- **Test Launch date:** 08/30/2022

### Result Details

Impacts breakdown:

- **Cx_Cancellation drop of -3.29%:** - Majority coming from who canceled*within 5 mins* after placing orders

- Hypothesis:

  - Increased transparency in checkout -> less likely to regret order after placing

  - Additional tap to checkout -> less likely to accidentally place order and regret tip/total

  - **This change dramatically improved these painpoints.:** -**GMV lift of +$34M/yr**, driven by subtotal lift of +0.38%, +0.24% in GoV

- Moving full pricing information to checkout (industry standard) encourages Cx to be more focused on cart-building in the cart, rather than a focus on pricing.

- Aligns with the industry standard of showing pricing in checkout

- Average cart size -> treatment saw +0.53% lift

*NSS Impact overall Checkout rate (directionally positive at ~0.15% lift)* Directionally positive (NSS) New Cx CVR (~1% lift, we expect this would go stat sig if we let the experiment run longer but we want to launch now to drive growth given current conditions

***DP trial lift of +4%**

  - Increased transparency of fees -> Cx find ways to reduce fees

  - Increased clarity of DP cart upsell (less competing information on cart page)

*Lowers average Tip/order by $0.02 (less than 0.39%)* **Stronger legal footing from consumer transparency pricing breakdown (fees, tip, totals)**#### Success Metrics (Treatment vs Control)

|**Metrics**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- |
| GoV | $36.23 | $36.15 | 0.24% | YES |
| Subtotal | $25.62 | $25.53 | 0.38% | YES |
| Tip | $4.20 | $4.22 | -0.39% | YES |
| Order Rate | 2.5819 | 2.5780 | 0.15% | NO |
| New Cx CVR | 4.25% | 4.21% | 1.15% | NO |

#### Check Metrics

|**Metrics**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- |
| DP trial subscription rate | 3.02% | 2.90% | 4.00% | YES |
| DP DTP subscription rate | 1.29% | 1.27% | 1.05% | NO |
| Cancellation rate | 2.49% | 2.58% | -3.36% | YES |
| HQDR | 90.76% | 90.72% | 0.05% | YES |**Next steps:**

- <mark>Ramp-up plan: Ramped up to 90% treatment + 10% long term holdout on 09/17
  </mark>

- <mark>Follow-up experiment:
  </mark>

  - <mark>Expand to international markets
    </mark>

  - <mark>iOS Version
    </mark>

  - <mark>Highlighting DP trial subscription on checkout page</mark>
