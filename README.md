<div align="center">
  
![Banner](assets/banner.gif)

# WORD-ART

![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logoColor=white)![Pygame](https://img.shields.io/badge/pygame-2.0+-81aa00?style=for-the-badge&logo=python&logoColor=white)![Requests](https://img.shields.io/badge/Requests-2.28+-2496ed?style=for-the-badge&logoColor=white)![Colorama](https://img.shields.io/badge/Colorama-0.4+-4EAA25?style=for-the-badge&logoColor=white)

</div>

### Word art is a program made to show images using provided text and image files.
---
<details>
<summary><strong>Table of Contents</summary>

1. [Features](#features)
2. [How to Install](#how-to-install)
    - [Pip Method](#pip-method-recomended)
    - [Local install](#local-install)
3. [Usage](#usage)
    - [Examples](#examples)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)
</u>
</details>

# Features
- Real-time image rendering and loading
- Support for PNG, JPG, BMP, GIF and more formats
- Customizable text overlays
- Smooth animations with pygame
- Simple pip installation

# How to install
To install it, you can mainly use 2 ways, which are listed below.

The recommended method is via pip, which handles all dependencies automatically. Alternatively, if you prefer to work with the source code or contribute to the project, you can clone the repository and install it locally.

Choose the method that best fits your needs:

## Pip method (Recomended)

```bash
pip install word-art
```

## Local install

```bash
git clone https://github.com/seu-username/word-art.git
cd word-art
pip install -e .
```
This method is useful if you want to modify the code or contribute to the project.

## Usage

### Basic usage

Run the program with default settings (uses included Miku image and "MIKU" text):

```bash
word-art
```

### With custom image

```bash
word-art -i path/to/your/image
```

### With custom text

```bash
word-art -t "YOUR TEXT HERE"
```

### With both image and text

```bash
word-art -i path/to/image -t "YOUT TEXT HERE"
```

### View help

```bash
word-art --help
```