# NLP Project

### Enviroment
- Windows Linux Subsystem

## Running repo

1. clone repo

```shell
git clone https://github.com/franksalas/nlp_project.git
```

2. create enviroment from yml file

```shell
conda env create -f environment.yml
```

3. activate enviroment

```shell
source activate spacy
```
4. get to work

... or  run [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/franksalas/nlp_project/master)

It might crash tho..


# Objectives

## Analyze unstructured data 

 • Transforming unstructured data into structured data via information extraction system. For example, convert investor memo (text format) to a well-defined structure (table format with pre-defined values), such as investor name, preference (geography, property type, investment size)
 

## Requirements
- Extract useful entities from unstructured text data
- reshape to structure with predefined values
    - name
    - preference
        - geography
        - property type
        - investment size


 
### Sample Investor Memo Data
- converted to JSON format to replicate API call
- dummy data was added to complete name entity
- Client A:
    - company: Argos Group
    - contact: Adam
- Client B:
    - Company: Blue Industries
    - None
- Client C:
    - Company: Circle Inc
    - Contact: Carol


## Possible Solution
Apply spaCy to unstructured text

1. view raw text
```
I recently caught up with Adam of Argos Group and he indicated they are actively trying to grow their
        portfolio in the US. They have been focused in NYC, but with his recent addition to the team, are
        looking in Chicago and on the West Coast. Their main focus continues to be high-rise office in CBDs, but
        are also considering urban multi-housing, preferably with a value-add component.
```

1. Extract entities with spacy
![memo 1](/images/memo_1A.PNG "memo_1")

2. Save entities in a format compatible for structure manipulation

```python
{'PERSON': ['Adam'],
 'ORG': ['Argos Group'],
 'GPE': ['US', 'Chicago'],
 'LOC': ['NYC', 'the West Coast'],
 'DATE': ['CBDs']}
```

## Problems w/ Solution
- Domain-specific terms not available
- multiple versions of the same word return errors
- not enough data for training

## Recommendations
- Updating the Named Entity Recognizer
- needs more data for correct NER training
- train for domain-specific terms
 - Real Estate & Financial Abbreviations

```
[ROC,REIT,MOB,"value-add",...]
```
- example https://github.com/explosion/spacy/blob/master/examples/training/train_ner.py


## Small Solutions
## Multiple versions of similar word

Apply regular expressions

```python
multi_family = '(?i)mult*\w*\-?fam*\w*'  # mUlTyFamily
text = 'This multifamily is not very good. my Multi-family is better. Not as good as my MULTIFAMILY'
match = re.findall(multi_family,text)
match
# ['multifamily', 'Multi-family', 'MULTIFAMILY']
```

## Extract monetary values from text

```python
money = '\$?(?i)\d{1,3}[m|b]\w*'  # CREAM
text = '''
But you ain't a Saint, this ain't KumbaYe
But you got hurt because you did cool by 'Ye
You gave him 20m without blinkin'
He gave you 20 minutes on stage,...
'''
match = re.findall(money,text)
match
# ['20m']
```



## Expand Domain specific acronyms
### text

```
I will be based in New York, mainly tasked with sourcing equity and debt investments in high-profile
        real estate assets in gateway markets with equity ticket $30M and up. My team and I will also look for JV
        and M&A opportunities of established real estate companies and platforms.
```

### results
```
JV: Joint Venture
M&A:  Mergers and Acquisitions
```

## Problem with Small Solutions

## Regular expressions

>... Some people, when confronted with a problem, think “I know,
I'll use regular expressions.”  Now they have two problems.
    - Jamie Zawinski
    
## Domain specific acronyms
- Does not scale
- topic modeling as possible choice

    
