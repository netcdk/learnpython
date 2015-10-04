"""
Cookie Clicker Simulator by CDK
Written on CodeSkulptor.org
"""

import simpleplot, math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(60)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return ("SUMMARY" + "\n" + "Total Cookies: " + str(self._total_cookies) + "\n" +
                "Current Cookies: " + str(self._current_cookies) + "\n" +
                "Current Time: " + str(self._current_time) + "\n" +
                "Current CPS: " + str(self._current_cps))
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_total_cookies(self):
        """
        Return total number of cookies 
        (not current number of cookies)
        
        Should return a float
        """
        return self._total_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if (cookies - self._current_cookies) > 0:
            return math.ceil((cookies - self._current_cookies) / self._current_cps)
        else:
            return 0.0
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._current_time += time
            self._current_cookies += (time * self._current_cps)
            self._total_cookies += (time * self._current_cps)
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name, cost, self._total_cookies))
    
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    # Create clone of build_info object
    build_info_clone = build_info.clone()
    
    # Create new ClickerState object
    clicker_state = ClickerState()
    
    # Loop for duration of simulation
    while clicker_state.get_time() <= duration:
        
        # Determine next item to purchase based on strategy
        item_to_purchase = strategy(clicker_state.get_cookies(),
                                    clicker_state.get_cps(),
                                    clicker_state.get_history(),
                                    (duration - clicker_state.get_time()),
                                    build_info_clone)
        
        # Break loop if no next item to purchase
        if item_to_purchase is None:
            break
        
        # Wait to purchase next item, and break if wait is longer than time remaining
        wait_time = clicker_state.time_until(build_info_clone.get_cost(item_to_purchase))
        if wait_time > (duration - clicker_state.get_time()):
            break
        clicker_state.wait(wait_time)
        
        # Purchase next item
        clicker_state.buy_item(item_to_purchase,
                               build_info_clone.get_cost(item_to_purchase),
                              build_info_clone.get_cps(item_to_purchase))
        
        # Update build info based on purchase
        build_info_clone.update_item(item_to_purchase)
    
    # Wait for remaining duration of simulation
    clicker_state.wait(duration - clicker_state.get_time())    
    
    return clicker_state

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cheapest_cost = float("inf")
    
    for item in build_info.build_items():
        item_cost = build_info.get_cost(item)
        if (item_cost < cheapest_cost) and (item_cost <= (cookies + (time_left * cps))):
            cheapest_cost = item_cost
            item_to_purchase = item
    
    if cheapest_cost == float("inf"):
        return None
    else:
        return item_to_purchase

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    highest_cost = 0.0
        
    for item in build_info.build_items():
        item_cost = build_info.get_cost(item)
        if (item_cost > highest_cost) and (item_cost <= (cookies + (time_left * cps))):
            highest_cost = item_cost
            item_to_purchase = item
    
    if highest_cost == 0.0:
        return None
    else:
        return item_to_purchase

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    items = []
    expected_values = []
        
    if (cookies < 855):
        return (strategy_cheap(cookies, cps, history, time_left, build_info))
    
    else:
        for item in build_info.build_items():
            items.append(item)
            expected_values.append(build_info.get_cps(item) / build_info.get_cost(item))
        if len(items) > 0:
            return items[expected_values.index(max(expected_values))]
        else:
            return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
