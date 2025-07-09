
import pandas as pd

# Sample data
data = {
    'customer_id': [1, 2, 1, 3, 2, 2, 4, 1, 3, 4, 4, 4],
    'order_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
}
df = pd.DataFrame(data)

# Set the desired rank
n = 2

# Count number of orders per customer
order_counts = df.groupby('customer_id').size().reset_index(name='order_count')

# Rank customers by order count in descending order
order_counts['rank'] = order_counts['order_count'].rank(method='dense', ascending=False)

# Filter to get the nth highest number of orders
nth_highest_orders = order_counts[order_counts['rank'] == n]

print(nth_highest_orders)
