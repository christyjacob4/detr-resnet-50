# Hugging Face DETR Object Detection Flask API

This repository contains a Flask API for object detection using the Hugging Face `facebook/detr-resnet-50` model. The API provides two endpoints: one for getting object detection results in JSON format and another for getting an image with bounding boxes drawn around detected objects.

## Project Structure

```plaintext
.
├── Dockerfile
├── LICENSE.md
├── README.md
├── app
│   ├── __init__.py
│   └── main.py
├── docker-compose.yml
└── requirements.txt
```

- `Dockerfile`: Dockerfile used to build the Docker image for the application.
- `LICENSE.md`: File containing the license information for this project.
- `README.md`: This file, containing information about the project and instructions on how to set it up.
- `app/`
  - `__init__.py`: File where the Flask application is initialized.
  - `main.py`: File containing the Flask route definitions and main application logic.
- `docker-compose.yml`: Docker Compose file to facilitate the deployment of the application using Docker Compose.
- `requirements.txt`: File listing the Python packages required for the application.

## Setup and Installation

### Prerequisites

- Docker installed on your system.
- Docker Compose installed on your system (if you intend to use Docker Compose).

### Building the Docker Image

Navigate to the project root directory and run the following command to build the Docker image:

```sh
docker build -t object-detection-api .
```

### Running the Application with Docker

Run the following command to start a container from the built image:

```sh
docker run -p 80:80 object-detection-api
```

## API Endpoints

### `POST /detect`

**Description**: Endpoint to get object detection results in JSON format.

**Request Body**:
```json
{
    "image_url": "URL_OF_IMAGE"
}
```

**Response**:
- JSON object containing the object detection results.

### `POST /detect_image`

**Description**: Endpoint to get an image with bounding boxes drawn around detected objects.

**Request Body**:
```json
{
    "image_url": "URL_OF_IMAGE"
}
```

**Response**:
- An image with bounding boxes drawn around detected objects.

## Contributing

Feel free to fork this repository and submit pull requests. For significant changes, please open an issue first to discuss the proposed change.

## License

This project is open source and available under the [MIT License](LICENSE.md).