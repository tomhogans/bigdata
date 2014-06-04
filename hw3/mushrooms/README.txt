This data is prepared from Mushroom records drawn from The
Audubon Society Field Guide to North American Mushrooms
(1981). G. H. Lincoff (Pres.), New York: Alfred A. Knopf

 This data set includes descriptions of hypothetical samples
 corresponding to 23 species of gilled mushrooms in the Agaricus
 and Lepiota Family (pp. 500-525 of the Field Guide).  Each
 species is identified as definitely edible, definitely
 poisonous, or of unknown edibility and not recommended.  This
 latter class was combined with the poisonous one.  The Guide
 clearly states that there is no simple rule for determining the
 edibility of a mushroom; no rule like ``leaflets three, let it
 be'' for Poisonous Oak and Ivy.

There are 8124 instances in all with 23 nominally valued
attributes as described below:

Attribute Information: 

     0: class:                edible=e, poisonous=p
     1. cap-shape:                bell=b,conical=c,convex=x,flat=f,
                                  knobbed=k,sunken=s
     2. cap-surface:              fibrous=f,grooves=g,scaly=y,smooth=s
     3. cap-color:                brown=n,buff=b,cinnamon=c,gray=g,green=r,
                                  pink=p,purple=u,red=e,white=w,yellow=y
     4. bruises?:                 bruises=t,no=f
     5. odor:                     almond=a,anise=l,creosote=c,fishy=y,foul=f,
                                  musty=m,none=n,pungent=p,spicy=s
     6. gill-attachment:          attached=a,descending=d,free=f,notched=n
     7. gill-spacing:             close=c,crowded=w,distant=d
     8. gill-size:                broad=b,narrow=n
     9. gill-color:               black=k,brown=n,buff=b,chocolate=h,gray=g,
                                  green=r,orange=o,pink=p,purple=u,red=e,
                                  white=w,yellow=y
    10. stalk-shape:              enlarging=e,tapering=t
    11. stalk-root:               bulbous=b,club=c,cup=u,equal=e,
                                  rhizomorphs=z,rooted=r,missing=?
    12. stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
    13. stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
    14. stalk-color-above-ring:   brown=n,buff=b,cinnamon=c,gray=g,orange=o,
                                  pink=p,red=e,white=w,yellow=y
    15. stalk-color-below-ring:   brown=n,buff=b,cinnamon=c,gray=g,orange=o,
                                  pink=p,red=e,white=w,yellow=y
    16. veil-type:                partial=p,universal=u
    17. veil-color:               brown=n,orange=o,white=w,yellow=y
    18. ring-number:              none=n,one=o,two=t
    19. ring-type:                cobwebby=c,evanescent=e,flaring=f,large=l,
                                  none=n,pendant=p,sheathing=s,zone=z
    20. spore-print-color:        black=k,brown=n,buff=b,chocolate=h,green=r,
                                  orange=o,purple=u,white=w,yellow=y
    21. population:               abundant=a,clustered=c,numerous=n,
                                  scattered=s,several=v,solitary=y
    22. habitat:                  grasses=g,leaves=l,meadows=m,paths=p,
                                  urban=u,waste=w,woods=d

Note that "feature" 0 is really the target label (whether a
mushroom is edible or poisonous). The remmaing features are true
attributes. There are some missing attribute values, 2480 of them
in all (denoted by "?"), and are all for attribute #11. You
should replace the nominal values with non-zero integers to
encode the data, before you run the sklearn code on it. In
particular, you should encode the target label as -2 for
poisonous and +2 for edible. 

Use the first 5000 instances to train a linear regression model
and determine how well it predicts the class label of a random
collection of 25 instances from among the remaining 3124
instances. The prediction should be translated as poisonous if
the predicted value for the target is negative and edible
otherwise. Summarize and create visualizations of your results. 
