<div align="center">

<img src="https://jeancochrane.com/static/images/blog/pytorch-functional-api/pytorch-logo.png" height="150">


<h3 align="center">THE NEURAL NETWORK GO BRR
</h3>

  <p align="center">
    Not recommended for dogs 🐶
    <br />
    <br />
    <a href="#contribute">Contribute</a>
    ·
    <a href="">Report Bug</a>
  </p>

![pytorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) &emsp;
![fastapi](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white) &emsp;
![react](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) &emsp;
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue&Version=3.8.5) &emsp;
</div>




This is a simple project to predict the color of text in case of a given background color. The project is divided into two parts: the frontend and the backend. The frontend is a simple React app that allows the user to select a color and the backend is a simple FastAPI app that uses a pre-trained model to predict the color of the text.


## Getting Started

### Prerequisites

* Python 3.8.5
* Node 14.17.0

### Installation

1. Clone the repo
   ```sh
   git clone
   ```
2. It is recommended to use a virtual environment
   ```sh
   python -m venv venv
   ```
2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Install Node packages
   ```sh
   pnpm install or npm install
   ```


## Usage

### Frontend

To run the frontend, run the following command in the `frontend` directory:
```sh
pnpm start or npm start
```

### Backend

To run the backend, run the following command in the `backend` directory:

```sh
uvicorn main:app --reload
```

### RUN USING DOCKER

run the following command in the root directory:

```sh
docker-compose up
```


### DEMO

![demo](assets/demo.gif)


## Contribute

For any suggestions or issues, please open an issue or contact us at [@NBGamer99](https://github.com/NBGamer99/), [@Hmesrar](mailto:hmesrar48@gmail.com), or[@ramo](https://github.com/OmarElHrr)