# Amazon Purchase List

For a better purchase experience, the products bought on a single purchase are stored on an array as many times as the product is ordered. Every product has a unique numeric ID. For instance, 2 shampoos `(ID 12)`, 3 dog food `(ID 34)`*,* and 1 soap `(ID 89)` would be stored as the following purchase list = `[12,12,34,34,34,89]`

After the purchase is performed, for a more efficient search of the products, we will need to store the products bought on the purchase only `12,34,89`

##### Follow UP

Because purchases are indexed, we can't create a new array, so the transformation must be done in-place. W only need to store where the array with the products actually ends.

`[12,12,34,34,34,89]` should return `([12,34,89,34,34,89],3)`
