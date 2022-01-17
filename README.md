# Bag-of-word-SER

Step 1: Extract  modulation spectral fetaures using window size of 256 ms and frame size of 40 ms (or 64 ms).
Step 2: Extract bag of words on top of these modulation spectrum.
Step 3: These BoW represented feature work as a input to the LSTM model
Step 4: Extract SRMR as a quality feature and these features can be fused to provide robustness along with BOW modulation features. 


