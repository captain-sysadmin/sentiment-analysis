# A horrible API for sentiment analysis

this is a simple python app that receives a POST'd JSON object and returns the posistve and negative sentiment value.

## how do I use?

Post a json goop to /:

```
{"sentences":[
    "on a long and frosty morning I sutmbled upon the Vicar.",
    "I said hello, and went on my way."]
}
```

and if it's all ok, It'll reply with:

```
{
    "negative_score": 1.125, 
    "positive_score": 0.0
}
```

As you can see, it was a solidly negative example
