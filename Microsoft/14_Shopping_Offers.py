class Solution:
    def shoppingOffers(self, price, special, needs):

        #   Calculating the cost without special offers
        def direct_cost(needs):
            return sum(needs[i] * price[i] for i in range(len(needs)))

        # DFS function with memoization
        def dfs(needs):

            # Check if the result for the current needs is already computed
            needs_tuple = tuple(needs)
            if needs_tuple in memo:
                return memo[needs_tuple]

            # Calculate the cost without any special offers
            min_cost = direct_cost(needs)

            # Try each special offer
            for offer in special:
                new_needs = needs[:]
                valid_offer = True

                # Check if the special offer can be applied
                for i in range(len(needs)):
                    if new_needs[i] < offer[i]:
                        valid_offer = False
                        break
                    new_needs[i] -= offer[i]

                # If the offer is valid, calculate the cost with it
                if valid_offer:
                    min_cost = min(min_cost, offer[-1] + dfs(new_needs))

            # Store the results in the memo and the dictionary
            memo[needs_tuple] = min_cost
            return min_cost

        # Memoization dictionary
        memo = {}
        return dfs(needs)
