
# Data Audit Context for ChatGPT


## Project

Course project topic: Low-Rank Adaptation (LoRA) for adapting Transformer models to financial text sentiment classification.

Main research question: Can LoRA achieve quality comparable to full fine-tuning on financial market sentiment classification while training substantially fewer parameters?

Dataset: zeroshot/twitter-financial-news-sentiment

Generated at: 2026-05-07 11:48:42


## Label Mapping

The label mapping used in all experiments must be:

```text
0 — Bearish
1 — Bullish
2 — Neutral
```


# 1. Original Dataset Structure

The dataset was loaded from Hugging Face using load_dataset("zeroshot/twitter-financial-news-sentiment").


## Original split sizes

```csv
split_original,n_rows,share_%
train,9543,79.98
validation,2388,20.02
```


## Original class distribution

```csv
split_original,total,Bearish,Bullish,Neutral,Bearish_%,Bullish_%,Neutral_%
train,9543,1442,1923,6178,15.11,20.15,64.74
validation,2388,347,475,1566,14.53,19.89,65.58
```


# 2. Label Mapping Check

Unique labels found: [0, 1, 2]

Unexpected labels: []

Missing labels: []


## Label mapping table

```csv
label,label_name,count
0,Bearish,1789
1,Bullish,2398
2,Neutral,7744
```


# 3. Missing Values and Empty Texts


## Missing values report

```csv
column,missing_count,missing_%
text,0,0.0
label,0,0.0
split_original,0,0.0
label_name,0,0.0
```

Number of empty texts: 0


# 4. Duplicates and Conflicting Labels

```json
{
  "total_rows": 11931,
  "unique_raw_texts": 11931,
  "unique_normalized_texts": 11924,
  "duplicate_normalized_texts": 7,
  "texts_with_conflicting_labels": 0
}
```

Important interpretation:

- duplicate_normalized_texts shows how many duplicated normalized texts were found.

- texts_with_conflicting_labels shows how many texts had more than one label.

- Texts with conflicting labels should not be used for model training.


# 5. Original Split Leakage Check

```csv
split_a,split_b,n_texts_a,n_texts_b,n_overlap,overlap_%_of_a,overlap_%_of_b
train,validation,9537,2388,1,0.0105,0.0419
```

If there is overlap between original train and original validation, those texts must be removed from train when original validation is used as final test.


# 6. Final Split Strategy

Official Hugging Face validation split is used as the final test set.

The final validation set for hyperparameter selection is created from the original train split using stratified splitting.

Final split logic:

1. Remove empty texts.

2. Remove texts with conflicting labels.

3. Use original validation as final test.

4. Remove from original train any texts that overlap with final test.

5. Remove duplicate normalized texts inside train candidate and test.

6. Split original train into final train and validation using stratified split.


## Final split sizes

```csv
split_final,n_rows,share_%
test,2388,20.03
train,8105,67.97
validation,1431,12.0
```


## Final class distribution

```csv
split_final,total,Bearish,Bullish,Neutral,Bearish_%,Bullish_%,Neutral_%
test,2388,347,475,1566,14.53,19.89,65.58
train,8105,1225,1633,5247,15.11,20.15,64.74
validation,1431,216,289,926,15.09,20.2,64.71
```


## Final total size

```text
total = 11924
train = 8105
validation = 1431
test = 2388
```


# 7. Final Leakage Check

```csv
split_a,split_b,n_texts_a,n_texts_b,n_overlap,overlap_%_of_a,overlap_%_of_b
train,validation,8105,1431,0,0.0,0.0
train,test,8105,2388,0,0.0,0.0
validation,test,1431,2388,0,0.0,0.0
```

Total final overlap: 0

The correct value should be 0. If it is not 0, the final split has leakage and must be fixed before training models.


# 8. Text Length Statistics


## Overall character and word length summary

```csv
group,metric,mean,median,p90,p95,p99,max
all,char_length,86.02,79.0,139.0,140.0,140.0,227
all,word_length,12.21,12.0,19.0,21.0,23.0,33
```


## Length summary by original split

```csv
group,metric,mean,median,p90,p95,p99,max
train,char_length,85.82,79.0,139.0,140.0,140.0,190
train,word_length,12.18,11.0,19.0,21.0,23.0,32
validation,char_length,86.85,81.0,140.0,140.0,141.0,227
validation,word_length,12.32,12.0,19.0,21.0,23.0,33
```


## Length summary by class

```csv
group,metric,mean,median,p90,p95,p99,max
Bearish,char_length,83.13,76.0,137.0,140.0,141.0,151
Bearish,word_length,11.95,11.0,18.0,20.0,22.12,32
Bullish,char_length,81.14,74.0,136.0,140.0,140.0,227
Bullish,word_length,12.02,11.0,18.0,20.0,23.0,33
Neutral,char_length,88.21,83.0,140.0,140.0,141.0,190
Neutral,word_length,12.33,12.0,19.0,21.0,23.0,29
```


# 9. Token Length Statistics

Tokenizer used for audit: distilbert-base-uncased


## Token length summary

```csv
metric,token_length
mean,27.68
median,25.0
p90,47.0
p95,50.0
p99,57.0
max,82.0
```


## Coverage by max_length

```csv
max_length,covered_%
64,99.81
128,100.0
256,100.0
512,100.0
```

Recommended max_length for Transformer experiments: 128

max_length=128 covers 100.00% of texts.

max_length=256 covers 100.00% of texts.


# 10. Qualitative Examples by Class

These examples are included for qualitative sanity check. They should be used to verify that Bearish, Bullish and Neutral labels look semantically reasonable.


## Examples: Bearish

```csv
split_original,label,label_name,text
validation,0,Bearish,"Highlight: ""We're gonna see companies start to report results and I think it's gonna look ugly,"" @FBBCap's Mike Bai… https://t.co/gdtm8YBxPc"
train,0,Bearish,This week in Trumponomics: 'Phase one' fizzles https://t.co/D9rtXUJXsB by @rickjnewman https://t.co/3kO62Lsqdf
train,0,Bearish,$NSSC: Napco Security Systems sees Q3 revs below consensus https://t.co/UllrqyQtlU
train,0,Bearish,"Funko stock plummets 39%, shares downgraded after holiday season weakness"
train,0,Bearish,"$ASLN $KZIA $XXII - KL, CBAY among premarket losers https://t.co/ITIV0JhjBM"
```


## Examples: Bullish

```csv
split_original,label,label_name,text
train,1,Bullish,Declining Rig Counts Point To Higher Energy Prices And A Headwind For The U.S. Economy
train,1,Bullish,Synaptics stock price target raised to $40 from $32 at J.P. Morgan
train,1,Bullish,"RECAP 4/7 +Pos Comments:
$CLDR + Craig Hallum
$XOM + CFRA
$BTI + MS"
train,1,Bullish,$JETS $ALGT $HA - U.S. airline traffic stays solid https://t.co/ZbOFc0gE22
train,1,Bullish,$CLR - Continental Resources: Still Going Strong. https://t.co/naXlXnnaSp #stocks #business #trading
```


## Examples: Neutral

```csv
split_original,label,label_name,text
train,2,Neutral,"Morgan Stanley says forecasting just the next two months, let alone 2020, is hard right now https://t.co/f3ToNSUFXu"
train,2,Neutral,Facebook co-founder eyes direct listing for Asana https://t.co/d2k631l6Ac
train,2,Neutral,Dow Jones News: Microsoft Reveals Next Xbox; Apple Avoids Tariffs
train,2,Neutral,Edited Transcript of GFF earnings conference call or presentation 13-Nov-19 9:30pm GMT
train,2,Neutral,"Mueller Industries, Inc. (NYSE:MLI) Is Yielding 1.3% - But Is It A Buy?"
```


# 11. Metrics for Future Experiments

Primary metric: macro F1

Secondary metrics:

- accuracy

- weighted F1

- per-class precision

- per-class recall

- per-class F1

- confusion matrix

Reason: if the classes are imbalanced, accuracy alone can be misleading. Macro F1 gives equal importance to Bearish, Bullish and Neutral.


# 12. Planned Models

The next experiments should compare:

1. TF-IDF + Logistic Regression

2. DistilBERT full fine-tuning

3. DistilBERT + LoRA

4. BERT-base full fine-tuning

5. BERT-base + LoRA

6. FinBERT full fine-tuning

7. FinBERT + LoRA

All models must use the same final train / validation / test split. The test set must only be used for final evaluation.


# 13. Methodological Notes for Coursework

The empirical study should not claim that LoRA is universally better than full fine-tuning.

The correct claim format is:

```text
Within the selected dataset, models and experimental setup, LoRA is compared with full fine-tuning in terms of classification quality, number of trainable parameters, training time and, if possible, memory usage.
```

The main comparison should focus on:

- macro F1

- trainable parameter count

- training time

- per-class errors

- confusion matrix

- whether quality loss from LoRA is small enough to justify parameter efficiency


# 14. Final Data Audit Decision

```text
final_overlap_total = 0
texts_with_conflicting_labels = 0
duplicate_normalized_texts = 7
recommended_max_length = 128
primary_metric = macro F1
```

Preliminary conclusion:

The dataset can be used as the main benchmark for the course project if:

1. final_overlap_total is 0.

2. conflicting labels were removed.

3. final train / validation / test split is fixed and not changed after seeing model results.

4. macro F1 is used as the primary metric.
