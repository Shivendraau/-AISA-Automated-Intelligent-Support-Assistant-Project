from setuptools import findpackages,setup

setup(
    name='Resolution_Generator',
    version='0.0.1',
    author='Shivendra Pratap Shahi',
    author_email='shivendraau@gmail.com',
    install_requires=['azure-functions','azure-identity','azure-keyvault-secrets','azure-storage-blob','opencensus-ext-azure','openai','joblib','scikit-learn','flask','pandas','python-dotenv'],
    packages=findpackages()
)

