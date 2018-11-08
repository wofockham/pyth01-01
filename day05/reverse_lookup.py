state_capitals = {
  "Alaska" : "Juneau",
  "Colorado" : "Denver",
  "Oregon" : "Salem",
  "Texas" : "Austin"
  }

def reverse_lookup(capital):
    capitals_states = {}

    # Invert the hash (swap keys and values around)
    for state in state_capitals:
        current_capital = state_capitals[state]
        capitals_states[current_capital] = state

    return capitals_states[capital]

print(reverse_lookup("Denver"))
