# Chicken Disease Classification Project

This project focuses on building an end-to-end system for classifying chicken diseases using Convolutional Neural Networks (CNNs). The model is trained to distinguish between healthy chickens and those affected by *Coccidiosis* based on fecal images. The project includes deployment and testing workflows on AWS and Azure for practical usability.

---

## 📂 Project Overview

Chicken diseases, especially *Coccidiosis*, are a significant challenge in poultry farming. Early and accurate detection is crucial to minimizing losses. This project leverages deep learning to automate the classification process, offering a scalable solution for poultry health management.

### Key Features:
- **Deep Learning Model**: CNN-based classifier trained on chicken fecal images.
- **End-to-End System**: Includes model training, evaluation, deployment, and testing workflows.
- **Multi-Cloud Deployment**: Integrated deployment pipelines for AWS and Azure.
- **DVC Integration**: Tracks data and model versioning efficiently.

---

## 🚀 Workflows

1. Update `config.yaml`
2. Update `secrets.yaml` *(optional)*
3. Update `params.yaml`
4. Define entities
5. Configure the `ConfigurationManager` in the `src/config` directory
6. Implement core components
7. Create and test the pipeline
8. Update `main.py`
9. Modify the `dvc.yaml` for pipeline versioning

---

## 🔧 How to Run

### Clone the Repository
```bash
git clone https://github.com/entbappy/Chicken-Disease-Classification--Project
cd Chicken-Disease-Classification--Project
````

### STEP 01: Set Up the Environment

Create and activate a Conda environment:

```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### STEP 02: Install Dependencies

```bash
pip install -r requirements.txt
```

### STEP 03: Run the Application

```bash
python app.py
```

### Access the Application

Open your browser and navigate to your local host and port as specified by the application.

---

## 🛠️ DVC Commands

1. Initialize DVC:

   ```bash
   dvc init
   ```
2. Reproduce the pipeline:

   ```bash
   dvc repro
   ```
3. Visualize the pipeline DAG:

   ```bash
   dvc dag
   ```

---

## 📊 Model Pipeline Overview

1. **Data Preprocessing**:

   * Cleanses and augments input images.
   * Ensures data consistency for training.

2. **Model Training**:

   * CNN architecture optimized for image classification.
   * Trained on a labeled dataset of healthy and *Coccidiosis*-affected chicken fecal images.

3. **Evaluation**:

   * Validates model performance using precision, recall, and accuracy metrics.
   * Includes visualization of training and validation loss curves.

4. **Deployment**:

   * Packaged as a Docker container.
   * Tested on AWS (ECR + EC2) and Azure (Azure Container Registry + Web App).

---

## 🖥️ Deployment Workflows

### AWS Deployment Steps:

1. Build Docker image.
2. Push the image to Amazon ECR.
3. Launch an EC2 instance.
4. Pull the image from ECR to the EC2 instance.
5. Run the application in the EC2 instance.

### Azure Deployment Steps:

1. Build Docker image.
2. Push the image to Azure Container Registry.
3. Deploy the image to an Azure Web App Server.
4. Launch the application from the container registry.

---

## 📜 Future Enhancements

* Add support for additional chicken diseases.
* Optimize the model for real-time inference.
* Incorporate more advanced deployment pipelines (e.g., Kubernetes).
* Explore edge computing for on-site disease classification.

---

## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your proposed changes.

---

## 💡 Acknowledgments

This project is inspired by the need for automated disease detection in poultry farming, ensuring healthier chickens and reducing economic losses.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Happy Coding! 🐔

```
