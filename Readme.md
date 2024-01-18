<div align="center">

<img src="https://jeancochrane.com/static/images/blog/pytorch-functional-api/pytorch-logo.png" height="150">


<h3 align="center">THE NEURAL NETWORK GO BRR
</h3>

  <p align="center">
    It's like Tinder but for colors
    <br />
    <br />
    <a href="#contribute">Contribute</a>
    ·
    <a href="https://github.com/ez7mz/text-bg-color-matcher/issues">Report Bug</a>
  </p>

![pytorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) &emsp;
![fastapi](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white) &emsp;
![react](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) &emsp;
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue&Version=3.8.5) &emsp;
</div>




This is a simple project to predict the color of text in case of a given background color. The project is divided into two parts: the frontend and the backend. The frontend is a simple React app that allows the user to select a color and the backend is a simple FastAPI app that uses a pre-trained (Home-made) model to predict the color of the text.


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

### RUN With Docker

run the following command in the root directory:

```sh
docker-compose up
```


### DEMO

![demo](assets/demo.gif)


## Contribute

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**. Feel free to open a pull request or an issue.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

For any questions or suggestions, feel free to contact us:

- Hamza Mesrar - [@ez7mz](https://hmesrar.netlify.app/)
- Yasser Nabouzi - [@NBGamer99](https://www.github.com/NBGamer99)
- Omar Elhariri - [@Ramo](https://github.com/OmarElHrr)
