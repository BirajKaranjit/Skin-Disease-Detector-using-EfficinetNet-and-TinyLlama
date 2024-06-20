# Skin Disease Detector using EfficientNet

## Project Summary and Motivation

The aim of this project is to develop a tool that, given an image of a skin lesion(lesion is that part of skin in which the skin texture looks different than other areas/parts) , can predict the likelihood of the lesion being a specific skin disease.
Skin diseases, including skin cancer, can have significant impacts on individuals' health, making early detection and diagnosis crucial.

### Key Facts About Skin Diseases

- Skin diseases is a prevalent disease, with new cases surpassing the combined incidence of several other non-canerous and cancerous diseases.
- Early detection of melanoma, a type of skin cancer, has a significant impact on survival rates. The estimated 5-year survival rate for early-detected melanoma is about 98%.

### Motivation

Given the importance of early detection, the development of a tool to assist in the early identification of skin diseases can contribute to better health outcomes.
This project leverages advanced machine learning techniques, specifically Convolutional Neural Networks (CNNs) and EfficientNet, to achieve this goal.

## Development Process and Data

The project involves constructing a CNN model to predict the likelihood that a skin lesion is one of several specified skin diseases.
In order to make the developmental task easier, we imported a pre-trained version of the efficientnet_bo model and implemented in our Skin Disease Detection tasks and further trained(fine-tuned) 
it on multiple epochs on around 4000+ datasets of 15 different classes of skin diseases.
The training, validation and testing losses are calculated along with the precision, accuracy, recall etc. and we viewed that these losses got significantly decreased after the completion of model
fine-tuning.

### Data

The dataset used for this project comprises images from the International Skin Imaging Collaboration (ISIC), and many other datasets from Kaggle, ImageNet etc.
The data includes both benign(non-cancerous) and malignant(cancerous) lesions, with the following breakdown:

Total images used:
- Benign Images: ~2500
- Malignant Images: ~1500

### Preprocessing

The following preprocessing steps were applied to the images:

- Visual inspection to filter out low-quality or non-representative images
- Image resizing to 224x224 pixels
- Normalization to standardize the pixel values

### CNN Model

The initial model is based on EfficientNet, a state-of-the-art CNN architecture known for its efficiency and accuracy. The model development process includes:

1. Data augmentation: Techniques such as rotation, noise addition, and scaling to prevent overfitting.
2. Transfer learning: Utilizing a pre-trained EfficientNet model and fine-tuning it with additional layers to enhance performance.

### Model Evaluation
The model is evaluated using many evaluation metrices such as accuracy, recall, precision, F1Score etc. 

## Results Presentation

The final tool predicts the likelihood that a skin lesion is one of several specified skin diseases. The results are presented to the user through mobile applications.

### Mobile Applications
  #Android App
Our CNN model will be loaded into the mobile phone to make local predictions. Advantages: The image then will be send to the backend server and processed, after that the result of the 
prediction is sent back to mobile along with the some skin care recommendations.
For now, both the mobile phone and the laptop containg the Flask server has to be connected in the same Wi-Fi network in order to send_request and receive_response from mobile UI and backend respectively.
## Project Schedule

| Activity                           | Days | Status | Progress |
|------------------------------------|------|--------|----------|
| Data Acquisition                   | 1    | Done   | ++++     |
| Initial Preprocessing and Visualizations | 1 | Done | ++++ |
| First Model Construction and Tuning | 2 | Done | ++++ |
| Model Optimization I (Data Augmentation) | 1 | Done | ++++ |
| Model Optimization II (Transfer Learning) | 3| Done | ++++ |
| Model Optimization III (Fine Tuning) | 4| Done | ++++ |
| App Development            | 4   | Done| ++++     |
| Presentation Preparation           | 5   | Done   | ++++     |

## Tools Used

- Pytorch (Google Colab GPU High Performance Cloud Computing)
- Python
- Matplotlib
- Scikit-learn
- Flask (for API development)



