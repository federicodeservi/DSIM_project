# **DSIM_project**

Github repository for Digital Signal & Image Recognition project.

## **Folders**

* **species_to_choose**: select which species will be used in the project

* **audio_download**: download audio files from Animal Sound Archive (gbif.org)

* **monodimensional**: audio recognition
    * **data**: contains the notebook that converts wav files to mel-spectrograms and the spectrograms themselves
    * **fine-tuning**: audio recognition fine-tuning a ResNet
    * **classifiers**: audio recognition using a ResNet as a feature extractor and  by training classical classifiers on the extracted features

* **bidimensional**: image recognition
    * **data**: contains the image dataset used ([Awa2](https://cvml.ist.ac.at/AwA2/))
    * **fine-tuning**: audio recognition fine-tuning a ResNet

* **retrieval**: retrieval
    * **data**: contains the image dataset used ([Awa2](https://cvml.ist.ac.at/AwA2/))
    * **retrieval**: retrieval using a ResNet and a KDTree

* **presentation**: Powerpoint presentation of the project

* **demo**: contains the video of the Demo created for this project and available [here](https://github.com/federicodeservi/DSIM_demo) 



## **Authors**

Federico De Servi, Federico Luzzi
