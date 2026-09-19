# Organic Customer Segmentation

An original customer-analytics project using **synthetic retail data** to connect segmentation with campaign decisions.

## Business question

Which customers are most likely to buy organic products, and how should a lifecycle team vary messaging by customer value and loyalty?

## Approach

- Generate 5,000 synthetic customer records
- Model age, income, loyalty tenure, annual spend, and email engagement
- Create an organic-purchase outcome from a transparent probability function
- Implement k-means clustering from scratch with NumPy
- Compare buyer rate, spend, and loyalty across four segments
- Produce a compact segment scorecard visual

## Run

```bash
pip install -r requirements.txt
python src/analysis.py
```

## Marketing use

The segment table helps choose different treatments: education for low-engagement customers, premium bundles for high-spend buyers, loyalty offers for long-tenure customers, and controlled tests for high-propensity audiences.

## Limits

All data and outcomes are synthetic. The project demonstrates method and communication, not claims about real consumers. Real activation would require consent, holdout testing, incrementality measurement, and bias review.
