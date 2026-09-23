# Booking Lab Evidence Record

**Name:** Krittithee Kanjanapinchote
**Student ID:** 6580988
**Repository:** https://github.com/Krittithee-Kan/iccs471-booking-lab-Krittithee-Kan.git

## Goal
I make the rule to stop booking the same room in the same time avilable. The system need to reject the new booking if the time is overlapping and not save in the system.

## Constraints / Out of Scope
I change booking_app/booking.py and tests/test_booking.py. I'm not allow to change demo.py or change Git. For example the old rule like the name must not be blank.

## Key Decision and Agent Claim
In plan step, I check that the math logic is correct make sure it use < not <=. Because if it use <= then it would be a bug.

The agent say it test all new rules good and not break old rule. I look at tests/test_booking.py to see this. I see it have test for partial overlap, different room, and back-to-back time. So the claim is accurate.

## Verification: Claim → Evidence
- **Claim:** The app will say no to overlap in same room and keep old rules.
- **Command or test I ran:** uv run python -m unittest discover -s tests -v
- **Actual result:** The test run good. The test number is more than 4 test before, and all say OK with no error.
- **What this supports:** This mean the overlap code is work. It show ValueError when overlap and agent not delete old code when it writing new code.

## Manual Validation
When I run uv run python demo.py by myself, I see it is fix. Before, it say Overlapping booking in room A: accepted (BUG) and 4 booking. After I fix, it show overlap booking is reject. The number of save booking is correct now.

## Remaining Uncertainty
The code not think about two people use in same time. If it is real web, two person might click book at same time. Then the system might not catch it and save both. So the room have double book problem.