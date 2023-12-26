# MNote Package

The MNote package is a Python tool for parsing and interpreting .mnote files, a custom LaTeX-inspired language, and converting them into standard LaTeX format. The purpose of this language and tool is twofold:
1) It makes it faster to write and edit structured math documents that have many theorems, definitions and results, eliminating the need for start and end delimiters (i.e. `\begin{definiton}{...} \end{definition}`)  by replacing them with indents 
2) It allows for python to understand the structure of a LaTeX document, allowing for applications to be built that use the structure of a document, such as a graph based note taking app
## Installation

To install the MNote package, follow these steps:

```bash

# Clone the repository
git clone https://github.com/lorisj/MNote.git

# Navigate to the package directory
cd MNote

# Install the package
pip install .
```
## Usage
Writing .mnote Files

.mnote files are a faster way to write structured documents with a syntax that is simpler than LaTeX but can be seamlessly converted into LaTeX format. Here is an example of a basic LaTeX file:


```latex
\section{Introduction}

  This note covers basic definitions and results of category theory.
  \begin{definition}{/category}{category}
    A category $C$ consists of
    \begin{itemize}
      \item A class $\Ob(C)$ consisting of objects
      \item A class $\Hom(C)$ of morphisms.
    \end{itemize}
    \begin{example}{category/common categories}{common categories}
    Some common categories are:
    \begin{itemize}
      \item $\cat{Set}$ has objects consisting of all sets, and morphisms consisting of all functions between sets.
      \item $\cat{Top}$ has objects consisting of all topological spaces, and morphisms consisting of all continuous functions between these spaces.
    \end{itemize}
  \end{definition}
```

and its corresponding .mnote file:

```latex
# introduction

This note covers basic definitions and results of category theory.
%def(category)
    A category $C$ consists of
    %item
        %i A class $\Ob(C)$ consisting of objects
        %i A class $\Hom(C)$ of morphisms.
  %exp(common categories)
    %enum
      %i $\cat{Set}$ has objects consisting of all sets, and morphisms consisting of all functions between sets.
      %i $\cat{Top}$ has objects consisting of all topological spaces, and morphisms consisting of all continuous functions between these spaces.
```


## Using the MNote Package

To convert .mnote files to LaTeX, use the following command:

```bash

python -m mnote yourfile.mnote
```
This will parse the .mnote file and output the corresponding LaTeX code to the terminal.
