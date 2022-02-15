# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 00:44:13 2018

@author: hp
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('crime.csv')
X = dataset.iloc[0:166, 0].values
y1 = dataset.iloc[:, 10].values
y2 = dataset.iloc[:, 11].values
y = [1, 2, 4, 1, 1, 2, 1, 1, 1, 2, 0, 2, 0, 2, 0, 2, 2, 2, 4, 0, 1, 0, 1,
       1, 3, 1, 2, 1, 1, 1, 0, 4, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 1, 1, 2, 0,
       4, 2, 1, 0, 1, 2, 0, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 2, 0, 2, 1, 0, 1,
       2, 2, 1, 4, 1, 2, 0, 0, 1, 0, 1, 1, 4, 2, 1, 3, 1, 0, 2, 2, 2, 1, 0,
       0, 4, 1, 2, 1, 1, 0, 3, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 3, 0,
       0, 1, 2, 1, 2, 0, 2, 3, 0, 1, 3, 2, 1, 0, 1, 4, 2, 4, 2, 1, 1, 1, 1,
       1, 1, 1, 1, 3, 0, 0, 2, 1, 1, 0, 0, 1, 2, 1, 0, 2, 1, 0, 3, 0, 0, 2,
       0, 0, 2, 2, 1]
places = ['CHITRANJAN PARK', 'DABRI', 'MALVIYA NAGAR', 'CHANDNI MAHAL',
       'MODEL TOWN', 'ANANDVIHAR', 'KASHMERE GATE', 'GOVIND PURI',
       'BINDAPUR', 'NEW FRIENDS COLONY', 'SARITA VIHAR', 'TIMARPUR',
       'KANJHAWALA', 'ANAND PARBAT', 'SAGARPUR', 'PRASHANT VIHAR',
       'SOUTH CAMPUS', 'ROHINI SOUTH', 'PUNJABI BAGH', 'DWARKA NORTH',
       'BURARI', 'JAMA MASJID', 'ADRASH NAGAR', 'CHANAKYAPURI',
       'PANDAV NAGAR', 'MIANWALI NAGAR', 'FATEHPUR BERI', 'NABI KARIM',
       'RAJOURI GARDEN', 'JAHANGIR PURI', 'KAMLA MARKET',
       'BARAKHAMBA ROAD', 'SAFDARJUNG ENCLAVE', 'MUKHERJI NAGAR',
       'FARASH BAZAR', 'KALKAJI', 'KALKAJI', 'PARSHAD NAGAR',
       'LODHI COLONY', 'INDERPURI', 'OKHLA', 'SAMAYPURBADLI',
       'JAFFARPUR KALAN', 'MAYA PURI', 'AMAN VIHAR', 'VIJAY VIHAR',
       'AMAR COLONY', 'ALIPUR', 'MAHENDRA PARK', 'VASANT KUNJ SOUTH',
       'BHALSWA DAIRY', 'BAWANA', 'BEGUM PUR', 'NARAINA', 'NEB SARAI',
       'RAJINDER NAGAR', 'SHALIMAR BAGH', 'KESHAV PURAM', 'RANI BAGH',
       'BARA HINDU RAO', 'CONNAUGHT PLACE', 'H. N. DIN', 'DARYA GANJ',
       'MANGOLPURI', 'VIVEKVIHAR', 'LAHORI GATE', 'SULTAN PURI',
       'GEETA COLONY', 'CIVIL LINES', 'ASHOK VIHAR', 'TILAK NAGAR',
       'PALAM VILLAGE', 'MOTI NAGAR', 'HARI NAGAR', 'PAHARGANJ',
       'SADAR BAZAR', 'SAROJINI NAGAR', 'NAJAFGARH', 'KAPASHERA',
       'KALYANPURI', 'BADAR PUR', 'SUBHASH PLACE', 'SUBZIMANDI',
       'MAURICE NAGAR', 'MANDIR MARG', 'TUGLAK ROAD', 'LAJPAT NAGAR',
       'KRISHNA NAGAR', 'PRASHANT VIHAR', 'ANANDVIHAR', 'SWARUP NAGAR',
       'GREATER KAILASH', 'VIKAS PURI', 'UTTAM NAGAR', 'DEFENCE COLONY',
       'JAMIA NAGAR', 'KASHMERE GATE', 'PULPRAHLAD PUR', 'SARITA VIHAR',
       'NANGLOI', 'SAFDARJUNG ENCLAVE', 'HAUZQAZI', 'DWARKA SOUTH',
       'PASCHIM VIHAR', 'BINDAPUR', 'TILAK MARG', 'RAJOURI GARDEN',
       'SANGAM VIHAR', 'MAYURVIHAR', 'SHAHBAD DAIRY', 'GANDHI NAGAR',
       'DWARKA SEC-23', 'RANJIT NAGAR', 'RANHOLA', 'SAKET', 'SHAKARPUR',
       'PREETVIHAR', 'KIRTI NAGAR', 'HAUZ KHAS', 'BAWANA', 'KN KATJU MARG',
       'I.P. ESTATE', 'KOTALA MUBARAK PUR', 'DELHI CANTT', 'D.B.G ROAD',
       'KHYALA', 'JAGATPURI', 'PATEL NAGAR', 'VASANT VIHAR', 'KAROL BAGH',
       'SUNLIGHT COLONY', 'NARELA', 'NEW ASHOK NAGAR', 'PARLIAMENT STREET',
       'NIHAL VIHAR', 'MADHUVIHAR', 'BHARAT NAGAR', 'MANDAWALI',
       'BABA HARI DAS NAGAR', 'CHHAWLA', 'MEHRAULI', 'MAURYA ENCLAVE',
       'JANAK PURI', 'SARAI ROHILLA', 'GULABIBAGH', 'ROOP NAGAR',
       'VASANT KUNJ NORTH', 'ROHINI NORTH', 'GHAZIPUR', 'SEEMAPURI',
       'SEELAMPUR', 'MANSAROVAR PARK', 'SHAHDARA', 'KHAJURIKHAS',
       'JYOTI NAGAR', 'HARSH VIHAR', 'MUNDKA', 'BHAJANPURI', 'ZAFRABAD',
       'WELCOME', 'NANDNAGARI', 'G.T.B. ENCLAVE', 'NEW USMANPUR',
       'SONIA VIHAR', 'KARAWAL NAGAR', 'GOKULPURI']
new_array= []
for i in range(0, 166):
    str = places[i]+", Delhi, India"
    new_array.append(str)
dataset2 = pd.read_csv('crime2.csv')
lati = dataset2.iloc[:, 0].values
longi = dataset2.iloc[:, 1].values

ar = []
   
for i in range(0, 166):
    y1[i] = round(y1[i], 4)
    y2[i] = round(y2[i], 4)

    o = {  "type": "Feature",
           "properties": { 'mag': y[i]   },                 
            'lati': y1[i], 
            'longi': y2[i]
          
           
            
        }
    ar.append(o)
print(ar)
'''