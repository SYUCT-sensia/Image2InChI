The accurate identification and analysis of chemical structures in molecular images is a prerequisite for drug research and development. It is significant to efficiently and automatically convert these images into their respective International Chemical Identifier (InChI) representations. Therefore, this paper proposes an automated molecular optical image recognition model, called Image2InChI, based on an encoder-decoder architecture. In this study, Image2InChI subdivides standardized molecular images into 16x16 patches and utilizes self-attention mechanisms to learn both the global and local information of the molecular images. Additionally, this model introduces a novel feature fusion network to integrate encoder and decoder features. The decoder of the Long Short-Term Memory (LSTM) model with attention mechanism ultimately transforms the image features into the corresponding InChI. Accordingly, experimental outcomes indicate that the Image2InChI model has a Cross Entropy Loss (CE loss) of only 0.0576, and achieves a lower running time and a significantly higher Longest Common Subsequence (LCS) accuracy rate of 96.18% compared to its competitors. The experiments demonstrate that the proposed model significantly improves the accuracy and efficiency of molecular image recognition and provides valuable reference for drug development.

<div align="center">
  <img src="https://github.com/SYUCT-sensia/Image2InChI/blob/dataset/Image2InChI.jpg">
</div>
