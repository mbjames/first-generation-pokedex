class Pokemon:
    def __init__(self):
        self.number = ""
        self.name = ""
        self.category = ""
        self.type = []
        self.abilities = []
        self.moves = []

    def print(self):
        print("\n Number:", self.number)
        print(" Name:", self.name)
        print(" Category:", self.category)

        for x in self.type:
            print("_Type:", x)

        for x in self.abilities:
            print("_Ability:", x)

        for x in self.moves:
            print("_Move:", x)


bulbasaur = Pokemon()
bulbasaur.number = "001"
bulbasaur.name = "Bulbasaur"
bulbasaur.category = "Seed Pokemon"
bulbasaur.type = ["Grass", "Poison"]
bulbasaur.abilities = ["Overgrow", "Chlorophyll (Hidden)"]
bulbasaur.moves = ["Growl", "Tackle", "Leech Seed", "Vine Whip"]

ivysaur = Pokemon()
ivysaur.number = "002"
ivysaur.name = "Ivysaur"
ivysaur.category = "Seed Pokemon"
ivysaur.type = ["Grass", "Poison"]
ivysaur.abilities = ["Overgrow", "Chlorophyll (Hidden)"]
ivysaur.moves = ["Vine Whip", "Poison Powder", "Razor Leaf", "Growth"]

venusaur = Pokemon()
venusaur.number = "003"
venusaur.name = "Venusaur"
venusaur.category = "Seed Pokemon"
venusaur.type = ["Grass", "Poison"]
venusaur.abilities = ["Overgrow", "Chlorophyll (Hidden)"]
venusaur.moves = ["Petal Blizzard", "Petal Dance", "Take Down", "Solar Beam"]

charmander = Pokemon()
charmander.number = "004"
charmander.name = "Charmander"
charmander.category = "Lizard Pokemon"
charmander.type = ["Fire"]
charmander.abilities = ["Blaze", "Solar Power (Hidden)"]
charmander.moves = ["Scratch", "Growl", "Ember", "Smokescreen"]

charmeleon = Pokemon()
charmeleon.number = "005"
charmeleon.name = "Charmeleon"
charmeleon.category = "Flame Pokemon"
charmeleon.type = ["Fire"]
charmeleon.abilities = ["Blaze", "Solar Power (Hidden)"]
charmeleon.moves = ["Ember", "Smokescreen", "Fire Fang", "Dragon Breath"]

charizard = Pokemon()
charizard.number = "006"
charizard.name = "Charizard"
charizard.category = "Flame Pokemon"
charizard.type = ["Fire", "Flying"]
charizard.abilities = ["Blaze", "Solar Power (Hidden)"]
charizard.moves = ["Air Slash", "Dragon Claw", "Heat Wave", "Fire Spin"]

squirtle = Pokemon()
squirtle.number = "007"
squirtle.name = "Squirtle"
squirtle.category = "Tiny Turtle Pokemon"
squirtle.type = ["Water"]
squirtle.abilities = ["Torrent", "Rain Dish (Hidden)"]
squirtle.moves = ["Tackle", "Tail Whip", "Water Gun", "Bite"]

wartortle = Pokemon()
wartortle.number = "008"
wartortle.name = "Wartortle"
wartortle.category = "Turtle Pokemon"
wartortle.type = ["Water"]
wartortle.abilities = ["Torrent", "Rain Dish (Hidden)"]
wartortle.moves = ["Bite", "Water Pulse", "Protect", "Rain Dance"]

blastoise = Pokemon()
blastoise.number = "009"
blastoise.name = "Blastoise"
blastoise.category = "Shellfish Pokemon"
blastoise.type = ["Water"]
blastoise.abilities = ["Torrent", "Rain Dish (Hidden)"]
blastoise.moves = ["Flash Cannon", "Hydro Pump", "Skull Bash", "Protect"]

caterpie = Pokemon()
caterpie.number = "010"
caterpie.name = "Caterpie"
caterpie.category = "Worm Pokemon"
caterpie.type = ["Bug"]
caterpie.abilities = ["Shield Dust", "Run Away (Hidden)"]
caterpie.moves = ["Tackle", "String Shot", "Bug Bite", "Electroweb"]

metapod = Pokemon()
metapod.number = "011"
metapod.name = "Metapod"
metapod.category = "Cocoon Pokemon"
metapod.type = ["Bug"]
metapod.abilities = ["Shed Skin"]
metapod.moves = ["Harden", "Tackle", "Electroweb", "Iron Defense"]

butterfree = Pokemon()
butterfree.number = "012"
butterfree.name = "Butterfree"
butterfree.category = "Butterfly Pokemon"
butterfree.type = ["Bug", "Flying"]
butterfree.abilities = ["Compound Eyes", "Tinted Lens (Hidden)"]
butterfree.moves = ["Gust", "Confusion", "Sleep Powder", "Psybeam"]

weedle = Pokemon()
weedle.number = "013"
weedle.name = "Weedle"
weedle.category = "Hairy Bug Pokemon"
weedle.type = ["Bug", "Poison"]
weedle.abilities = ["Shield Dust", "Run Away (Hidden)"]
weedle.moves = ["Poison Sting", "String Shot", "Bug Bite", "Electroweb"]

kakuna = Pokemon()
kakuna.number = "014"
kakuna.name = "Kakuna"
kakuna.category = "Cocoon Pokemon"
kakuna.type = ["Bug", "Poison"]
kakuna.abilities = ["Shed Skin"]
kakuna.moves = ["Bug Bite", "Electroweb", "Iron Defense", "Poison Sting"]

beedrill = Pokemon()
beedrill.number = '015'
beedrill.name = "Beedrill"
beedrill.category = "Poison Bee Pokemon"
beedrill.type = ["Bug", "Poison"]
beedrill.abilities = ["Swarm", "Sniper (Hidden)"]
beedrill.moves = ["Fury Attack", "Focus Energy", "Twineedle", "Rage"]

pidgey = Pokemon()
pidgey.number = '016'
pidgey.name = "Pidgey"
pidgey.category = "Tiny Bird Pokemon"
pidgey.type = ["Normal", "Flying"]
pidgey.abilities = ["Keen Eye", "Tangled Feet", "Big Pecks (Hidden)"]
pidgey.moves = ["Tackle", "Sand Attack", "Gust", "Quick Attack"]

pidgeotto = Pokemon()
pidgeotto.number = "017"
pidgeotto.name = "Pidgeotto"
pidgeotto.category = "Bird Pokemon"
pidgeotto.type = ["Normal", "Flying"]
pidgeotto.abilities = ["Keen Eye", "Tangled Feet", "Big Pecks (Hidden)"]
pidgeotto.moves = ["Gust", "Quick Attack", "Whirlwind", "Wing Attack"]

pidgeot = Pokemon()
pidgeot.number = "018"
pidgeot.name = "Pidgeot"
pidgeot.category = "Bird Pokemon"
pidgeot.type = ["Normal", "Flying"]
pidgeot.abilities = ["Keen Eye", "Tangled Feet", "Big Pecks (Hidden)"]
pidgeot.moves = ["Hurricane", "Quick Attack", "Roost", "Air Slash"]

rattata = Pokemon()
rattata.number = "019"
rattata.name = "Rattata"
rattata.category = "Mouse Pokemon"
rattata.type = ["Normal"]
rattata.abilities = ["Run Away", "Guts", "Hustle (Hidden)"]
rattata.moves = ["Tackle", "Tail Whip", "Quick Attack", "Focus Energy"]

raticate = Pokemon()
raticate.number = "020"
raticate.name = "Raticate"
raticate.category = "Mouse Pokemon"
raticate.type = ["Normal"]
raticate.abilities = ["Run Away", "Guts", "Hustle (Hidden)"]
raticate.moves = ["Quick Attack", "Bite", "Hyper Fang", "Super Fang"]

spearow = Pokemon()
spearow.number = "021"
spearow.name = "Spearow"
spearow.category = "Tiny Bird Pokemon"
spearow.type = ["Normal", "Flying"]
spearow.abilities = ["Keen Eye", "Sniper (Hidden)"]
spearow.moves = ["Peck", "Growl", "Leer", "Fury Attack"]

fearow = Pokemon()
fearow.number = "022"
fearow.name = "Fearow"
fearow.category = "Beak Pokemon"
fearow.type = ["Normal", "Flying"]
fearow.abilities = ["Keen Eye", "Sniper (Hidden)"]
fearow.moves = ["Drill Peck", "Fury Attack", "Aerial Ace", "Mirror Move"]

ekans = Pokemon()
ekans.number = "023"
ekans.name = "Ekans"
ekans.category = "Snake Pokemon"
ekans.type = ["Poison"]
ekans.abilities = ["Intimidate", "Shed Skin", "Unnerve (Hidden)"]
ekans.moves = ["Wrap", "Leer", "Poison Sting", "Bite"]

arbok = Pokemon()
arbok.number = "024"
arbok.name = "Arbok"
arbok.category = "Cobra Pokemon"
arbok.type = ["Poison"]
arbok.abilities = ["Intimidate", "Shed Skin", "Unnerve (Hidden)"]
arbok.moves = ["Crunch", "Acid", "Glare", "Wrap"]

pikachu = Pokemon()
pikachu.number = "025"
pikachu.name = "Pikachu"
pikachu.category = "Mouse Pokemon"
pikachu.type = ["Electric"]
pikachu.abilities = ["Static", "Lightning Rod (Hidden)"]
pikachu.moves = ["Quick Attack", "Nuzzle", "Thunder Shock", "Thunderbolt"]

raichu = Pokemon()
raichu.number = "026"
raichu.name = "Raichu"
raichu.category = "Mouse Pokemon"
raichu.type = ["Electric"]
raichu.abilities = ["Static", "Lightning Rod (Hidden)"]
raichu.moves = ["Thunder Punch", "Electro Ball", "Discharge", "Slam"]

sandshrew = Pokemon()
sandshrew.number = "027"
sandshrew.name = "Sandshrew"
sandshrew.category = "Mouse Pokemon"
sandshrew.type = ["Ground"]
sandshrew.abilities = ["Sand Veil", "Sand Rush (Hidden)"]
sandshrew.moves = ["Scratch", "Defense Curl", "Poison Sting", "Sand Attack"]

sandslash = Pokemon()
sandslash.number = "028"
sandslash.name = "Sandslash"
sandslash.category = "Mouse Pokemon"
sandslash.type = ["Ground"]
sandslash.abilities = ["Sand Veil", "Sand Rush (Hidden)"]
sandslash.moves = ["Dig", "Bulldoze", "Fury Swipes", "Slash"]

nidoran_female = Pokemon()
nidoran_female.number = "029"
nidoran_female.name = "Nidoran♀"
nidoran_female.category = "Poison Pin Pokemon"
nidoran_female.type = ["Poison"]
nidoran_female.abilities = ["Poison Point", "Rivalry", "Hustle (Hidden)"]
nidoran_female.moves = ["Growl", "Poison Sting", "Scratch", "Tail Whip"]

nidorina = Pokemon()
nidorina.number = "030"
nidorina.name = "Nidorina"
nidorina.category = "Poison Pin Pokemon"
nidorina.type = ["Poison"]
nidorina.abilities = ["Poison Point", "Rivalry", "Hustle (Hidden)"]
nidorina.moves = ["Bite", "Double Kick", "Crunch", "Toxic"]

nidoqueen = Pokemon()
nidoqueen.number = "031"
nidoqueen.name = "Nidoqueen"
nidoqueen.category = "Drill Pokemon"
nidoqueen.type = ["Poison", "Ground"]
nidoqueen.abilities = ["Poison Point", "Rivalry", "Sheer Force (Hidden)"]
nidoqueen.moves = ["Superpower", "Toxic", "Earth Power", "Double Kick"]

nidoran_male = Pokemon()
nidoran_male.number = "032"
nidoran_male.name = "Nidoran♂"
nidoran_male.category = "Poison Pin Pokemon"
nidoran_male.type = ["Poison"]
nidoran_male.abilities = ["Poison Point", "Rivalry", "Hustle (Hidden)"]
nidoran_male.moves = ["Leer", "Poison Sting", "Peck", "Focus Energy"]

nidorino = Pokemon()
nidorino.number = "033"
nidorino.name = "Nidorino"
nidorino.category = "Poison Pin Pokemon"
nidorino.type = ["Poison"]
nidorino.abilities = ["Poison Point", "Rivalry", "Hustle (Hidden)"]
nidorino.moves = ["Fury Attack", "Toxic Spikes", "Double Kick", "Horn Attack"]

nidoking = Pokemon()
nidoking.number = "034"
nidoking.name = "Nidoking"
nidoking.category = "Drill Pokemon"
nidoking.type = ["Poison", "Ground"]
nidoking.abilities = ["Poison Point", "Rivalry", "Sheer Force (Hidden)"]
nidoking.moves = ["Megahorn", "Horn Attack", "Poison Jab", "Earth Power"]

clefairy = Pokemon()
clefairy.number = "035"
clefairy.name = "Clefairy"
clefairy.category = "Fairy Pokemon"
clefairy.type = ["Fairy"]
clefairy.abilities = ["Cute Charm", "Magic Guard", "Friend Guard (Hidden)"]
clefairy.moves = ["Pound", "Growl", "Defense Curl", "Sing"]

clefable = Pokemon()
clefable.number = "036"
clefable.name = "Clefable"
clefable.category = "Fairy Pokemon"
clefable.type = ["Fairy"]
clefable.abilities = ["Cute Charm", "Magic Guard", "Unaware (Hidden)"]
clefable.moves = ["Moonblast", "Healing Wish", "Sing", "Life Dew"]

vulpix = Pokemon()
vulpix.number = "037"
vulpix.name = "Vulpix"
vulpix.category = "Fox Pokemon"
vulpix.type = ["Fire"]
vulpix.abilities = ["Flash Fire", "Drought (Hidden)"]
vulpix.moves = ["Ember", "Tail Whip", "Disable", "Quick Attack"]

ninetales = Pokemon()
ninetales.number = "038"
ninetales.name = "Ninetales"
ninetales.category = "Fox Pokemon"
ninetales.type = ["Fire"]
ninetales.abilities = ["Flash Fire", "Drought (Hidden)"]
ninetales.moves = ["Will-O-Wisp", "Flamethrower", "Fire Spin", "Quick Attack"]

jigglypuff = Pokemon()
jigglypuff.number = "039"
jigglypuff.name = "Jigglypuff"
jigglypuff.category = "Balloon Pokemon"
jigglypuff.type = ["Normal", "Fairy"]
jigglypuff.abilities = ["Cute Charm", "Competitive", "Friend Guard (Hidden)"]
jigglypuff.moves = ["Disable", "Charm", "Sing", "Pound"]

wigglytuff = Pokemon()
wigglytuff.number = "040"
wigglytuff.name = "Wigglytuff"
wigglytuff.category = "Balloon Pokemon"
wigglytuff.type = ["Normal", "Fairy"]
wigglytuff.abilities = ["Cute Charm", "Competitive", "Frisk (Hidden)"]
wigglytuff.moves = ["Sweet Kiss", "Disarming Voice", "Disable", "Charm"]

zubat = Pokemon()
zubat.number = "041"
zubat.name = "Zubat"
zubat.category = "Bat Pokemon"
zubat.type = ["Poison", "Flying"]
zubat.abilities = ["Inner Focus", "Infiltrator (Hidden)"]
zubat.moves = ["Absorb", "Supersonic", "Astonish", "Mean Look"]

golbat = Pokemon()
golbat.number = "042"
golbat.name = "Golbat"
golbat.category = "Bat Pokemon"
golbat.type = ["Poison", "Flying"]
golbat.abilities = ["Inner Focus", "Infiltrator (Hidden)"]
golbat.moves = ["Bite", "Confuse Ray", "Air Slash", "Leech Life"]

oddish = Pokemon()
oddish.number = "043"
oddish.name = "Oddish"
oddish.category = "Weed Pokemon"
oddish.type = ["Grass", "Poison"]
oddish.abilities = ["Chlorophyll", "Run Away (Hidden)"]
oddish.moves = ["Absorb", "Growth", "Acid", "Sweet Scent"]

gloom = Pokemon()
gloom.number = "044"
gloom.name = "Gloom"
gloom.category = "Weed Pokemon"
gloom.type = ["Grass", "Poison"]
gloom.abilities = ["Chlorophyll", "Stench (Hidden)"]
gloom.moves = ["Acid", "Sleep Powder", "Giga Drain", "Petal Dance"]

vileplume = Pokemon()
vileplume.number = "045"
vileplume.name = "Vileplume"
vileplume.category = "Flower Pokemon"
vileplume.type = ["Grass", "Poison"]
vileplume.abilities = ["Chlorophyll", "Effect Spore (Hidden)"]
vileplume.moves = ["Petal Blizzard", "Aromatherapy", "Mega Drain", "Poison Powder"]

paras = Pokemon()
paras.number = "046"
paras.name = "Paras"
paras.category = "Mushroom Pokemon"
paras.type = ["Bug", "Grass"]
paras.abilities = ["Effect Spore", "Dry Skin", "Damp (Hidden)"]
paras.moves = ["Scratch", "Stun Spore", "Poison Powder", "Absorb"]

parasect = Pokemon()
parasect.number = "047"
parasect.name = "Parasect"
parasect.category = "Mushroom Pokemon"
parasect.type = ["Bug", "Grass"]
parasect.abilities = ["Effect Spore", "Dry Skin", "Damp (Hidden)"]
parasect.moves = ["Cross Poison", "Slash", "Scratch", "Fury Cutter"]

venonat = Pokemon()
venonat.number = "048"
venonat.name = "Venonat"
venonat.category = "Insect Pokemon"
venonat.type = ["Bug", "Poison"]
venonat.abilities = ["Compound Eyes", "Tinted Lens", "Run Away (Hidden)"]
venonat.moves = ["Tackle", "Disable", "Supersonic", "Confusion"]

venomoth = Pokemon()
venomoth.number = "049"
venomoth.name = "Venomoth"
venomoth.category = "Poison Moth Pokemon"
venomoth.type = ["Bug", "Poison"]
venomoth.abilities = ["Shield Dust", "Tinted Lens", "Wonder Skin (Hidden)"]
venomoth.moves = ["Quiver Dance", "Sleep Powder", "Bug Buzz", "Sludge Bomb"]

diglett = Pokemon()
diglett.number = "050"
diglett.name = "Diglett"
diglett.category = "Mole Pokemon"
diglett.type = ["Ground"]
diglett.abilities = ["Sand Veil", "Arena Trap", "Sand Force (Hidden)"]
diglett.moves = ["Sand Attack", "Scratch", "Growl", "Mud-Slap"]

dugtrio = Pokemon()
dugtrio.number = "051"
dugtrio.name = "Dugtrio"
dugtrio.category = "Mole Pokemon"
dugtrio.type = ["Ground"]
dugtrio.abilities = ["Sand Veil", "Arena Trap", "Sand Force (Hidden)"]
dugtrio.moves = ["Sand Tomb", "Sucker Punch", "Tri Attack", "Bulldoze"]

meowth = Pokemon()
meowth.number = "052"
meowth.name = "Meowth"
meowth.category = "Scratch Cat Pokemon"
meowth.type = ["Normal"]
meowth.abilities = ["Pickup", "Technician", "Unnerve (Hidden)"]
meowth.moves = ["Fake Out", "Growl", "Feint", "Scratch"]

persian = Pokemon()
persian.number = "053"
persian.name = "Persian"
persian.category = "Classy Cat Pokemon"
persian.type = ["Normal"]
persian.abilities = ["Limber", "Technician", "Unnerve"]
persian.moves = ["Power Gem", "Fake Out", "Pay Day", "Taunt"]

psyduck = Pokemon()
psyduck.number = "054"
psyduck.name = "Psyduck"
psyduck.category = "Duck Pokemon"
psyduck.type = ["Water"]
psyduck.abilities = ["Damp", "Cloud Nine", "Swift Swim (Hidden)"]
psyduck.moves = ["Scratch", "Tail Whip", "Water Gun", "Confusion"]

golduck = Pokemon()
golduck.number = "055"
golduck.name = "Golduck"
golduck.category = "Duck Pokemon"
golduck.type = ["Water"]
golduck.abilities = ["Damp", "Cloud Nine", "Swift Swim (Hidden)"]
golduck.moves = ["Aqua Jet", "Confusion", "Aqua Tail", "Hydro Pump"]

mankey = Pokemon()
mankey.number = "056"
mankey.name = "Mankey"
mankey.category = "Pig Monkey Pokemon"
mankey.type = ["Fighting"]
mankey.abilities = ["Vital Spirit", "Anger Point", "Defiant (Hidden)"]
mankey.moves = ["Scratch", "Low Kick", "Focus Energy", "Karate Chop"]

primeape = Pokemon()
primeape.number = "057"
primeape.name = "Primeape"
primeape.category = "Pig Monkey Pokemon"
primeape.type = ["Fighting"]
primeape.abilities = ["Vital Spirit", "Anger Point", "Defiant (Hidden)"]
primeape.moves = ["Rage", "Low Kick", "Karate Chop", "Seismic Toss"]

growlithe = Pokemon()
growlithe.number = "058"
growlithe.name = "Growlithe"
growlithe.category = "Puppy Pokemon"
growlithe.type = ["Fire"]
growlithe.abilities = ["Intimidate", "Flash Fire", "Justified (Hidden)"]
growlithe.moves = ["Ember", "Leer", "Howl", "Bite"]

arcanine = Pokemon()
arcanine.number = "059"
arcanine.name = "Arcanine"
arcanine.category = "Legendary Pokemon"
arcanine.type = ["Fire"]
arcanine.abilities = ["Intimidate", "Flash Fire", "Justified (Hidden)"]
arcanine.moves = ["Extreme Speed", "Crunch", "Fire Fang", "Flame Wheel"]

poliwag = Pokemon()
poliwag.number = "060"
poliwag.name = "Poliwag"
poliwag.category = "Tadpole Pokemon"
poliwag.type = ["Water"]
poliwag.abilities = ["Water Absorb", "Damp", "Swift Swim (Hidden)"]
poliwag.moves = ["Water Gun", "Hypnosis", "Pound", "Mud Shot"]

poliwhirl = Pokemon()
poliwhirl.number = "061"
poliwhirl.name = "Poliwhirl"
poliwhirl.category = "Tadpole Pokemon"
poliwhirl.type = ["Water"]
poliwhirl.abilities = ["Water Absorb", "Damp", "Swift Swim (Hidden)"]
poliwhirl.moves = ["Water Gun", "Hypnosis", "Bubble Beam", "Body Slam"]

poliwrath = Pokemon()
poliwrath.number = "062"
poliwrath.name = "Poliwrath"
poliwrath.category = "Tadpole Pokemon"
poliwrath.type = ["Water", "Fighting"]
poliwrath.abilities = ["Water Absorb", "Damp", "Swift Swim (Hidden)"]
poliwrath.moves = ["Submission", "Dynamic Punch", "Bubble Beam", "Body Slam"]

abra = Pokemon()
abra.number = "063"
abra.name = "Abra"
abra.category = "Psi Pokemon"
abra.type = ["Psychic"]
abra.abilities = ["Synchronize", "Inner Focus", "Magic Guard (Hidden)"]
abra.moves = ["Teleport", "Light Screen", "Reflect", "Protect"]

kadabra = Pokemon()
kadabra.number = "064"
kadabra.name = "Kadabra"
kadabra.category = "Psi Pokemon"
kadabra.type = ["Psychic"]
kadabra.abilities = ["Synchronize", "Inner Focus", "Magic Guard (Hidden)"]
kadabra.moves = ["Confusion", "Disable", "Teleport", "Psybeam"]

alakazam = Pokemon()
alakazam.number = "065"
alakazam.name = "Alakazam"
alakazam.category = "Psi Pokemon"
alakazam.type = ["Psychic"]
alakazam.abilities = ["Synchronize", "Inner Focus", "Magic Guard (Hidden)"]
alakazam.moves = ["Psybeam", "Recover", "Psychic", "Clam Mind"]

machop = Pokemon()
machop.number = "066"
machop.name = "Machop"
machop.category = "Superpower Pokemon"
machop.type = ["Fighting"]
machop.abilities = ["Guts", "No Guard", "Steadfast (Hidden)"]
machop.moves = ["Low Kick", "Leer", "Focus Energy", "Revenge"]

machoke = Pokemon()
machoke.number = "067"
machoke.name = "Machoke"
machoke.category = "Superpower Pokemon"
machoke.type = ["Fighting"]
machoke.abilities = ["Guts", "No Guard", "Steadfast (Hidden)"]
machoke.moves = ["Strength", "Seismic Toss", "Dynamic Punch", "Bulk Up"]

machamp = Pokemon()
machamp.number = "068"
machamp.name = "Machamp"
machamp.category = "Superpower Pokemon"
machamp.type = ["Fighting"]
machamp.abilities = ["Guts", "No Guard", "Steadfast (Hidden)"]
machamp.moves = ["Dynamic Punch", "Bulk Up", "Cross Chop", "Knock Off"]

bellsprout = Pokemon()
bellsprout.number = "069"
bellsprout.name = "Bellsprout"
bellsprout.category = "Flower Pokemon"
bellsprout.type = ["Grass", "Poison"]
bellsprout.abilities = ["Chlorophyll", "Gluttony (Hidden)"]
bellsprout.moves = ["Vine Whip", "Growth", "Wrap", "Sleep Powder"]

weepinbell = Pokemon()
weepinbell.number = "070"
weepinbell.name = "Weepinbell"
weepinbell.category = "Flycatcher Pokemon"
weepinbell.type = ["Grass", "Poison"]
weepinbell.abilities = ["Chlorophyll", "Gluttony (Hidden)"]
weepinbell.moves = ["Acid", "Razor Leaf", "Poison Jab", "Growth"]

victreebel = Pokemon()
victreebel.number = "071"
victreebel.name = "Victreebel"
victreebel.category = "Flycatcher Pokemon"
victreebel.type = ["Grass", "Poison"]
victreebel.abilities = ["Chlorophyll", "Gluttony (Hidden)"]
victreebel.moves = ["Leaf Tornado", "Razor Leaf", "Leaf Storm", "Sleep Powder"]

tentacool = Pokemon()
tentacool.number = "072"
tentacool.name = "Tentacool"
tentacool.category = "Jellyfish Pokemon"
tentacool.type = ["Water", "Poison"]
tentacool.abilities = ["Clear Body", "Liquid Ooze", "Rain Dish (Hidden)"]
tentacool.moves = ["Poison Sting", "Water Gun", "Acid", "Wrap"]

tentacruel = Pokemon()
tentacruel.number = "073"
tentacruel.name = "Tentacruel"
tentacruel.category = "Jellyfish Pokemon"
tentacruel.type = ["Water", "Poison"]
tentacruel.abilities = ["Clear Body", "Liquid Ooze", "Rain Dish (Hidden)"]
tentacruel.moves = ["Supersonic", "Screech", "Water Pulse", "Sludge Wave"]

geodude = Pokemon()
geodude.number = "074"
geodude.name = "Geodude"
geodude.category = "Rock Pokemon"
geodude.type = ["Rock", "Ground"]
geodude.abilities = ["Rock Head", "Sturdy", "Sand Veil (Hidden)"]
geodude.moves = ["Tackle", "Defense Curl", "Mud Sport", "Rock Polish"]

graveler = Pokemon()
graveler.number = "075"
graveler.name = "Graveler"
graveler.category = "Rock Pokemon"
graveler.type = ["Rock", "Ground"]
graveler.abilities = ["Rock Head", "Sturdy", "Sand Veil (Hidden)"]
graveler.moves = ["Rollout", "Magnitude", "Rock Throw", "Bulldoze"]

golem = Pokemon()
golem.number = "076"
golem.name = "Golem"
golem.category = "Megaton Pokemon"
golem.type = ["Rock", "Ground"]
golem.abilities = ["Rock Head", "Sturdy", "Sand Veil (Hidden)"]
golem.moves = ["Heavy Slam", "Magnitude", "Earthquake", "Explosion"]

ponyta = Pokemon()
ponyta.number = "077"
ponyta.name = "Ponyta"
ponyta.category = "Fire Horse Pokemon"
ponyta.type = ["Fire"]
ponyta.abilities = ["Run Away", "Flash Fire", "Flame Body (Hidden)"]
ponyta.moves = ["Tackle", "Growl", "Tail Whip", "Ember"]

rapidash = Pokemon()
rapidash.number = "078"
rapidash.name = "Rapidash"
rapidash.category = "Fire Horse Pokemon"
rapidash.type = ["Fire"]
rapidash.abilities = ["Run Away", "Flash Fire", "Flame Body (Hidden)"]
rapidash.moves = ["Megahorn", "Poison Jab", "Flame Charge", "Fire Blast"]

slowpoke = Pokemon()
slowpoke.number = "079"
slowpoke.name = "Slowpoke"
slowpoke.category = "Dopey Pokemon"
slowpoke.type = ["Water", "Psychic"]
slowpoke.abilities = ["Oblivious", "Own Tempo", "Regenerator (Hidden)"]
slowpoke.moves = ["Tackle", "Curse", "Growl", "Water Gun"]

slowbro = Pokemon()
slowbro.number = "080"
slowbro.name = "Slowbro"
slowbro.category = "Hermit Crab Pokemon"
slowbro.type = ["Water", "Psychic"]
slowbro.abilities = ["Oblivious", "Own Tempo", "Regenerator (Hidden)"]
slowbro.moves = ["Confusion", "Yawn", "Surf", "Psychic"]

magnemite = Pokemon()
magnemite.number = "081"
magnemite.name = "Magnemite"
magnemite.category = "Magnet Pokemon"
magnemite.type = ["Electric", "Steel"]
magnemite.abilities = ["Magnet Pull", "Sturdy", "Analytic (Hidden)"]
magnemite.moves = ["Thunder Shock", "Tackle", "Supersonic", "Thunder Wave"]

magneton = Pokemon()
magneton.number = "082"
magneton.name = "Magneton"
magneton.category = "Magnet Pokemon"
magneton.type = ["Electric", "Steel"]
magneton.abilities = ["Magnet Pull", "Sturdy", "Analytic (Hidden)"]
magneton.moves = ["Tri Attack", "Electric Terrain", "Thunder Shock", "Thunder Wave"]

farfetchd = Pokemon()
farfetchd.number = "083"
farfetchd.name = "Farfetch'd"
farfetchd.category = "Wild Duck Pokemon"
farfetchd.type = ["Normal", "Flying"]
farfetchd.abilities = ["Keen Eye", "Inner Focus", "Defiant (Hidden)"]
farfetchd.moves = ["Peck", "Sand Attack", "Leer", "Fury Cutter"]

doduo = Pokemon()
doduo.number = "084"
doduo.name = "Doduo"
doduo.category = "Twin Bird Pokemon"
doduo.type = ["Normal", "Flying"]
doduo.abilities = ["Run Away", "Early Bird", "Tangled Feet (Hidden)"]
doduo.moves = ["Peck", "Growl", "Quick Attack", "Rage"]

dodrio = Pokemon()
dodrio.number = "085"
dodrio.name = "Dodrio"
dodrio.category = "Triple Bird Pokemon"
dodrio.type = ["Normal", "Flying"]
dodrio.abilities = ["Run Away", "Early Bird", "Tangled Feet (Hidden)"]
dodrio.moves = ["Jump Kick", "Drill Peck", "Thrash", "Agility"]

seel = Pokemon()
seel.number = "086"
seel.name = "Seel"
seel.category = "Sea Lion Pokemon"
seel.type = ["Water"]
seel.abilities = ["Thick Fat", "Hydration", "Ice Body (Hidden)"]
seel.moves = ["Headbutt", "Growl", "Water Sport", "Aqua Jet"]

dewgong = Pokemon()
dewgong.number = "087"
dewgong.name = "Dewgong"
dewgong.category = "Sea Lion Pokemon"
dewgong.type = ["Water", "Ice"]
dewgong.abilities = ["Thick Fat", "Hydration", "Ice Body (Hidden)"]
dewgong.moves = ["Sheer Cold", "Icy Wind", "Dive", "Safeguard"]

grimer = Pokemon()
grimer.number = "088"
grimer.name = "Grimer"
grimer.category = "Sludge Pokemon"
grimer.type = ["Poison"]
grimer.abilities = ["Stench", "Sticky Hold", "Poison Touch (Hidden)"]
grimer.moves = ["Pound", "Poison Gas", "Disable", "Sludge"]

muk = Pokemon()
muk.number = "089"
muk.name = "Muk"
muk.category = "Sludge Pokemon"
muk.type = ["Poison"]
muk.abilities = ["Stench", "Sticky Hold", "Poison Touch (Hidden)"]
muk.moves = ["Venom Drench", "Poison Gas", "Sludge", "Sludge Bomb"]

shellder = Pokemon()
shellder.number = "090"
shellder.name = "Shellder"
shellder.category = "Bivalve Pokemon"
shellder.type = ["Water"]
shellder.abilities = ["Shell Armor", "Skill Link", "Overcoat (Hidden)"]
shellder.moves = ["Tackle", "Water Gun", "Withdraw", "Ice Shard"]

cloyster = Pokemon()
cloyster.number = "091"
cloyster.name = "Cloyster"
cloyster.category = "Bivalve Pokemon"
cloyster.type = ["Water", "Ice"]
cloyster.abilities = ["Shell Armor", "Skill Link", "Overcoat (Hidden)"]
cloyster.moves = ["Icicle Spear", "Icicle Crash", "Toxic Spikes", "Protect"]

gastly = Pokemon()
gastly.number = "092"
gastly.name = "Gastly"
gastly.category = "Gas Pokemon"
gastly.type = ["Ghost", "Poison"]
gastly.abilities = ["Levitate"]
gastly.moves = ["Lick", "Confuse Ray", "Hypnosis", "Mean Look"]

haunter = Pokemon()
haunter.number = "093"
haunter.name = "Haunter"
haunter.category = "Gas Pokemon"
haunter.type = ["Ghost", "Poison"]
haunter.abilities = ["Levitate"]
haunter.moves = ["Lick", "Hypnosis", "Dream Eater", "Sucker Punch"]

gengar = Pokemon()
gengar.number = "094"
gengar.name = "Gengar"
gengar.category = "Shadow Pokemon"
gengar.type = ["Ghost", "Poison"]
gengar.abilities = ["Cursed Body"]
gengar.moves = ["Perish Song", "Sucker Punch", "Shadow Ball", "Destiny Bond"]

onix = Pokemon()
onix.number = "095"
onix.name = "Onix"
onix.category = "Rock Snake Pokemon"
onix.type = ["Rock", "Ground"]
onix.abilities = ["Rock Head", "Sturdy", "Weak Armor (Hidden)"]
onix.moves = ["Tackle", "Harden", "Bind", "Rock Throw"]

drowzee = Pokemon()
drowzee.number = "096"
drowzee.name = "Drowzee"
drowzee.category = "Hypnosis Pokemon"
drowzee.type = ["Psychic"]
drowzee.abilities = ["Insomnia", "Forewarn", "Inner Focus (Hidden)"]
drowzee.moves = ["Hypnosis", "Pound", "Disable", "Confusion"]

hypno = Pokemon()
hypno.number = "097"
hypno.name = "Hypno"
hypno.category = "Hypnosis Pokemon"
hypno.type = ["Psychic"]
hypno.abilities = ["Insomnia", "Forewarn", "Inner Focus (Hidden)"]
hypno.moves = ["Future Sight", "Hypnosis", "Psychic", "Shadow Ball"]

krabby = Pokemon()
krabby.number = "098"
krabby.name = "Krabby"
krabby.category = "River Crab Pokemon"
krabby.type = ["Water"]
krabby.abilities = ["Hyper Cutter", "Shell Armor", "Sheer Force (Hidden)"]
krabby.moves = ["Water Gun", "Leer", "Harden", "Metal Claw"]

kingler = Pokemon()
kingler.number = "099"
kingler.name = "Kingler"
kingler.category = "Pincer Pokemon"
kingler.type = ["Water"]
kingler.abilities = ["Hyper Cutter", "Shell Armor", "Sheer Force (Hidden)"]
kingler.moves = ["Wide Guard", "Hammer Arm", "Bubble Beam", "Crabhammer"]

voltorb = Pokemon()
voltorb.number = "100"
voltorb.name = "Voltorb"
voltorb.category = "Ball Pokemon"
voltorb.type = ["Electric"]
voltorb.abilities = ["Soundproof", "Static", "Aftermath (Hidden)"]
voltorb.moves = ["Charge", "Tackle", "Sonic Boom", "Screech"]

electrode = Pokemon()
electrode.number = "101"
electrode.name = "Electrode"
electrode.category = "Ball Pokemon"
electrode.type = ["Electric"]
electrode.abilities = ["Soundproof", "Static", "Aftermath (Hidden)"]
electrode.moves = ["Charge", "Sonic Boom", "Electro Ball", "Explosion"]

exeggcute = Pokemon()
exeggcute.number = "102"
exeggcute.name = "Exeggcute"
exeggcute.category = "Egg Pokemon"
exeggcute.type = ["Grass", "Psychic"]
exeggcute.abilities = ["Chlorophyll", "Harvest (Hidden)"]
exeggcute.moves = ["Absorb", "Hypnosis", "Reflect", "Leech Seed"]

exeggutor = Pokemon()
exeggutor.number = "103"
exeggutor.name = "Exeggutor"
exeggutor.category = "Coconut Pokemon"
exeggutor.type = ["Grass", "Psychic"]
exeggutor.abilities = ["Chlorophyll", "Harvest (Hidden)"]
exeggutor.moves = ["Stomp", "Seed Bomb", "Psyshock", "Wood Hammer"]

cubone = Pokemon()
cubone.number = "104"
cubone.name = "Cubone"
cubone.category = "Lonely Pokemon"
cubone.type = ["Ground"]
cubone.abilities = ["Rock Head", "Lightning Rod", "Battle Armor (Hidden)"]
cubone.moves = ["Mud-Slap", "Growl", "Tail Whip", "False Swipe"]

marowak = Pokemon()
marowak.number = "105"
marowak.name = "Marowak"
marowak.category = "Bone Keeper Pokemon"
marowak.type = ["Ground"]
marowak.abilities = ["Rock Head", "Lightning Rod", "Battle Armor (Hidden)"]
marowak.moves = ["Headbutt", "Bonemerang", "Thrash", "Bone Rush"]

hitmonlee = Pokemon()
hitmonlee.number = "106"
hitmonlee.name = "Hitmonlee"
hitmonlee.category = "Kicking Pokemon"
hitmonlee.type = ["Fighting"]
hitmonlee.abilities = ["Limber", "Reckless", "Unburden (Hidden)"]
hitmonlee.moves = ["Brick Break", "Low Kick", "Low Sweep", "Fake Out"]

hitmonchan = Pokemon()
hitmonchan.number = "107"
hitmonchan.name = "Hitmonchan"
hitmonchan.category = "Punching Pokemon"
hitmonchan.type = ["Fighting"]
hitmonchan.abilities = ["Keen Eye", "Iron Fist", "Inner Focus (Hidden)"]
hitmonchan.moves = ["Drain Punch", "Feint", "Bullet Punch", "Mach Punch"]

lickitung = Pokemon()
lickitung.number = "108"
lickitung.name = "Lickitung"
lickitung.category = "Licking Pokemon"
lickitung.type = ["Normal"]
lickitung.abilities = ["Own Tempo", "Oblivious", "Cloud Nine (Hidden)"]
lickitung.moves = ["Lick", "Defense Curl", "Rollout", "Supersonic"]

koffing = Pokemon()
koffing.number = "109"
koffing.name = "Koffing"
koffing.category = "Poison Gas Pokemon"
koffing.type = ["Poison"]
koffing.abilities = ["Levitate", "Neutralizing Gas", "Stench (Hidden)"]
koffing.moves = ["Poison Gas", "Tackle", "Smog", "Smokescreen"]

weezing = Pokemon()
weezing.number = "110"
weezing.name = "Weezing"
weezing.category = "Poison Gas Pokemon"
weezing.type = ["Poison"]
weezing.abilities = ["Levitate", "Neutralizing Gas", "Stench (Hidden)"]
weezing.moves = ["Heat Wave", "Poison Gas", "Tackle", "Smog"]

rhyhorn = Pokemon()
rhyhorn.number = "111"
rhyhorn.name = "Rhyhorn"
rhyhorn.category = "Spikes Pokemon"
rhyhorn.type = ["Ground", "Rock"]
rhyhorn.abilities = ["Lightning Rod", "Rock Head", "Reckless (Hidden)"]
rhyhorn.moves = ["Tackle", "Tail Whip", "Smack Down", "Bulldoze"]

rhydon = Pokemon()
rhydon.number = "112"
rhydon.name = "Rhydon"
rhydon.category = "Drill Pokemon"
rhydon.type = ["Ground", "Rock"]
rhydon.abilities = ["Lightning Rod", "Rock Head", "Reckless (Hidden)"]
rhydon.moves = ["Hammer Arm", "Horn Attack", "Horn Drill", "Megahorn"]

chansey = Pokemon()
chansey.number = "113"
chansey.name = "Chansey"
chansey.category = "Egg Pokemon"
chansey.type = ["Normal"]
chansey.abilities = ["Natural Cure", "Serene Grace", "Healer (Hidden)"]
chansey.moves = ["Sweet Kiss", "Disarming Voice", "Pound", "Soft-Boiled"]

tangela = Pokemon()
tangela.number = "114"
tangela.name = "Tangela"
tangela.category = "Vine Pokemon"
tangela.type = ["Grass"]
tangela.abilities = ["Chlorophyll", "Leaf Guard", "Regenerator (Hidden)"]
tangela.moves = ["Absorb", "Bind", "Stun Spore", "Vine Whip"]

kangaskhan = Pokemon()
kangaskhan.number = "115"
kangaskhan.name = "Kangaskhan"
kangaskhan.category = "Parent Pokemon"
kangaskhan.type = ["Normal"]
kangaskhan.abilities = ["Early Bird", "Scrappy", "Inner Focus (Hidden)"]
kangaskhan.moves = ["Bite", "Stomp", "Crunch", "Endure"]

horsea = Pokemon()
horsea.number = "116"
horsea.name = "Horsea"
horsea.category = "Dragon Pokemon"
horsea.type = ["Water"]
horsea.abilities = ["Swift Swim", "Sniper", "Damp (Hidden)"]
horsea.moves = ["Water Gun", "Leer", "Bubble Beam", "Smokescreen"]

seadra = Pokemon()
seadra.number = "117"
seadra.name = "Seadra"
seadra.category = "Dragon Pokemon"
seadra.type = ["Water"]
seadra.abilities = ["Poison Point", "Sniper", "Damp (Hidden)"]
seadra.moves = ["Dragon Pulse", "Hydro Pump", "Dragon Dance", "Agility"]

goldeen = Pokemon()
goldeen.number = "118"
goldeen.name = "Goldeen"
goldeen.category = "Goldfish Pokemon"
goldeen.type = ["Water"]
goldeen.abilities = ["Swift Swim", "Water Veil", "Lightning Rob (Hidden)"]
goldeen.moves = ["Peck", "Tail Whip", "Horn Attack", "Water Pulse"]

seaking = Pokemon()
seaking.number = "119"
seaking.name = "Seaking"
seaking.category = "Goldfish Pokemon"
seaking.type = ["Water"]
seaking.abilities = ["Swift Swim", "Water Veil", "Lightning Rob (Hidden)"]
seaking.moves = ["Waterfall", "Flail", "Megahorn", "Horn Drill"]

staryu = Pokemon()
staryu.number = "120"
staryu.name = "Staryu"
staryu.category = "Star Shape Pokemon"
staryu.type = ["Water"]
staryu.abilities = ["Illuminate", "Natural Cure", "Analytic (Hidden)"]
staryu.moves = ["Tackle", "Harden", "Water Gun", "Confuse Ray"]

starmie = Pokemon()
starmie.number = "121"
starmie.name = "Starmie"
starmie.category = "Mysterious Pokemon"
starmie.type = ["Water", "Psychic"]
starmie.abilities = ["Illuminate", "Natural Cure", "Analytic (Hidden)"]
starmie.moves = ["Rapid Spin", "Minimize", "Swift", "Psybeam"]

mr_mime = Pokemon()
mr_mime.number = "122"
mr_mime.name = "Mr. Mime"
mr_mime.category = "Barrier Pokemon"
mr_mime.type = ["Psychic", "Fairy"]
mr_mime.abilities = ["Soundproof", "Filter", "Technician (Hidden)"]
mr_mime.moves = ["Pound", "Copycat", "Baton Pass", "Encore"]

scyther = Pokemon()
scyther.number = "123"
scyther.name = "Scyther"
scyther.category = "Mantis Pokemon"
scyther.type = ["Bug", "Flying"]
scyther.abilities = ["Swarm", "Technician", "Steadfast (Hidden)"]
scyther.moves = ["Quick Attack", "Fury Cutter", "Wing Attack", "X-Scissor"]

jynx = Pokemon()
jynx.number = "124"
jynx.name = "Jynx"
jynx.category = "Human Shape Pokemon"
jynx.type = ["Ice", "Psychic"]
jynx.abilities = ["Oblivious", "Forewarn", "Dry Skin (Hidden)"]
jynx.moves = ["Sweet Kiss", "Lick", "Pound", "Powder Snow"]

electabuzz = Pokemon()
electabuzz.number = "125"
electabuzz.name = "Electabuzz"
electabuzz.category = "Electric Pokemon"
electabuzz.type = ["Electric"]
electabuzz.abilities = ["Static", "Vital Spirit (Hidden)"]
electabuzz.moves = ["Quick Attack", "Thunder Shock", "Thunder Punch", "Light Screen"]

magmar = Pokemon()
magmar.number = "126"
magmar.name = "Magmar"
magmar.category = "Spitfire Pokemon"
magmar.type = ["Fire"]
magmar.abilities = ["Flame Body", "Vital Spirit (Hidden)"]
magmar.moves = ["Smog", "Fire Blast", "Ember", "Fire Punch"]

pinsir = Pokemon()
pinsir.number = "127"
pinsir.name = "Pinsir"
pinsir.category = "Stag Beetle Pokemon"
pinsir.type = ["Bug"]
pinsir.abilities = ["Hyper Cutter", "Mold Breaker", "Moxie (Hidden)"]
pinsir.moves = ["Vise Grip", "Bug Bite", "X-Scissor", "Guillotine"]

tauros = Pokemon()
tauros.number = "128"
tauros.name = "Tauros"
tauros.category = "Wild Bull Pokemon"
tauros.type = ["Normal"]
tauros.abilities = ["Intimidate", "Anger Point", "Sheer Force (Hidden)"]
tauros.moves = ["Horn Attack", "Take Down", "Thrash", "Double-Edge"]

magikarp = Pokemon()
magikarp.number = "129"
magikarp.name = "Magikarp"
magikarp.category = "Fish Pokemon"
magikarp.type = ["Water"]
magikarp.abilities = ["Swift Swim", "Rattled (Hidden)"]
magikarp.moves = ["Splash", "Tackle", "Flail", "Hydro Pump"]

gyarados = Pokemon()
gyarados.number = "130"
gyarados.name = "Gyarados"
gyarados.category = "Atrocious Pokemon"
gyarados.type = ["Water", "Flying"]
gyarados.abilities = ["Intimidate", "Moxie (Hidden)"]
gyarados.moves = ["Waterfall", "Aqua Tail", "Hyper Beam", "Hurricane"]

lapras = Pokemon()
lapras.number = "131"
lapras.name = "Lapras"
lapras.category = "Transport Pokemon"
lapras.type = ["Water", "Ice"]
lapras.abilities = ["Water Absorb", "Shell Armor", "Hydration (Hidden)"]
lapras.moves = ["Sing", "Mist", "Life Dew", "Ice Beam"]

ditto = Pokemon()
ditto.number = "132"
ditto.name = "Ditto"
ditto.category = "Transform Pokemon"
ditto.type = ["Normal"]
ditto.abilities = ["Limber", "Imposter (Hidden)"]
ditto.moves = ["Transform"]

eevee = Pokemon()
eevee.number = "133"
eevee.name = "Eevee"
eevee.category = "Evolution Pokemon"
eevee.type = ["Normal"]
eevee.abilities = ["Run Away", "Adaptability", "Anticipation (Hidden)"]
eevee.moves = ["Helping Hand", "Quick Attack", "Swift", "Bite"]

vaporeon = Pokemon()
vaporeon.number = "134"
vaporeon.name = "Vaporeon"
vaporeon.category = "Bubble Jet Pokemon"
vaporeon.type = ["Water"]
vaporeon.abilities = ["Water Absorb", "Hydration (Hidden)"]
vaporeon.moves = ["Water Gun", "Aurora Beam", "Acid Armor", "Hydro Pump"]

jolteon = Pokemon()
jolteon.number = "135"
jolteon.name = "Jolteon"
jolteon.category = "Lightning Pokemon"
jolteon.type = ["Electric"]
jolteon.abilities = ["Volt Absorb", "Quick Feet (Hidden)"]
jolteon.moves = ["Thunder Shock", "Swift", "Take Down", "Thunder Fang"]

flareon = Pokemon()
flareon.number = "136"
flareon.name = "Flareon"
flareon.category = "Flame Pokemon"
flareon.type = ["Fire"]
flareon.abilities = ["Flash Fire", "Guts (Hidden)"]
flareon.moves = ["Ember", "Fire Fang", "Fire Spin", "Flare Blitz"]

porygon = Pokemon()
porygon.number = "137"
porygon.name = "Porygon"
porygon.category = "Virtual Pokemon"
porygon.type = ["Normal"]
porygon.abilities = ["Trace", "Download", "Analytic (Hidden)"]
porygon.moves = ["Tri Attack", "Conversion", "Magnet Rise", "Psybeam"]

omanyte = Pokemon()
omanyte.number = "138"
omanyte.name = "Omanyte"
omanyte.category = "Spiral Pokemon"
omanyte.type = ["Rock", "Water"]
omanyte.abilities = ["Swift Swim", "Shell Armor", "Weak Armor (Hidden)"]
omanyte.moves = ["Bind", "Withdraw", "Rollout", "Water Gun"]

omastar = Pokemon()
omastar.number = "139"
omastar.name = "Omastar"
omastar.category = "Spiral Pokemon"
omastar.type = ["Rock", "Water"]
omastar.abilities = ["Swift Swim", "Shell Armor", "Weak Armor (Hidden)"]
omastar.moves = ["Crunch", "Ancient Power", "Rock Blast", "Surf"]

kabuto = Pokemon()
kabuto.number = "140"
kabuto.name = "Kabuto"
kabuto.category = "Shellfish Pokemon"
kabuto.type = ["Rock", "Water"]
kabuto.abilities = ["Swift Swim", "Battle Armor", "Weak Armor (Hidden)"]
kabuto.moves = ["Absorb", "Harden", "Aqua Jet", "Ancient Power"]

kabutops = Pokemon()
kabutops.number = "141"
kabutops.name = "Kabutops"
kabutops.category = "Shellfish Pokemon"
kabutops.type = ["Rock", "Water"]
kabutops.abilities = ["Swift Swim", "Battle Armor", "Weak Armor (Hidden)"]
kabutops.moves = ["Slash", "Aqua Jet", "Stone Edge", "Leech Life"]

aerodactyl = Pokemon()
aerodactyl.number = "142"
aerodactyl.name = "Aerodactyl"
aerodactyl.category = "Fossil Pokemon"
aerodactyl.type = ["Rock", "Flying"]
aerodactyl.abilities = ["Rock Head", "Pressure", "Unnerve (Hidden)"]
aerodactyl.moves = ["Bite", "Ancient Power", "Supersonic", "Wing Attack"]

snorlax = Pokemon()
snorlax.number = "143"
snorlax.name = "Snorlax"
snorlax.category = "Sleeping Pokemon"
snorlax.type = ["Normal"]
snorlax.abilities = ["Immunity", "Thick Fat", "Gluttony (Hidden)"]
snorlax.moves = ["Yawn", "Body Slam", "Belly Drum", "Giga Impact"]

articuno = Pokemon()
articuno.number = "144"
articuno.name = "Articuno"
articuno.category = "Freeze Pokemon"
articuno.type = ["Ice", "Flying"]
articuno.abilities = ["Pressure", "Snow Cloak (Hidden)"]
articuno.moves = ["Gust", "Mist", "Powder Snow", "Blizzard"]

zapdos = Pokemon()
zapdos.number = "145"
zapdos.name = "Zapdos"
zapdos.category = "Electric Pokemon"
zapdos.type = ["Electric", "Flying"]
zapdos.abilities = ["Pressure", "Static (Hidden)"]
zapdos.moves = ["Peck", "Thunder Wave", "Thunder Shock", "Light Screen"]

moltres = Pokemon()
moltres.number = "146"
moltres.name = "Moltres"
moltres.category = "Flame Pokemon"
moltres.type = ["Fire", "Flying"]
moltres.abilities = ["Pressure", "Flame Body (Hidden)"]
moltres.moves = ["Gust", "Ember", "Wing Attack", "Heat Wave"]

dratini = Pokemon()
dratini.number = "147"
dratini.name = "Dratini"
dratini.category = "Dragon Pokemon"
dratini.type = ["Dragon"]
dratini.abilities = ["Shed Skin", "Marvel Scale (Hidden)"]
dratini.moves = ["Wrap", "Leer", "Dragon Tail", "Outrage"]

dragonair = Pokemon()
dragonair.number = "148"
dragonair.name = "Dragonair"
dragonair.category = "Dragon Pokemon"
dragonair.type = ["Dragon"]
dragonair.abilities = ["Shed Skin", "Marvel Scale (Hidden)"]
dragonair.moves = ["Twister", "Slam", "Dragon Tail", "Hyper Beam"]

dragonite = Pokemon()
dragonite.number = "149"
dragonite.name = "Dragonite"
dragonite.category = "Dragon Pokemon"
dragonite.type = ["Dragon", "Flying"]
dragonite.abilities = ["Inner Focus", "Multiscale (Hidden)"]
dragonite.moves = ["Hurricane", "Roost", "Extreme Speed", "Dragon Tail"]

mewtwo = Pokemon()
mewtwo.number = "150"
mewtwo.name = "Mewtwo"
mewtwo.category = "Genetic Pokemon"
mewtwo.type = ["Psychic"]
mewtwo.abilities = ["Pressure", "Unnerve (Hidden)"]
mewtwo.moves = ["Psychic", "Recover", "Shadow Ball", "Calm Mind"]

mew = Pokemon()
mew.number = "151"
mew.name = "Mew"
mew.category = "New Species Pokemon"
mew.type = ["Psychic"]
mew.abilities = ["Synchronize"]
mew.moves = ["Psychic", "Transform", "Mega Punch", "Protect"]
