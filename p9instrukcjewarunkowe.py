light = input("jakie jest światło? (red, green, yellow) ")

# if light == 'red':
#     print("Czekaj!")
# elif light == 'yellow':
#     print("Przygotuj się!") 
# elif light == 'green':       
#     print("Jedz!")
# else:
#     print("Nie właściwa wartość mordeczko!")
# --------------------------------------------------------------------

# if str(light).startswith("r"):
#     print("Czekaj!")
# elif light == 'yellow':
#     print("Przygotuj się!") 
# elif light == 'green':       
#     print("Jedz!")
# else:
#     print("Nie właściwa wartość mordeczko!")
#---------------------------------------------------------------------
print("Jedź!") if light == 'green' else print("Czekaj!")