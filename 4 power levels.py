for pirates

p_basic = {
"strength": 2, 
"defence": 10, 
"health": 100,  
"alive": True,  
"attack":(5,10)
"name":"Space Pirate", 
"description":"""You encountered a Space Pirate.
From your knowledge, Space Pirates have a lot of health 
as they don't have many real body parts since most were replaced 
because of previous injuries. However they don't hit hard."""
}

p_elite = {
"strength": 2, 
"defence": 15, 
"health": 100,  
"alive": True,  
"attack":(5,10)
"name":"Pirate Corsair", 
"description":"""You encountered a Space Pirate Corsair.
The weakest known space pirates to actually get involved with a boarding action.
They serve as meat shields and labour for the more powerful pirates 
and are often looking for the perfect time to stab their superior in the back 
and earn a promotion.""" 
}

p_superior = {
"strength": 2, 
"defence": 20, 
"health": 100,  
"alive": True,  
"attack":(5,10)
"name":"Pirate Armsman", 
"description":"""You encountered a Space Pirate Armsman.
Their curious name comes from the heavy weapon systems that 
replace their previously human arms in an attempt to bring 
anti-ship weaponry onto a more portable platform. 
Most Armsmen underwent surgery without their consent and 
can only take their rage out on their victims, or you for that matter."""
}

p_boss = {
"strength": 20, 
"defence": 20, 
"health": 100,  
"alive": True,  
"attack":(5,10)
"name":"Pirate Lord", 
"description":"""You encountered a Space Pirate Lord.

Leading from the front has always been the best method of 
insuring loyalty among pirate factions and this Pirate Lord 
is demonstrating exactly that. He stands before you to make 
an example out of you, to demonstrate to his subordinates 
that no one stands in the way of a pirate legion

This fight is no joke. Standing in front of you is an assailant 
of immense fortitude and power. His immense stature augmented with cyber technology 
far more powerful than you have encountered on any of his whelps before. 
His mere presence causes cold sweat to pour down your face and his voice 
booms like a thousand drums beating in unison. This will not be an easy 
fight, feel free to retreat and come back when you are better prepared to 
deal with such a fearsome foe."""
}

enemy_pirate = p_basic
enemy_pirate_corsair = p_elite
enemy_pirate_armsman = p_superior
enemy_pirate_ravager = p_boss

for aliens

a_basic = {
"strength": 10, 
"defence": 2, 
"health": 25,  
"alive": True,  
"attack":(20,30)
"name":"Alien",
"description":"""You encountered an Alien.

It looks weird and hits like a space shuttle.
Aliens can kill some people with one hit, 
however they don't have much health"""
}

a_elite = {
"strength": 20, 
"defence": 2, 
"health": 25,  
"alive": True,  
"attack":(20,30)
"name": "Savage Alien"
"description": """ You encountered an Savage Alien.

They are stronger then the usual Alien.
This is because of their thick exo-suit,
which protects them from the harshness of deep space."""
}

a_superior = {
"strength": 30, 
"defence": 2, 
"health": 25,  
"alive": True,  
"attack":(20,30)
"name": "Formidabble Alien"
"description": """You encountered a Formidabble Alien.

They are second in command, 
they are warriers travelling through the galaxies doing the work of their queen,
they have been blessed with remarkable strength."""
}

a_boss = {
"strength": 30, 
"defence": 8, 
"health": 25,  
"alive": True,  
"attack":(20,30)
"name": "Alien Queen"
"description": """ You encountered an Alien Queen.

She has not only strength but inteligence, having lived for 1000's of years,
she has grown tired of her world,
commanding her childeren to expand their reach, expand the hive.
Your chances of success are slim."""}


enemy_alien = a_basic
enemy_alien_savage = a_elite
enemy_alien_formiddable = a_superior
enemy_alien_queen = a_boss

for monster

m_basic = {
"strength": 5,
"defence": 5,
"health": 50, 
"alive": True, 
"attack":(10,20)
"name": "Goopy Monster"
"description": """ You encountered an Goopy Monster.

Not a lot is know about them or where they came from,
most likely a failed lab experiment.
Goopy Monsters have a nice mix of health and strength"""}

m_elite = {
"strength": 10,
"defence": 5,
"health": 50, 
"alive": True, 
"attack":(10,20)
"name": "Squishy Monster"
"description": """ You encountered an Squishy Monster.

This little pain can hide in the smallest crevis there is and wait.
It will try to suprise you so be careful, condsidering their small size their strength is vast,
dont underestimate them."""}

m_superior = {
"strength": 20,
"defence": 5,
"health": 50, 
"alive": True, 
"attack":(10,20)
"name": "Creep Monster"
"description": """You encountered an Creep Monster.

Its long tenticles have increased its strength dramatically, using them to crush any unwanted fellow.
Be carefull on this one, and have your eyes on those tenticles!""" }

m_boss = {
"strength": 20,
"defence": 10,
"health": 50, 
"alive": True, 
"attack":(10,20)
"name": "Scary Monster"
"description": """You encountered an Scary Monster.

A creature spat out of hell itself, so evil, so sinister, feeding of the fear of the crew it has groen strong.
It is still Hungry... It senses your prescence."""}

enemy_monster_goopy = m_basic
enemy_monster_squishy = m_elite
enemy_monster_creep = m_superior
enemy_monster_scary = m_boss


