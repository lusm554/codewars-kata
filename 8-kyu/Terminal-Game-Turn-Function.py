# https://www.codewars.com/kata/56019d3b2c39ccde76000086/train/python

def do_turn():
    for func in ["roll_dice", "move", "combat", "get_coins", "buy_health", "print_status"]:
        eval(f"{func}()")
        
