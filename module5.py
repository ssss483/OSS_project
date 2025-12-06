# module 5 
# replace <mask> to tokens with KLUE RoBERTa predictions.


  def apply_fill_mask(masked_sentence):
    predictions = fill_mask(masked_sentence)
    best = predictions[0]["token_str"].strip() # Extracts the top predicted token and removes extra whitespace.

    return masked_sentence.replace("<mask>", best, 1) 


# in main," completed_sentence = apply_fill_mask(masked_sentence) " received like this.
