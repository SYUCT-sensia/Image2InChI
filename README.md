The accurate identification and analysis of chemical structures in molecular images is a prerequisite for drug research and development. It is significant to efficiently and automatically convert these images into their respective International Chemical Identifier (InChI) representations. Therefore, this paper proposes an automated molecular optical image recognition model, called Image2InChI, based on an encoder-decoder architecture. In this study, Image2InChI subdivides standardized molecular images into 16x16 patches and utilizes self-attention mechanisms to learn both the global and local information of the molecular images. Additionally, this model introduces a novel feature fusion network to integrate encoder and decoder features. The decoder of the Long Short-Term Memory (LSTM) model with attention mechanism ultimately transforms the image features into the corresponding InChI. Accordingly, experimental outcomes indicate that the Image2InChI model has a Cross Entropy Loss (CE loss) of only 0.0576, and achieves a lower running time and a significantly higher Longest Common Subsequence (LCS) accuracy rate of 96.18% compared to its competitors. The experiments demonstrate that the proposed model significantly improves the accuracy and efficiency of molecular image recognition and provides valuable reference for drug development.

<div align="center">
  <img src="https://github.com/SYUCT-sensia/Image2InChI/blob/dataset/Image2InChI.jpg">
</div>
Project Status
📢 News: Our research paper is currently in the process of being submitted for publication. Stay tuned for updates on its progress!

While the project is not yet complete, we are actively working on improving and expanding its functionality. We plan to continually update the repository.

Contributing
We welcome contributions from the community! If you’re interested in contributing to our project, please refer to our Contribution Guidelines. By contributing, you can help us make Image2InChI even better.

Issues and Bug Reports
If you encounter any issues or bugs while using Image2InChI, please open an issue on our GitHub repository. We appreciate your help in improving the project and addressing any problems.

Contact
For any questions or inquiries, please contact our team at image2inchi@example.com.

Thank you for your interest in Image2InChI! We look forward to your support and feedback.
