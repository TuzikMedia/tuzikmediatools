# **tuzikmediatools**

## installation

`pip install tuzikmediatools`

or

`pip3 install tuzikmediatools`

## Description

**tuzikmediatools** - is a small module that can generate strings from user-specified characters.

## Usage

### import

`
import tuzikmediatools as tmt
`


### Generate

```
  import tuzikmediatools as tmt

  # tmt.generate(lenght, symbols='a-z / numbers / castom_symbols', case='low / up', numbers_range=(from, before)) 


  tmt.generate(8) # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> qHG1%lb4


  tmt.generate(8, symbols = 'a-z') # >>>>>>>>>>>>>>>>>>>>>>>>> ajTDkapW

  tmt.generate(6, symbols='a-z', case='up') # >>>>>>>>>>>>>>>> URLDGQ
  tmt.generate(12, symbols='a-z', case='low') # >>>>>>>>>>>>>> kdyemfjsgisy


  tmt.generate(6, symbols='numbers') # >>>>>>>>>>>>>>>>>>>>>>> 194837

  tmt.generate(6, symbols='numbers', numbers_range=(0, 6)) # > 163402
  tmt.generate(6, symbols='numbers', numbers_range=(0, 1)) # > 010011
  
  
  tmt.generate(6, symbols='1230 *') # >>>>>>>>>>>>>>>>>>>>>>>> 10 *32
  tmt.generate(6, symbols='йцукенгшщзх') # >>>>>>>>>>>>>>>>>>> кщйгцк
```


