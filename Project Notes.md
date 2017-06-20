# Overview
____
This project is an experiment with Generative Adversarial Neural Networks to try and catch card counters in casinos. In this project, however, there will be many generator networks, and one discriminator network. The many generator networks will each be card counting using a [different style](##Counting Styles Used). The discriminator network will learn from each of these networks how to catch card counters. The generator networks will be trained to both profit, and avoid being caught card counting, so that they don't just always lose money to avoid being caught.

## Generator Networks
____
Each generator network will stem from the following basic structure:

- Inputs
  - The count for that specific network on the table
  - The sum of the cards in the networks hand
  - The dealer's count (all a network has to do to make money is beat the dealer)
- Outputs
  - Hit or stay

Generator networks have a much harder training than the discriminator network. Generator networks must not only stay profitable, but also not be caught card counting. Since defining a loss function of two variables might be challenging, we have to define a loss function of one variable, but have it be influenced by others. For example, we could define a loss function in terms of profits, and if the network doesn't bust on the move, it gets a value of 0, if it beats the dealer, it gets a value of double the bet (which will be the expected output), and the negative bet amount if it busts, and double the negative bet amount if it is suspected of card counting over a certain threshold. This really is just so that we have the generator networks behave appropriately for the discriminator network. The goal of this project is not to  develop a fantastic card counting network, but rather one to catch card counters. 

## Discriminator Network
____
The discriminator network will have the following inputs and outputs

- Inputs
  - The count from each card counting system present on the table
  - The move a certain network made that round
  - The sum of the cards of the certain network before card was dealt
  - Dealt card value
- Output
  - Probability rating of whether or not the network was card counting

The discriminator network will have a very simple loss function, which is the difference between whether or not the network was counting cards, and its prediction. 

## Control Networks
____
We will also have a few control networks following basic blackjack strategy that are not card counting so that the network can accurately determine what card counting does NOT look like. 
## Counting Styles Used
____
- Hi-Lo
- K-O
- Hi-Opt 1
- Hi-Opt 2
- Halves
- Omega 2
- Red Seven
- Zen

[Reference](https://www.blackjackapprenticeship.com/resources/card-counting-systems/)
____


