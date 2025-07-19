#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Imports
import sys
import random
import numpy

# Global variables
## Menu variables
in_menu = True

# ## Game variables
# positions = ['LW', 'ST', 'SS', 'RW', 'LM', 'AM', 'M', 'RM', 'DM', 'LB', 'CB', 'RB', 'GK']
# nationalities = ['ENG', 'BR', 'ESP']
# leagues = ['PL', 'BRA', 'LL']
# staff_roles = ['тренер', 'pt', 'физиотерапевт', 'ph',
#                'врач', 'med', 'главный скаут', 'hs',
#                'скаут', 'as']

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

# Main
if __name__=='__main__':
    print("----- Pysoccer -----")
