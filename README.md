# LA CIPHER - Encryption and decryption
Developed project in the course Computer science - Universidade Paulista - UNIP
A project about Encryption.

## :pushpin: About
In the project you need a keys for encryption or decryption of your messages.<br>
You can choose between 3 to 20 keys and all keys should be different.<br>
You can open a txt file, update it and create a new file with the final message.<br>

In the example below i use 3 keys and my name as message.<br>
The result: swzhu<br>

key 1: 123<br>
key 2: 456<br>
key 3: 789<br>

message: lucas<br>

L = 76 - 12 - 123 = 59<br>
U = 85 - 21 - 456 = 392<br>
C = 67 - 3 - 789 = 725<br>
A = 65 - 1 - 123 = 59<br>
S = 89 - 19 - 456 = 392<br>

The first number is the letter in the ASCII table.<br>
The second number is the letter in alphabetical order.<br>
The third number is the key.<br>

Difference: <br>
59 - 52 = 7<br>
392 - 390 = 2<br>
725 - 702 = 23<br>
59 - 52 = 7<br>
392 - 390 = 2<br>

The logic<br>
Is 26 * 1 = 26 greater than 59? No, continue<br>
26 * 2 = 52 no again<br>
26 * 3 = 78 is greater than 7<br>

Then 59 - 52 = 7<br>

From de current letter move total difference forward until you get to the new letter.<br>

Decryption is the same logic, but you move backwards.<br>

New message: swzhu<br>

## :lock: Encryption
<img src="https://github.com/lucas-serafim/La-cipher/blob/main/readme/encryption.jpg" width="900">
  
## :unlock: Decryption
<img src="https://github.com/lucas-serafim/La-cipher/blob/main/readme/decryption.jpg" width="900">

## :computer: Technologies
- Python

## :octocat: Clone this project
Use this command in your gitbash ``git clone https://github.com/lucas-serafim/La-cipher.git``

##
<p align="center">
  Project developed for university members. 
</p>
