#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Imports
import sys
import random
import numpy

# Global variables
## Menu variables
in_menu = True

## Game variables
positions = ['LW', 'ST', 'SS', 'RW', 'LM', 'AM', 'M', 'RM', 'DM', 'LB', 'CB', 'RB', 'GK']
nationalities = ['ENG', 'BR', 'ESP']
leagues = ['PL', 'BRA', 'LL']
staff_roles = ['player training', 'pt', 'player physiotherapy', 'pp',
               'player medical', 'pm', 'head scout', 'hs',
               'assistant scout', 'as']

## Names
### English names (41 names in total)
fnames_ENG = ['Oliver', 'George', 'Harry', 'Jack', 'Jacob', 'Noah', 'Charlie',
              'Muhammad', 'Thomas', 'Oscar', 'Matthew', 'Jamie', 'Aaron',
              'Josh', 'Alex', 'Harrison', 'Bruyne', 'John', 'Spencer', 'Aidan',
              'Ellis', 'Morgan', 'Terry', 'Joey', 'Scot', 'Jeffry', 'Eddie',
              'Sebastian', 'Alfred', 'Danny', 'James', 'Bobbie', 'Lenny', 'Kevin',
              'Wilford', 'Fred', 'Tim', 'Sheldon', 'Lester', 'Porter', 'Davie']

lnames_ENG = ['Ward', 'Wilson', 'John', 'Moore', 'Hart', 'Russell', 'Gardner',
              'Ashton', 'Jarvis', 'Poole', 'Parkes', 'Lyons', 'Smith', 'Jones',
              'Williams', 'Walker', 'Brown', 'Gilbert', 'Dixon', 'Preston',
              'Fraser', 'Sutton', 'Tod', 'Snider', 'Randall', 'Jephson', 'Blue',
              'Preston', 'Neville', 'Giles', 'Fulton', 'Winton', 'Adams', 'Sheppard',
              'Green', 'Larson', 'Rodgers', 'Blackburn', 'Simons', 'Newton', 'Headley']

### Portuguese-Brazilian names (32 names in total)
fnames_BR = ['Pedro', 'Henrique', 'Davi', 'Paulo', 'Eduardo', 'Rodrigo', 'Gustavo',
             'Thiago', 'Nicolas', 'Leonardo', 'Lucas', 'Gabriel', 'Cauã', 'Antônio',
             'Alexandre', 'Ronaldo', 'Otávio', 'Jailson', 'Felipe', 'João', 'André',
             'Guilherme', 'Diego', 'Fábio', 'Pietro', 'Michel', 'Tomas', 'José',
             'Luis', 'Jair', 'Joaquim', 'Igor']

lnames_BR = ['Rincon', 'Silva', 'Santos', 'Barbosa', 'Badial', 'Barros', 'De Paula',
             'Araujo', 'Oliveira', 'Costa', 'Correia', 'Meucci', 'Rodrigues', 'Cavalcante',
             'Martins', 'Braga', 'Mendes', 'Almeida', 'Bolsonaro', 'Rocha', 'Marques', 'Ferreira',
             'Melo', 'Dias', 'Gonçalves', 'Cunha', 'Temer', 'Turbando', 'Pereira',
             'Azevedo', 'Neto', 'Pinto']

### Spanish names (40 names in total)
fnames_ESP = ['Carlos', 'Alejandro', 'Pablo', 'Mateo', 'Marcelo', 'Simón', 'Maximiliano',
              'Sergio', 'Adelardo', 'Roldán', 'Patricio', 'David', 'Eusebio', 'Héctor',
              'Domingo', 'Severo', 'René', 'Nazario', 'Haroldo', 'Godofredo', 'Fortunato',
              'Carlito', 'Vidal', 'Ramiro', 'Sancho', 'Miguelángel', 'Andre', 'Xavi',
              'Jesus', 'Carles', 'Tomás', 'Pancho', 'Fabián', 'Ernesto', 'Rómulo', 'Juán',
              'Guillermo', 'Ricardo', 'Pepe', 'Nacho']

lnames_ESP = ['Rincón', 'Rojas', 'Escobar', 'Catalán', 'Cardoso', 'Meléndez', 'Ramos',
              'Chaves', 'Ríos', 'Machado', 'Silva', 'Castro', 'Martínez', 'García',
              'Espina', 'Franco', 'Perez', 'Moralez', 'De La Cruz', 'Herrero', 'Fuentes',
              'Guerrero', 'Ventura', 'Aguado', 'Arenas', 'Iniesta', 'Hernandes',
              'Navas', 'Puyol', 'Gonzales', 'Fontana', 'Méndez', 'Cruz', 'Campo', 'Santos',
              'Cardozo', 'Gallo', 'Espinoza', 'Ríos']

# Classes
class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def __del__(self):
        print("%s (%s) was fired"%(self.name, self.role))

class Player:
    def __init__(self, name, age, position, shooting, dribbling, speed, passing, positioning, defense):
        self.name = name
        self.age = int(age)
        position = position.upper()
        with position as p:         
            if p in positions:
                self.position = position
            else:
                raise ValueError("Invalid player position")
        self.shooting = int(shooting)
        self.dribbling = int(dribbling)
        self.speed = int(speed)
        self.passing = int(passing)
        self.positioning = int(positioning)
        self.defense = int(defense)
    def __del__(self):
        print("%s was sent away"%(self.name))

class Team:
    def __init__(self, name, league, home_country):
        self.name = name
        if league == '1':
            self.league = 'PL'
            pass
        elif league == '2':
            self.league = 'BR'
            pass
        elif league == '3':
            self.league = 'LL'
            pass
        self.home_country = home_country
        
        self.staff = []
        self.players = []
    def add_staff(self, staff_name, staff_role):
        s = Staff(staff_name, staff_role)
        self.staff.append(s)
    def add_player(self, n, a, position, sho, dri, speed, pas, positioning, defense):
        p = Player(n, a, position, sho, dri, speed, pas, positioning, defense)
        self.players.append(p)
    def random_staff(self, nation, rrole):
        if nation.upper() in nationalities and rrole.lower() in staff_roles:
            pass
        else:
            raise ValueError("Invalid staff arguments")
        fname, lname = random_name(nation)
        name = fname + ' ' + lname
        self.add_staff(name, rrole)

# Functions
def random_name(nationality):
    if nationality.upper() in nationalities:
        fname = eval("random.choice(fnames_%s)"%(nationality))
        lname = eval("random.choice(lnames_%s)"%(nationality))
        return fname, lname
    else:
        raise ValueError("Invalid nationality in random name generator")

def create_game():
    tn = input("Team name: ")
    tl = input("Select a league: [1] PRIME LEAGUE (PL) | [2] BRAZILEIRINHO (BR) | [3] LE LEAGUE (LL)\n> ")
    if tl == '1':
        tl = 'PRIME LEAGUE'
        ht = 'ENG'
    elif tl == '2':
        tl = 'BRAZILEIRINHO'
        ht = 'BR'
    elif tl == '3':
        tl = 'LE LEAGUE'
        ht = 'ESP'
    else:
        raise ValueError("Invalid league", tl)
    t = Team(tn, tl, ht)
    print("Generating staff...")
    t.random_staff(t.home_country, 'player training')
    t.random_staff(t.home_country, 'player physiotherapy')
    t.random_staff(t.home_country, 'player medical')
    t.random_staff(t.home_country, 'head scout')
    t.random_staff(t.home_country, 'assistant scout')
    print("Staff was generated")
    
    
def check(inp):
    if inp == '1':
        # New game
        print("Creating new game...")
        in_menu = False
        create_game()
        return None
    elif inp == '2':
        # Load game
        return print("Coming soon")
    elif inp == '3':
        # Exit
        print("Exiting game...")
        return sys.exit(0)
# Main
if __name__=='__main__':
    print("----- Pysoccer -----\n1 - New game\n2 - Load game\n3 - Exit")
    while in_menu == True:
        usr = str(input("\n> "))
        check(usr)
        
