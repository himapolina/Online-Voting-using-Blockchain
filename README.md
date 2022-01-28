# Online-Voting-using-Blockchain
## Abstract
A blockchain based solution for online voting. This project only consists of **creation of a genesis block**(first block in the blockchain) for one voter when they cast a vote. However, it can be scaled to make an entire portal for Online Voting based on blockchain technology.

* Online Voting Portal that can be used by voters to cast their vote for the candidates that have already been registered.
* There is more transparency in elections. No third party is trusted with vote validation and/or counting. Every vote, along with the voter’s public key is published and can be viewed by many.
* Critical details like secret key and voter ID are not published. But the validity of a published vote can be checked using the published public key.
* This method reduces fraud that happens in status quo. That is, illegitimate vote count.

Hence, this project can ensure fair elections!

## Detailed explanation of Code
* **Voting_program.py**
  - This is the code for the voting program that takes input from the user, generates secret and public keys and sends the information to voting_blockchain.py for creation of block.
  - We define the gcd, gen_key and power functions to create secret and public key pair.
  - ElGamal algorithm is used here for key generation.
  - Key variable stores the secret key that is generated.
  - We ask for Voter ID of the voter to store the secret key information associated with the voter ID.
  - Assumption – voter ID is a 3-digit integer.
  - Choice of vote is an integer that is the serial number of the candidates contesting the election.
publickKey generated along with the vote is passed onto the voting_blockchain.py for block creation.
  - Secret key and associated voter ID is stored in a text file.
* **Voting_blockchain.py**
  - Flask is a lightweight web application framework written for python.
  - Here, Flask is used to create a REST-API. This builds an interface that we can interact with.
  - Defining a class ‘Block’. It contains all the block information like transactions, timestamp, nonce, hash value and previous hash.
  - Defining a class ‘Blockchain’. Consists of functions that create genesis block and check last block.
  - Compute hash function is defined to compute a hash value using SHA 256 protocol.
  - Proof of work function is defined to compute the hash value using the difficulty and nonce values.
  - We will initially store the data of each transaction in unconfirmed transactions. Once we confirm that the new block is a valid proof that satisfies the difficulty criteria, we can add it to the chain.
  - The vote casted by the voter is stored as a transaction in the block: public key + vote.
  - We defined our web application already. Now we create a local blockchain. 
  - Then, we create an endpoint that allows us to send a query to display the relevant information of the blockchain.
  - When we run this program, our output information of the block is visible on port 5000 on the localhost.

## Architecture and Input
* Voter must first enter their VOTER ID, a 3-digit integer.
* They can then vote for the candidate of their choice by entering the respective Sl. No.
* Voter has an option to change their vote for one time, if they wish to do so.
* This functionality was added in case the voter has entered the wrong number the first time and wants to correct it.
## Output
* A text file named secretKey is appended every time a voter casts their vote.
* This file consists of the voter ID and their respective secret key that was generated using ElGamal Algorithm.
* Block Information can be viewed on port 5000 on the localhost at /chain.
URL for viewing - http://127.0.0.1:5000/chain
* We can see all the information that we defined in the voting_blockchain.py file.
* Transaction details consists of the public key that is [q,g,h] and vote values collected from voting_program.py file.
* This is a genesis block, hence previous hash value is 0 and length of chain is 1.

## Conclusion
* Successfully implemented a **genesis block** for the use case – Online Voting using Blockchain Concepts.
* This project can be used to hold fair and transparent elections.
* This project can be further implemented to create more blocks for multiple voters and candidates. It has great scope for improvement.
* Voters’ **privacy is protected**; neither their voter ID nor their Secret keys are published in the public domain and kept safe in a text file. To add more layers of security, this file can be encrypted using cryptographic algorithms.

