# Causal_Relation_Extraction

![Language](https://img.shields.io/badge/Language-Python3-blue.svg) [![GitHub license](https://img.shields.io/github/license/prateekguptaiiitk/Causal_Relation_Extraction.svg)](https://github.com/prateekguptaiiitk/Causal_Relation_Extraction/blob/master/LICENSE) [![HitCount](http://hits.dwyl.io/{prateekguptaiiitk}/{Causal_Relation_Extraction}.svg)](http://hits.dwyl.io/{prateekguptaiiitk}/{Causal_Relation_Extraction})


Causal Relation Extraction and Identification using Conditional Random Fields. It was a project under our faculty [Mr. Tirthankar Dasgupta](https://www.linkedin.com/in/tirthankar-dasgupta-89b0551/).

[Link](https://docs.google.com/presentation/d/1YaRbxTpHDO4jnRgMU_OG_1xm6cr_gTgt_8riPPF3dr8/edit?usp=sharing) to the project presentation.

## Introduction

Causal Relation is a relation between two events: cause and effect. Cause is the producer of the effect, and effect the result of the cause. </br>

Ex.  “Hunger is the most common cause of crying in a young baby.” Here cause is “Hunger” and effect is “Crying”.</br>
The present work is focused on the detection and extraction of Causal Relations from Medical domain text.</br>

From the point of view of detecting Causal Relations, the following distinctions may be useful:</br>
</br>
 **• Marked or unmarked:** a causation is marked if there is a specific linguistic unit that signals the relation; unmarked otherwise. “I bought it because I read a good review” is marked; “Be careful. It’s unstable” isn’t.</br>
 **• Ambiguity:** if the mark signals always a causation, it is unambiguous (e.g. “because”). If it signals sometimes a causation, it is ambiguous (e.g. “since” ). </br>
**• Explicit or implicit:** a causation is explicit if both arguments are present; implicit if one or both are missing. “She was thrown out of the hotel after she had run naked through its halls.” is explicit; “John killed Bob.” is implicit, since the effect, Bob’s death, is not explicitly stated. We focus on marked and explicit causations.</br>

## Workflow

**1. Data Preprocessing** </br>
**2. Feature Selection and Extraction** </br>
**3. Training Model** </br>
**4. Testing Model Prediction Accuracy** </br>

## Data Preprocessing

<ul>
  <li>Extracting unique words</li>
  <li>POS Tagging & Term Labelling (CC- cause, EE- effect, O- Null, RR- relation(Causal Link word) )</li>
</ul>

#### Code Snippet:-
![alt text](https://github.com/prateekguptaiiitk/Causal_Relation_Extraction/blob/master/preprocessing.png)

## Feature Selection and Extraction

<ul>
  <li>Word Case (upper/lower)</li>
  <li>Word POS</li>
  <li>Word title</li>
  <li>Type (Alphanumeric/Character)</li>
</ul>

## Model Selection and Training

Statistical Model [CRF (Conditional Random Field)](https://en.wikipedia.org/wiki/Conditional_random_field) is used from [sklearn-crfsuite library](https://sklearn-crfsuite.readthedocs.io/en/latest/). We trained model on our preprocessed training dataset.

#### Code Snippet:-
![alt text](https://github.com/prateekguptaiiitk/Causal_Relation_Extraction/blob/master/crf.png)

## Model Testing

Testing model on test data with following Precession, Recall, & F-1 score values. 		

#### Code Snippet:-
![alt text](https://github.com/prateekguptaiiitk/Causal_Relation_Extraction/blob/master/modelTesting.png)

## The Results of Conditional Random Field:-

![alt text](https://github.com/prateekguptaiiitk/Causal_Relation_Extraction/blob/master/results.png)

## Future Scope

To get more accurate result we can use (Sequence Models) Deep Neural Networks, like Bidirectional LSTM Models. </br>
These models can be used owing to their high accuracy because of their very deep feature extraction capabilities. Only disadvantage is that they (LSTMs) require very large amount of data for training. </br>

## References 

• [University Of New Zealand](http://www-ist.massey.ac.nz/dstirlin/CAST/CAST/Hcausal/causal_c2.html) </br>
• [Wikipedia](https://en.wikipedia.org/wiki/Conditional_random_field) </br>
• [Automatic Extraction of Causal Relations from Text using Linguistically
    Informed Deep Neural Networks](https://www.aclweb.org/anthology/W18-5035) </br>
    
## Author

<table>
<tr>
<td>
     <img src="https://avatars2.githubusercontent.com/u/29523950?s=400&u=878e242ca2c624eb45a62bf62ae580a370b7a0ae&v=4" width="180"/>
     
     Prateek Gupta

<p align="center">
<a href = "https://github.com/prateekguptaiiitk"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://twitter.com/prateek_gupta21"><img src = "https://www.shareicon.net/download/2016/07/06/107115_media.svg" width="36" height="36"/></a>
<a href = "https://www.linkedin.com/in/prateekjpg/"><img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/></a>
</p>
</td>
</tr> 
  </table>
    
## Other Contributor

Special Thanks to [Shivendra Pratap Singh](https://github.com/shivendrapratap2) for all his efforts and contributions.

