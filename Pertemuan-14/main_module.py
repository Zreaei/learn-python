# Import item dari module
import module.my_module as mod

mod.greeting("Zamzami")

pet = mod.kucing["nama"]
print(pet)

# Import salah satu item dari module
from module.my_module import kucing as k

pet = k["nama"]
print(pet)