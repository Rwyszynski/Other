from enum import IntEnum

Event = IntEnum("Lista zakupów", ["Piwo", "Bułka", "Pep"])

print(list(Event))

Event.Bułka
