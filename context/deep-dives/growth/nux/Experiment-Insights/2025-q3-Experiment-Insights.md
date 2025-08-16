NUX Experiment Insights and Learnings

3 areas of learning

- Search

- DashPass

- Removing friction

**Search summary:**

- We launched 5 search experiments

  - <mark>[ios horizontal search pills](https://admin-gateway.doordash.com/decision-systems/experiments/f83288d8-491c-4979-b4ea-20ec01d74029?analysisId=b785b460-5dbb-43a8-b456-56bb38089d47)</mark>

  - <mark>[android horizontal search pills](https://admin-gateway.doordash.com/decision-systems/experiments/77600bd8-c293-4c96-823c-61b055e29d12?analysisId=40440cc8-f64d-44dd-acbc-8056e4ca3440)</mark>

  - <mark>[android cuisine filters](https://admin-gateway.doordash.com/decision-systems/experiments/9348cc3e-c48d-450d-bb10-971e98ca4cc9?analysisId=bbfca2f5-6c1c-4e7f-9b9b-7ff19458226d)</mark>

  - <mark>[ios cuisine filters](https://admin-gateway.doordash.com/decision-systems/experiments/70f6f7c4-6e14-4afc-bd24-2595b0317e7e?analysisId=4b21c26f-4c91-4cb5-8f41-e78cf8843ac7)</mark>

  - [cx_ios_search_bar_for_guests_in_home_page](https://admin-gateway.doordash.com/decision-systems/experiments/3d6cd2d1-d89f-41db-a3f8-fdfd59818e5f?analysisId=eaf170ee-bc00-4c18-a736-abd2bb2f4d77)

- TLDR: none of the search experiments were able to improve New Cx CVR or order rate because none of the experiments were able to increase search conversion.

  - Search Bar

    - Our hypothesis was that adding another entry point for search would dramatically increase usage because new users are more likely to search but it appears guests who wanted to search are having no issues finding it. Adding another entry point didn’t drastically change our metrics. We saw a slight increase in usage which was offset by a decrease in conversions (the new users were not high intent users, this could contribute to the increase in search null rate which we saw).

    - This experiment was rolled back.

  - Search Pills

    - Our hypothesis was that the pills were a better search experience causing more users to convert on search but it seems this isn’t the case (search conversions actually went down). Usage was also down. It’s possible users are finding the pills confusing to use.

    - This experiment was rolled back but we are iterating and reramping it soon.

  - Cuisine Filters

    - Our hypothesis was that the cuisine images in search were a better search experience causing more users to convert on search but it seems this isn’t the case (search conversions actually went down). There was an increase in cuisine filter usage but a decrease in other search forms (overall usage flat).

    - This experiment was rolled back.

- Next steps/learnings

  - We are re-launching search pills with only 5 pills instead of 10 (trying to make the UI simpler to see if this increases usage in conversion).

  - If this doesn’t work, our learning is that new users aren’t susceptible to search changes:

    - Possible those who do search are high enough intent that they would search regardless of making it more accessible or easy to use

    - Possible lower intent new users don’t have enough background to search successfully (the increase in null rate outlines this).

- [Search summary deep dive](https://docs.google.com/document/d/143sVLOavg9CedCS-nGHujHM-9qh4ESg-CGlnILTmTD0/edit)

**DashPass insights:**

- Two relevant DashPass experiments

  - [iOS price prominence](https://docs.google.com/document/d/1QhcatWoi8XcsVVo5iBfHOdCqKt3UhiXY-WLhtk3YaI8/edit)

    - Adding DashPass upsell in checkout did increase dp trial rate but didn’t increase new cx or order rate

    - Our hypothesis: by this point, users were already high intent, therefore adding DashPass didn’t incentivize them to convert any more. Also for new users, at this point they are already aware of $0 delivery fee for first order.

  - Current Location Browsing

    - This experiment had to remove the upsell banner after the address screen due to eng constraints while testing the current location feature.

    - We saw a decrease in DP metrics but also a decrease in Order Rate and New Cx.

    - Doing some rough sizing I saw:

      - For all Cx

        - The order rate for dp trial signups is 1.8 as compared to 1.3 for those who don't sign up for dp trials

        - The new cx rate for dp trial signups is 45% as compared to 5% for those who don’t sign up for dp trials

      - For new Cx

        - The order rate for dp trial signups is 1.7 as compared to .49 for those who don't sign up for dp trials

        - The new cx rate for dp trial signups is 90% as compared to 56% for those who don't sign up for dp trials.

          - *New cx are 60% more likely to convert if they sign up for a dp trial*

    - This experiment was rolled back to add back the dashpass upsell.

- Next steps/learnings

  - Serving the Dashpass upsell early in their order flow increases conversion because Cx sees a money-saving opportunity. Also once they purchase DashPass, they are much more likely to convert (they have already made a financial commitment)

**Adding more friction to increase stickiness vs. removing friction to align with Customer expectations:**

- Relevant Experiments

  - Sticky address banner

    - We tried to remove the blocking address modal and saw a drop in Order rate and New Cx. We then introduced it back in the form of a sticky modal and an improvement but still negative when compared to the blocking modal. We are now experimenting with bringing back the modal and keeping the sticky banner.

  - Android skip new user address confirmation

    - We tried removing the address confirmation screen and saw a drop in order rate and new cx.

    - This experiment was rolled back.

  - Android cx skip login

    - We defaulted non-logged in android users to guest mode with a signin bottom sheet and saw a drop in both order rate and new cx.

    - This experiment was rolled back.

  - [iOS Guest Cart Copy](https://docs.google.com/document/d/1uqN8wUu6EHVn0EQr8GYKHVKslBBu9Kj-_llPMrgoFiM/edit#heading=h.wa7bm2c0ccta)

    - We changed the “Signup to Checkout” text on the checkout button to “Continue”. We saw a lift in New Cx Conversion.

    - By indicating to users at cart that the next stage of the checkout process removed friction

  - [Android Guest Nearby Copy](https://docs.google.com/document/d/1i0et5h_4i_pzd3j3RiBpmFNYCfQ9K-6eBoIGrJz1ki0/edit#heading=h.wa7bm2c0ccta)

    - We changed the “Continue” text on the landing page to “Search Nearby”. We saw a lift in order rate.

    - This aligns closer with Cx expectations (of skipping friction), not avoiding login.

- Next steps/learnings

  - There are two types of friction in the new user flow: fiction that makes the users stickier and friction that causes confusion at what the next steps are.

    - Type 1: Removing friction that makes users stickier can actually lead to a decrease in conversion. The earlier in the process that users feel invested can give them higher intent.

      - We previously thought that getting users to view the explore page as soon as possible would increase conversion by showing them what the platform had to offer. Now we realize if the user has taken some sort of action before viewing the explore page (enter their address, purchasing DashPass etc.) they might be more likely to convert.

    - Type 2: Removing friction that causes confusion will increase conversion. Adding clarity about what the next steps are makes the user more likely to take that next step
