# Experiment Readout: Cx New User Mobile Header

Analytics DRI: [Sara Nordstrom](mailto:sara.nordstrom@doordash.com)

Working team: [Helena Huang](mailto:helena.huang@doordash.com)(eng), [Omung Goyal](mailto:omung.goyal@doordash.com)(eng), [Zohaib Sibté Hassan](mailto:zohaib.hassan@doordash.com) (EM), [Saur Vasil](mailto:saur.vasil@doordash.com) (PM), [Shakti Mb](mailto:shakti.m@doordash.com) (Design), [Vero Jimenez](mailto:veronica.jimenez@doordash.com) (research)

### TL;DR

**Problem:**We currently have near equivalent visits between mobile and desktop users, with +70% of them browsing as a guest For this customer cohort, we do not surface prominent entry points for logging those users in platform.**Solution:**- Emphasize “Open in App” as a way to capture users into the App Flow

- For those who have the App, this deeplinks directly into the point of the funnel the user was in

- For those who do not have the App, this tracks the user through Adjust links and opens the App Store.

- Emphasize “Sign in” as a way to capture both signins and signups

- This opens the login modal above the current point of the funnel (does not redirect users)

|**Control**| Treatment |
| --- | --- |
| ![Drawing 1](Experiment-Readout-Cx-New-User-Mobile-Header/images/image_1.png) | ![Drawing 2](Experiment-Readout-Cx-New-User-Mobile-Header/images/image_2.png) |**Results Summary**The Cx New User Mobile Header Experiment drove 15k incremental orders and 10k incremental MAU over an 11 day experiment period,**leading to an estimated annualized +$23.4M**[^1]**GMV/year and 30k incremental MAU**and**8k incremental Q2 exit MAU and $1.2M incremental Q2 GMV**

- <u>Success Metrics
  </u>

  - Estimated annualized incremental GMV: **$23.4M/year**- Estimated annualized incremental MAU:**$30k/year**- Check metrics: Avg GOV per order -1.22%*

- Additional metrics:

  - SUMA: -3.32%

  - App Downloads: +754.42%

[Mode Dashboard](https://app.mode.com/doordash/reports/e897e63ad913)

### Experiment Timeline

![Drawing 3](Experiment-Readout-Cx-New-User-Mobile-Header/images/drawing_3_thumbnail.png)

### Methodology

#### Overview

**Test mechanism:**A/B test**Test platform:**mWeb**Country:**Global**Experience:**DoorDash only**Target Population:**Guest users on mobile web**Test duration:**11 days at 50/50**Control/Treatment Split:**50/50

### Result Details

#### Success Metrics (Treatment vs Control)

|**Metrics**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- |
| Order Rate | 7.52% | 6.86% | +<mark>9.61%</mark> | YES |
| Logins | 8.62% | 8.34% | +<mark>3.35%</mark> | YES |
| MAU | 6.37% | 6.10% | +<mark>4.44%</mark> | YES |

#### Check Metrics

|**Metrics**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- |
| Signups | 3.43% | 3.39% | +1.43% | NO |
| New Cx Rate | 2.26% | 2.30% | -1.54% | NO |
| GoV | $41.49 | $42.01 | -1.22% | YES |

#### Additional Metrics

|**Metrics**|**Treatment**|**Control**|**% Change**|**Significance**|
| --- | --- | --- | --- | --- |
| SUMA | 0.51% | <mark>0.53%</mark> | -3.32% | NO |
| App Downloads | <mark>1.33%</mark> | <mark>0.16%</mark> | +<mark>754.42%</mark> | YES |

Impacts breakdown:**Experiment Context**: This experiment implemented adjust links to take users from mweb to the app, which capture both the mweb device id (the experiment bucket key) and the app device id. Through these links we are able to attribute user behavior in the app to the devices in the treatment group in the experiment. There are 2 shortcomings with this experiment design. First, we only have tracking for treatment devices who go to the app but inevitably some control devices will also go to the app through other methods besides this button and we won’t have any tracking on that. Second, we only ran this experiment for around 2 weeks and during that period drove many incremental users to the app, but due to the short experiment period, we aren’t capturing the long term benefits to a user of the app over mweb. To account for this, we came up with the following methodology:**Method**: After investigating we found that 53% of users who sign up on mweb eventually make their way to the app, so we took a 50% haircut on our results to account for the control users that converted on the app that we have no way of tracking. We also found that New Cx on the App vs. mWeb have significantly higher 12 month order rate and 12 month retention, so we added multipliers to our annualized numbers to account for the long term benefits of the app.

Original numbers:

- Q2 exit

  - Incremental GMV from orders: $680k

  - Incremental MAU: 8k

    - Incremental GMV from MAU: $540k

- Annualized

  - Incremental GMV from orders: 8.5M

  - Incremental MAU: 35k

    - Incremental GMV from MAU: $18.2M

App vs. Web multipliers:

| | **App New Cx**|**Web New Cx**|**Increase**|
| --- | --- | --- | --- |
|**12 month order rate**| 12.0 | 6.6 | +82% |
|**12 month retention**| 16.9% | 9.8% | +72% |

53% of web signups that go on to place orders on the app. We will therefore take an additional 50% haircut.

Updated Numbers:

- Annualized:**+23.4M GMV and +30k MAU**- Incremental GMV from orders: 8.5M*1.82*.5= $7.7M

- Incremental MAU: 35k*1.72*.5=30k

  - Incremental GMV from MAU: $18.2M*1.72*.5= $15.7M

Note on the average GOV/order decrease:

- The decrease in GMV per order is not surprising. If we look at average GOV per order by platform for the last year we see the following:

| **Platform**|**Avg GOV**|
| --- | --- |
| mobile-web | $38.08 |
| desktop | $42.07 |
| android | $35.71 |
| ios | $35.11 |**Next steps:**

- Ramp-up plan: Rollout to 100% and pursue other areas where we can drive mobile web users to the app

- Run future “App Downloads and Redirection” experiments as switchback tests to avoid the need to make the assumptions made above
---
## Footnotes

\[^1\]: This is with a 50% haircut
