# module 5 
  def apply_fill_mask(masked_sentence):
    predictions = fill_mask(masked_sentence)
    best = predictions[0]["token_str"].strip()
      
    return masked_sentence.replace("<mask>", best, 1) 


# in main," completed_sentence = apply_fill_mask(masked_sentence) " received like this.

