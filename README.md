# VideoClassification
This repo have three deep learning solutions for general video classification problem

1. A 3D CNN approch
2. A Transfer Learning + LSTM approch
3. A CNN + Time distributed LSTM approch
            
The folder 'dataset' won't be there in repo, so create one at your working directory
The programs are maintaned as python notebook



How to run the classifiers?

1. Create a folder dataset(as mentioned above)
2. Run download_dataset.py(it will dowload the dataset in dataset folder)
3. Run the python notebook corresponding to the required model.

Note : 
The same dataset is used for all three models

# Requirements

platform: linux-64

numpy=1.19.0=pypi_0

numpydoc=0.9.1=py_0

keras=2.3.1=pypi_0

keras-applications=1.0.8=pypi_0

keras-preprocessing=1.1.0=pypi_0

scikit-learn=0.21.3=py37hd81dba3_0

cloudpickle=1.2.2=py_0

pickleshare=0.7.5=py37_0

matplotlib=3.2.1=pypi_0

opencv-contrib-python=4.2.0.34=pypi_0

opencv-python=4.1.2.30=pypi_0

cvlib=0.2.5=pypi_0

json5=0.8.5=py_0

jsonschema=3.0.2=py37_0

pandas=0.25.1=py37he6710b0_0

youtube-dl=2020.7.28=pypi_0

*run setup.py for installing requirements automatically

