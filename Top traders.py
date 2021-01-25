# The program which takes specific traders' list and figures out top three traders who gave maximum contribution to overall trade


def remove_duplicates(customers):
    """takes list and removes duplicates from it"""
    customer_names = []
    
    for customer_name in customers:
        no_of_occurance = customers.count(customer_name)

        # if no of occurance more than one it'll remove customer name 
        if no_of_occurance > 1:
            customers.remove(customer_name)

            # it appends customer name only if it's not present in list named customer_names
            if customer_name not in customer_names:
                customer_names.append(customer_name)
        else:
            customer_names.append(customer_name)
    return customer_names


def top_three_contributors(contribution_in_trades):
    """returns top three contributors"""
    # distributing customer names and contribution in separate lists
    customer_names = list(contribution_in_trades.keys())
    contribution = list(contribution_in_trades.values())
    top_contributors = []

    # looping three times for getting top three contributors
    for top_contributor_no in range(3):
        # finding max contribution and assigning its index 
        max_contributor_index = contribution.index(max(contribution))     

        # it appends customer name only if customer name not already present in top contributors
        if customer_names[max_contributor_index] not in top_contributors: 
            top_contributors.append(customer_names[max_contributor_index])
        
        # deleting items of top contributors to get rid of duplication
        contribution.__delitem__(max_contributor_index)
        customer_names.__delitem__(max_contributor_index)
    
    top_contributors.sort()
    return top_contributors


def mostActive(customers):
    """returns Most active customers' list who trades atleast 5% of total trade"""
    # figuring out unique names
    customer_names = remove_duplicates(customers.copy())
    # for customer name and their no of trades
    customer_trades = {}
    # for customer's contribution in trade (in percentage)
    contribution_in_trades = {}
    # figuring out total trades by length of customers who trades
    total_trades = len(customers)

    # looping through customer_names to store no of trades and percentage of contribution
    for customer_name in customer_names:
        no_of_trades = customers.count(customer_name)     # counting customer trades
        customer_trades[customer_name] = no_of_trades       # storing no of trades 
        contribution_in_trades[customer_name] = no_of_trades / total_trades     # storing contribution in trades (in percentage)
    
    # getting list of top contributors and returning to main
    top_contributors = top_three_contributors(contribution_in_trades)    
    return top_contributors
        

if __name__ == '__main__':
    no_of_customers = int(input("Total customers : "))

    customers = []
    # taking customers names from user and storing in list named customers
    for i in range(no_of_customers):
        customer_name = input()
        customers.append(customer_name)

    # gets list of most active customers and prints
    most_active_customers = mostActive(customers)
    print("\nMost active customers are as follows:")
    for i, most_active_customer in enumerate(most_active_customers, 1):
        print(i, most_active_customer.title())

