import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=['Stock', 'Shares', 'Purchase Price', 'Current Price'])
    
    def add_stock(self, stock, shares, purchase_price):
        new_entry = pd.DataFrame({'Stock': [stock], 'Shares': [shares], 'Purchase Price': [purchase_price], 'Current Price': [0]})
        self.portfolio = pd.concat([self.portfolio, new_entry], ignore_index=True)
    
    def update_current_price(self, stock, current_price):
        if stock in self.portfolio['Stock'].values:
            self.portfolio.loc[self.portfolio['Stock'] == stock, 'Current Price'] = current_price
        else:
            print(f"Stock {stock} not found in portfolio.")
    
    def calculate_performance(self):
        self.portfolio['Gains/Losses'] = (self.portfolio['Current Price'] - self.portfolio['Purchase Price']) * self.portfolio['Shares']
        total_investment = (self.portfolio['Purchase Price'] * self.portfolio['Shares']).sum()
        total_value = (self.portfolio['Current Price'] * self.portfolio['Shares']).sum()
        total_gains = total_value - total_investment
        return total_investment, total_value, total_gains

    def display_portfolio(self):
        print(self.portfolio)
        total_investment, total_value, total_gains = self.calculate_performance()
        print(f"\nTotal Investment: ${total_investment:.2f}")
        print(f"Total Value: ${total_value:.2f}")
        print(f"Total Gains/Losses: ${total_gains:.2f}")

if __name__ == "__main__":
    tracker = StockPortfolio()
    
    # Example usage
    tracker.add_stock('AAPL', 10, 150)  # Adding Apple Stock
    tracker.add_stock('TSLA', 5, 700)   # Adding Tesla Stock
    
    # Updating current prices
    tracker.update_current_price('AAPL', 170)  # Apple is now $170
    tracker.update_current_price('TSLA', 800)  # Tesla is now $800

    # Displaying current portfolio performance
    tracker.display_portfolio()