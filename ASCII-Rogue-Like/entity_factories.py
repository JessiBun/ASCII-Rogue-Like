from components.ai import HostileEnemy
from components.consumable import HealingConsumable, LightningDamageConsumable, ConfusionConsumable, FireballDamageConsumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Ted",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Gregi",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
)

confusion_scroll = Item(
    char="+",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="#",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=FireballDamageConsumable(damage=12, radius=3),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
)

lightening_scroll = Item(
    char="~",
    color=(0, 0, 0),
    name="Lightning Scroll",
    consumable=LightningDamageConsumable(damage=20, maximum_range=5),
)