# **tuzikmediatools**

## installation


`pip install tuzikmediatools`\
or\
`pip3 install tuzikmediatools`\
or\
`python -m pip install tuzikmediatools`

## Description

**tuzikmediatools** - is a small module that can:
1. Generate strings from user-specified characters.
2. Сheck if a number is prime
3. Count the number of words in a text

## Usage

### import

```
import tuzikmediatools as tmt
```


### Generate

```
import tuzikmediatools as tmt

# tmt.generate(lenght, 
#              symbols='a-z / numbers / castom_symbols', 
#              case='low / up', 
#              numbers_range=(from, before), 
# ) 


tmt.generate(8) # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> qHG1%lb4


tmt.generate(8, symbols = 'a-z') # >>>>>>>>>>>>>>>>>>>>>>>>>> ajTDkapW

tmt.generate(6, symbols='a-z', case='up') # >>>>>>>>>>>>>>>>> URLDGQ
tmt.generate(12, symbols='a-z', case='low') # >>>>>>>>>>>>>>> kdyemfjsgisy


tmt.generate(6, symbols='numbers') # >>>>>>>>>>>>>>>>>>>>>>>> 194837

tmt.generate(6, symbols='numbers', numbers_range=(0, 6)) # >> 163402
tmt.generate(17, symbols='numbers', numbers_range=(0, 1)) # > 10011110011100010


tmt.generate(6, symbols='1230 *') # >>>>>>>>>>>>>>>>>>>>>>>>> 10 *32
tmt.generate(6, symbols='йцукенгшщзх') # >>>>>>>>>>>>>>>>>>>> кщйгцк
```


### Is_prime

```
import tuzikmediatools as tmt

tmt.is_prime(5) # >>>>>>>>  True
tmt.is_prime(18) # >>>>>>>  False
tmt.is_prime(-3, 5, 4) # > (False, True, False)
```


### Word_count

```
import tuzikmediatools as tmt

tmt.word_count('Hello, world!') # >>>>>>>>>>>>>>>>>>>>>>>>>  2
tmt.word_count('Hello,   word!', 'Hello, how are you?') # > (2, 4)
```
