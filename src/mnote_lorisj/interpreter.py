from lark.visitors import Interpreter
from .utils import title_case, escape_underscore, format_name





class LaTeXInterpreter(Interpreter):
    def ind_println(self, string_in):
        print('\t' * self.indent_level, end='')
        print(string_in)
        
    def ind_print(self, string_in):
        print('\t' * self.indent_level, end='')
        print(string_in, end='')
    
    def tex_block_print(self, type, tree):
        self.ind_println("\\begin{" + type + "}")
        self.indent_level += 1
        for child in tree.children:
            self.visit(child)
        self.indent_level -= 1
        self.ind_println("\\end{" + type + "}")


    def block_reference(self, tree): # TODO: make sure this communicates with server to get block text.
        print("\\refdef{" + tree.children[0] + "}", end="") # TODO: Change this to either link. Local reference with %lref
    
    # TODO: add bib_reference as well
    
    def __init__(self, author_name = "", document_name = ""):
        super().__init__()
        self.indent_level = 0
        self.latex_start_text = r"""
\documentclass[12pt]{article}
\usepackage{notespkg}
\usepackage{screenread} %Puts every document on one page comment out if not needed.
%\addbibresource{bibliography.bib} % Rename bibliography.bib to your current .bib file, in the same directory. 
\usepackage{alltopics}
\title{""" +  document_name + r"""} 
\author{""" + author_name + r"""}
\begin{document}
\maketitle

%\tableofcontents
"""
        self.latex_end_text = r"""\end{document}"""


    def start(self, tree):
        for child in tree.children:
            self.visit(child)
        print() # Ensure we end with a newline

    def content(self, tree):
        for child in tree.children:
            self.visit(child)
           

    def block(self, tree):
        for child in tree.children:
            self.visit(child)

    def result(self, tree):
        self.boxed_object("result", tree)
    
    def claim(self, tree):
        self.boxed_object("claim", tree)
    
    def example(self, tree):
        self.boxed_object("example", tree)

    def definition(self, tree):
        self.boxed_object("definition", tree)
    
    def text(self, tree):
        for child in tree.children:
            self.visit(child)
    def dline(self, tree):
        self.ind_println("\\dline")
    def newpage(self, tree):
        self.ind_println("\\newpage")
    def proof(self, tree):
        self.tex_block_print("proof", tree)

    def line(self, tree):
        self.ind_print("")
        for child in tree.children:
            if isinstance(child, str):
                print(child, end="")
            else: # Handle inline commands,
                self.visit(child)
        print() # get newline at end.

    def subtitle(self, tree):
        self.ind_println("\\subtitle{" + format_name(tree.children[0]) + "}")
    def todoline(self, tree):
        self.ind_println("\\todo[inline]{" + tree.children[0] + "}")

    def image(self, tree):
        file_path = str(tree.children[0])#Path(str(tree.children[0].children[0])) # TODO: Figure out a way to have a database of images, and a way to upload images.
    
        self.ind_println("\\begin{figure}[H]")
        self.indent_level += 1
        self.ind_println("\\centering")
        if(file_path[-4:] == ".svg"):
            self.ind_println("\\includesvg{images/" + file_path +"}")
        else:
            self.ind_println("\\includegraphics{images/" + file_path +"}")
        self.ind_println("\\caption{" + format_name(file_path[0:-4]) + "}")
        self.indent_level -= 1
        self.ind_println("\\end{figure}")
        
    def section_name(self, tree):
        number_pound_signs = tree.children[0].count("#")
        name_without_pound_signs = format_name(tree.children[0].replace("#", "").strip())
        if number_pound_signs == 0:
            self.ind_println("\\section{" + name_without_pound_signs + "}")
        elif number_pound_signs == 1:
            self.ind_println("\\subsection{" + name_without_pound_signs + "}")
        else: # raise error, too many pound signs
            raise ValueError("Too many pound signs in section name")
            
    def empty_line(self, tree):
        self.ind_println("")

    def tex_block(self, tree):
        for child in tree.children:
            self.visit(child)
        
    def enumerate(self, tree):
        self.tex_block_print("enumerate", tree)
    
    def tikcd(self, tree):
        self.tex_block_print("tikzcd", tree)

    def tikcd_center(self, tree):
        self.ind_println("\\begin{center}")
        self.indent_level += 1
        self.tex_block_print("tikzcd", tree)
        self.indent_level -= 1
        self.ind_println("\\end{center}")

    def itemize(self, tree):
        self.tex_block_print("itemize", tree)

    def item(self, tree):
        self.ind_println("\\item")
        for child in tree.children:
            self.visit(child)

    def nice_equation(self, tree):
        self.tex_block_print("niceeq", tree)

    def equation(self, tree):
        self.tex_block_print("align", tree) # we call equations align, as this allows multi-line equations

    def boxed_object(self, type, tree):
        content_list = tree.children[1:]
        tag_name = tree.children[0]
        name = ""
        if tree.children[1].data == "blockname_array":
            content_list = tree.children[2:]
            context_array = [f"{str(child)}" for child in tree.children[1].children]
            name = escape_underscore(f"{str(context_array)}/ \\\\")
        else:
            name += "/"
        name+= escape_underscore(tag_name)#format_name(tag_name)

        self.ind_println("\\begin{" + type + "}{" + name.replace("'", "") + "}{" + escape_underscore(tag_name) + "}")
        self.indent_level += 1
        for child in content_list:
            self.visit(child)
        self.indent_level -= 1
        self.ind_println("\\end{" + type + "}")



class MNoteInterpreter(Interpreter):
    
    def __init__(self, author_name):
        self.author_name = author_name
        self.string_output = ""
        super().__init__()
        self.indent_level = 0
        
    def start(self, tree):
        for child in tree.children:
            self.visit(child)
        self.string_output += "\n" # Ensure we end with a newline