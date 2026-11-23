# **Token Economics Budget Calculator**

## **1. Project Overview**

This project uses Python to calculate the cost of using AI models. It checks how many tokens are used and how much money is needed per day and month.

It also checks whether the expected usage is within the given limits and budget.

## **2. What It Calculates**

- Input tokens used per day.
- Output tokens used per day.
- Total tokens used per day.
- Daily AI cost.
- Monthly AI cost.
- Requests per minute (RPM).
- Tokens per minute (TPM).
- Checks whether the usage is within the budget.

## **3. Project Files**

- `budget.py` – Main Python program.
- `test_budget.py` – Checks whether the program works.
- `requirements_6ee100.txt` – Contains the required packages.

## **4. Installation**

Install the required packages using:

```
pip install -r requirements_6ee100.txt
```

## **5. Configuration**

Create a `.env` file and add these values:

```
REQUESTS_PER_DAY=1000
AVG_INPUT_TOKENS=1000
AVG_OUTPUT_TOKENS=500
PEAK_REQUESTS_PER_MINUTE=10
INPUT_PRICE_PER_MILLION=1.0
OUTPUT_PRICE_PER_MILLION=2.0
RPM_LIMIT=100
TPM_LIMIT=50000
MONTHLY_BUDGET_USD=100
DAILY_BUDGET_USD=5
SAFETY_MARGIN_PERCENT=20
```

## **6. Meaning of Settings**

- `REQUESTS_PER_DAY` – Number of questions asked per day.
- `AVG_INPUT_TOKENS` – Average tokens sent to AI.
- `AVG_OUTPUT_TOKENS` – Average tokens returned by AI.
- `PEAK_REQUESTS_PER_MINUTE` – Maximum requests in one minute.
- `INPUT_PRICE_PER_MILLION` – Cost of input tokens.
- `OUTPUT_PRICE_PER_MILLION` – Cost of output tokens.
- `RPM_LIMIT` – Maximum requests allowed per minute.
- `TPM_LIMIT` – Maximum tokens allowed per minute.
- `MONTHLY_BUDGET_USD` – Monthly spending limit.
- `DAILY_BUDGET_USD` – Daily spending limit.
- `SAFETY_MARGIN_PERCENT` – Extra amount added for safety.

## **7. How to Run**

Run the following command:

```
python budget.py
```

The program calculates the token usage and cost and displays the results.

## **8. Expected Output**

The program displays:

- Total input and output tokens.
- Daily cost.
- Monthly cost.
- Peak RPM and TPM.
- Budget checking results.

It checks four conditions:

1. RPM limit.
2. TPM limit.
3. Daily budget.
4. Monthly budget.

**PASS:** The usage is within the given limit.

**REVIEW:** The usage needs to be checked or changed.

If all four checks pass, it displays:

`WITHIN configured planning limits.`

Otherwise, it displays:

`REVISE assumptions, limits, or design before build.`

## **9. How It Works**

- Calculates the total tokens used per day.
- Finds the daily AI cost.
- Calculates the monthly cost using 30 days.
- Adds an extra safety margin.
- Checks whether the usage is within the limits.
- Shows an error if negative values are entered.

## **10. Testing**

Run this command to test the program:

```
python -m unittest test_budget.py
```

It checks whether the calculations are working correctly.

## **11. Conclusion**

This project helps us calculate the cost of using AI models. It shows daily and monthly expenses and checks whether the usage is within the given budget. It also helps us understand token usage and avoid spending more money than planned.
