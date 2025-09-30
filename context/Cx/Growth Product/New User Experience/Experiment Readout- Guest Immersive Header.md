[Experiment Results] Guest Cx Immersive Header expected to drive $13.9M 12 Month GMV, +27.8K 12 Month Exit MAU

**Analytics DRI**: [Xiao Tan](mailto:xiao.tan@doordash.com)**Working team**: [Saur Vasil](mailto:saur.vasil@doordash.com)(PM) [David Zou](mailto:david.zou@doordash.com)(Eng) [Marina Sawaya](mailto:marina.mukhina@doordash.com) (Eng) [Jim Kim](mailto:james.kim@doordash.com)[Shakti Mb](mailto:shakti.m@doordash.com)(Design)**Last Updated**: 01/23/2024

# TL;DR

**Background**Every month, we have around 900,000 Cx who land on the DoorDash app using Guest Mode.

Guest Mode provides guests with a taste of DoorDash’s selection, especially when they are not ready to log in or sign up. However, we've learned that when customers log in or sign up, they have a more relevant and personalized experience, making them more likely to place an order.**Solution**An immediate solution to this problem is to introduce a prominent, action-oriented surface at the top of the funnel for Guest Browsers to help provide context on the value of signing up or logging in.**We believe this will improve login and signup rates in the Guest Funnel and lead to increased long-term Monthly Active Users (MAU).**|**Treatment (USA)**|
| --- |
| ![Drawing 1](images/image_2.png) |

|**Treatment (Canada)**|
| --- |
| ![Drawing 2](images/image_3.png) |

|**Treatment (AUS)**|
| --- |
| ![Drawing 3](images/image_4.png) |

|**Treatment (NZ)**|
| --- |
| ![Drawing 4](images/image_1.png) |**Results**-**iOS**(All Cx who land on the explore page were exposed to the experiment, including Guest Cx and Cx who signed in)

<u>Success Metric and Input Metrics
</u>

- **Login Rate:** : +0.0267% abs lift (stat sig),**leading to an estimated $13.3M 12 Month GMV, +26.6K 12 Month Exit MAUs**-**Order Rate** :

- +0.0173% abs lift (stat sig)

<u>Check Metrics:
</u>

- Cx app quality latency (See details from Curie [here](https://admin-gateway.doordash.com/decision-systems/experiments/8144a140-79d1-4514-8f47-98a42fede3b4?analysisId=04b2043a-08e1-4e6f-bd96-a95f09eed49c))

  - No <mark>detrimental</mark> stat sig change

- **Android:** (Only Cx who land on the explore page using Guest Mode were exposed)

<u>Success Metric and Input Metrics
</u>

- **Login Rate:** :

- +0.96% abs lift (stat sig), **leading to an estimated $595.8K 12 Month GMV, +1.2K 12 Month Exit MAU**

* Order Rate :

  - +0.90% abs. directional uplift

<u>Check Metrics:
</u>

- Cx app quality latency (See details from Curie [here](https://admin-gateway.doordash.com/decision-systems/experiments/4e49a5ef-34c4-4a7f-9464-a88c0a231492?analysisId=770cd842-b6df-41f6-a7a9-d65a6ba3e8cf))

  - No <mark>detrimental</mark> stat sig change

- **International Metrics:** (Limited to Guest Cx only)

|**Tag**|**Device Region**|**Overall Signup Rate**|**Signup Rate Rel. Uplift** |
| --- | --- | --- | --- |
| Control | CA | 11.71% | |
| Treatment | CA | 12.81% | +9.33% |
| Control | AU | 14.41% | |
| Treatment | AU | 14.53% | +0.88% |
| Control | NZ | 19.35% | |
| Treatment | NZ | 24.45% | +26.32% |

Signup Rate on iOS

*50% haircut applies to MAU & GMV given mutual exclusive from other experiments**Next steps**

- We added the feature to the Q4 2023 NUX device id level long term holdout group to monitor the long term behaviors.

# Methodology

Test mechanism: A/B

Test platform: Android, iOS

Test Duration: 47 days on Android, and 15 days on iOS

Target population: Cx who land on the App using Guest Mode

Control/Treatment split: 50/50

# Timeline

The experiment data was measured between 10/04/2023 - 11/19/2023 on Android, and 11/14/2023 - 11/28/2023 on iOS

# Appendix

[Curie for iOS](https://admin-gateway.doordash.com/decision-systems/experiments/8144a140-79d1-4514-8f47-98a42fede3b4?analysisId=04b2043a-08e1-4e6f-bd96-a95f09eed49c)

[iOS MAU and GMV projection template](https://docs.google.com/spreadsheets/d/1nDNLaHRRvZ4pYAErJdhTb3mcF2KY9DD3izNnZ0MX6rg/edit?usp=sharing)

[Curie for Android](https://admin-gateway.doordash.com/decision-systems/experiments/4e49a5ef-34c4-4a7f-9464-a88c0a231492?analysisId=770cd842-b6df-41f6-a7a9-d65a6ba3e8cf)

[Android MAU and GMV projection template](https://docs.google.com/spreadsheets/d/1at1aw98QVkmXbFvYxEIRZ1bfs-eXjAWHJ0eN1tsIOZY/edit?usp=sharing)

[Mode for Android](https://app.mode.com/editor/doordash/reports/43a2b48b0cae/presentation)
