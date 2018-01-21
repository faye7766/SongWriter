#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:05:35 2017

@author: fayewang
"""
import pandas as pd

data =  pd.read_csv('songdata.csv')

name = str(input("Enter the singer's name: "))

# try Adele
sub = data.text[data['artist'] == name]
sub = sub.reset_index()
t = ''.join(sub['text'])

# save to txt
with open("lyrics.txt", "w") as text_file:
    text_file.write(t)


# try rap song singers
# https://www.biography.com/people/groups/most-streamed-rappers-on-spotify
rap = ['LL Cool J', 'Tupac Shakur', 'Biggie Smalls', 'Jay-Z', 'Dr. Dre', 'Eminem', 'Queen Latifah',
       'Adam Horovitz', 'Donald Glover', 'Kanye West', 'Big Boi', 'Black Thought', "Lil' Kim", 'Nas',
       'Migos', 'Rza', 'DJ Premier', 'Pete Rock', 'Schoolly D', 'G-Easy', 'J-Cole', 'Drake', 
       'Lil Wayne', 'Nicki Minaj','Wiz Khalifa', 'Kendrick Lamar', 'DJ Khaled','Pharell Williams',
       'Timbaland', 'Common Sense', 'The Sugarhill Gang', '2Pac',
       'Nas', 'Audio Two', 'Public Enemy', 'Snoop Dogg', 'Geto Boys',
       'dead prez', 'MC Lyte', 'Beastie Boys', 'Talib Kweli', 'Brand Nubian',
       'Mos Def', 'Westside Connection', 'Warren G', 'DMX', 'O.C.',
       'Scarface', 'OutKast', 'M.O.P','Slick Rick', 'Aasim', 'Marley Marl',
       'Artifacts','UGK', 'Black Moon',' Big Daddy Kane', '50 Cent']

rap_dat = data[data['artist'].isin(rap)]

rap_t = ''.join(rap_dat['text'])

# save to txt
with open("raps.txt", "w") as text_file:
    text_file.write(rap_t)

#### rock
rock = ['Robert Plant', 'Freddie Mercury', 'Mick Jagger', 'Paul McCartney',
        'Janis Joplin','Bruce Springsteen', 'Axl Rose', 'Ann Wilson','David Bowie',
        'Bob Dylan', 'Bono','John Lennon','Neil Young','Stevie Nicks',
        'Kurt Cobain','Roger Daltrey', 'Jim Morrison', 'Steven Tyler',
        'Jon Bon Jovi', 'Ozzy Osbourne', 'Bon Jovi', 'Nirvana',
        'Pearl Jam', 'Foo Fighters', 'Soundgarden', 'Red Hot Chili Peppers',
        'Stone Temple Pilots', 'Nine Inch Nails', 'Rage Against the Machine',
        'Live', 'Korn']

rock_dat = data[data['artist'].isin(rock)]

rock_t = ''.join(rock_dat['text'])

# save to txt
with open("rocks.txt", "w") as text_file:
    text_file.write(rock_t)

###### country
ct = ['Hank Williams', 'Johnny Cash', 'Merle Haggard', 'Jimmie Rodgers','Waylon Jennings',
      'George Jones', 'Dolly Parton', 'Loretta Lynn','Willie Nelson', 'Lefty Frizzel',
      'Buck Owens', 'Gene Autry', 'Kitty Wells',  'Kris Kristofferson', 'Gram Parsons',
      'Glen Campbell', 'Patsy Cline', 'Porter Wagoner', 'Ernest Tubb', 'Tammy Wynette',
      'Chet Atkins', 'Jim Reeves', 'Roy Acuff', 'Ray Price', 'Roger Miller', 'The Carter Family', 
      'Alabama', 'The Louvin Brothers', 'Charlie Daniels Band', 'The Stanley Brothers', 'Dixie Chicks',
      'THE JUDDS', 'Lonestar', 'Brooks & Dunn', 'The Oak Ridge Boys', 'Zac Brown Band', 'Sugarland', 'Montgomery Gentry',
      'Lady Antebellum', 'The Highwaymen', 'Bill Monroe', 'Bob Wills', 
      'Ray Price', 'Ernest Tubb', 'Hank Snow', ]    

ct_dat = data[data['artist'].isin(ct)]

ct_t = ''.join(ct_dat['text'])

# save to txt
with open("country.txt", "w") as text_file:
    text_file.write(ct_t)
    
    
#### folk
fk = ['The Alamanac Singers', 'Ani DiFranco', 'Ben Harper',  'Bob Dylan', 'The Carter Family', 
      'Cat Stevens', 'Charlie Poole', 'Dave Carter and Tracy Grammer', 'Dave Van Ronk', 'Doc Watson', 
      'Emmylou Harris', 'Gillian Welch', 'The Grateful Dead', 'Greg Brown', 'Guy Clark', 'Holly Near', 'Harry Belafonte',
      'Ian & Sylvia', 'James Taylor', 'Janis Ian', 'Joan Baez', 'John Gorka', 'John Prine', 'Johnny Cash', 'Joni Mitchell',
      'Judy Collins', 'The Kingston Trio', 'Kris Kristofferson', 'Leonard Cohen',  'The Mamas and the Papas', 'Michael Franti & Spearhead', 
      'Neil Young', 'Nickel Creek', 'Odetta', 'Patty Griffin', 'Pete Seeger', 'Phil Ochs', 'Richard Shindell', 'Steve Earle',
      'Tom Paxton', 'Tom Waits', 'Utah Phillips', 'The Weavers', 'Woody Guthrie']

fk_dat = data[data['artist'].isin(fk)]

fk_t = ''.join(fk_dat['text'])

# save to txt
with open("folk.txt", "w") as text_file:
    text_file.write(fk_t)

###### pop
pop = ['Lady Gaga', 'Madonna', 'One Direction', 'Black Eyed Peas', 'Justin Bieber', 
       'Christina Aguilera', 'Walk the Moon', 'Christina Perri', 'Pink', 'Passenger',
       'Adele', 'Grren Day', 'Idina Menzel', 'Katy Perry', 'Rihanna', 'Susan Boyle', 'Beyonce',
       'Shakira', 'Maroon 5', 'Pitbull', 'Ryan Tedder', 'Whitney Houston', 'Sia',
       'Jay Sean', 'Rob Thomas', 'Bow Wow', 'Taylor Swift', 'Micheal Jackson', 'Miley Cyrus',
       'Jessie J', 'Kelly Clarkson', 'Prince', 'Jordin Sparks', 'Kesha', 'Madonna', 
       'The Police', 'U2', 'R.E.M.', 'John Mellencamp', 'Selena Gomez', 'Nena', 
       'Eric Carmen', 'Talk Talk']
pop_dat = data[data['artist'].isin(pop)]

pop_t = ''.join(pop_dat['text'])

# save to txt
with open("pop.txt", "w") as text_file:
    text_file.write(pop_t)