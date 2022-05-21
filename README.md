# Bag-of-word-SER
![bow_mod3_1 (2)](https://user-images.githubusercontent.com/34964872/169665298-84b865f4-6f8b-49c6-a7b5-bb391c198967.png)

Step 1: Extract  modulation spectral fetaures using window size of 256 ms and frame size of 40 ms (or 64 ms). <br />
Step 2: Extract bag of words on top of these modulation spectrum. <br />
Step 3: These BoW represented feature work as a input to the LSTM model <br />
Step 4: Extract SRMR as a quality feature and these features can be fused to provide robustness along with BOW modulation features.  <br />


![low_high_val](https://user-images.githubusercontent.com/34964872/169665479-c24b53da-998f-4a5c-a0d0-253c82bce215.png)
