
def nth_highest_order(orders, n):
    # orders is a list of customer IDs
    order_counts = Counter(orders)
    sorted_counts = sorted(order_counts.items(), key=lambda x: x[1], reverse=True)
    
    if n <= len(sorted_counts):
        return sorted_counts[n-1]
    else:
        return None
