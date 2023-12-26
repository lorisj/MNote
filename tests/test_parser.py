import unittest
from mnote import get_parser

class TestParser(unittest.TestCase):
    def test_basic_parsing(self):
        parser = get_parser()
        content = r"""

# introduction

This note covers basic definitions and results of category theory. It mostly follows \cite{riehl_2016}, but also contains notes from \cite{simmons_2011},
as well as special topics from \cite{nourani_2014}.

%def(category)
    A category $C$ consists of
    %item
        %i A class $\Ob(C)$ consisting of objects
        %i A class $\Hom(C)$ of morphisms.
        
        %def(morphism)
            A morphism is any object that has a source object $A \in \Ob(C)$ and a target $B \in \Ob(C)$. Morphisms are sometimes called arrows. 
            
            If $f$ is a morphism with source $A \in \Ob(C)$ and target $B \in \Ob(C)$, then this is usually written as $f:A \to B$. 
        %i A binary operation $\circ : M \to M$, called composition, which satisfies:
        %enum
            %i $\circ$ is associative
            %i $\Hom(A)$ has an idenity morphism for every $X \in \Ob(C)$
            %def(identity_morphism)[morphism]
                For every objecrmt $X \in \Ob(C)$, there exists an identity morphism $\id_X : X \to X$, such that for every morphism $f:X \to Y$:
                %neq
                    f \circ \id_X = f = \id_Y \circ f  
                Or as a diagram:
                %ccd
                    X \arrow[r, "f"] \arrow["\id_X"', loop, distance=2em, in=215, out=145] & Y \arrow["\id_Y"', loop, distance=2em, in=35, out=325]
%exp(common_categories)[category]
    Some common categories are:
    %item
        %i $\cat{Set}$ has objects consisting of all sets, and morphisms consisting of all functions between sets.
        %i $\cat{Top}$ has objects consisting of all topological spaces, and morphisms consisting of all continuous functions between these spaces.
        %i $\cat{Group}$ has objects consisting of all groups, and morphisms consisting of all homomorphisms between groups.
        %i $\cat{Mod}_R$ for a fixed ring $R$ (with identity),  is the category of left $R$-modules and $R$-module homomorphisms.
        If $R$ is a field, then we call this   
        %i $\cat{Graph}$ has objects consisting of all graphs, and morphisms consisting of graph homomorphisms.
        %i 
        $\cat{Model}_T$ for any language $\mathcal L$ and first order $\mathcal L$-theory $T$ is a category with objects as 
        $[\mathcal L, T]$-structures (i.e. $\mathcal L$-structures $\mathcal M$ that model $T$, so $\mathcal M \models T$).

%res(unique_identity)[category]
    Identity morphisms in a category are unique.
    %dl
    %pf
        Consider an object $A$ with two identity morphisms $f, g : A \to A$. Then note $f = f \circ g = g$. 
        Thus $f = g$ and identity morphisms are unique.

%def(hom_class)[category]
    Let $C$ be a category. Let $A,B \in \ob(C)$ be two objects. Denote $C(A,B) = \{ f \in \Hom(C)  |  f : A \to B\}$, 
    i.e. the class containing all morphisms with source $A$ and target $B$. This is called the Hom-class, and is sometimes written as $\Hom(A,B)$.

%def(isomorphism)[morphism]
    A morphism $f:X\to Y$ is an isomorphism if and only if it is invertible, i.e there exists some $f^{-1}:Y \to X$ such that:
    %neq
        f^{-1}\circ f &= \id_X\\
        f\circ f^{-1} &= \id_Y
    %ccd
        X \arrow[r, "f", bend left] \arrow["\id_X"', loop, distance=2em, in=215, out=145] & Y \arrow[l, "\exists f^{-1}", dotted, bend left] \arrow["\id_Y"', loop, distance=2em, in=35, out=325]
    
    We then say two objects $X,Y$ are isomorphic.
    

%def(endomorphism)[morphism]
    An endomorphism is a morphism whose domain is the same as the codomain, i.e. $f:X \to X$ is an endomorphism.
    a set of all endomorphisms of an object $X$ is denoted $\End(X)$.

%def(automorphism)[morphism]
    A automorphism is a morphism which is both an isomorphism and an endomorphism.


%exp(category_isomorphisms)[isomorphism]
    Note that morphisms are technically binary relations, (if they arent a set then they can be though of as a relation of a class) 
    but this sometimes is not the right way of looking at them.
    This is true in the following example: 
    %enum
        %i For any ring $R$, define the category $C$:
        %item
            %i $\Ob(C) \eqdef \Z_+$
            %i $\Hom(C)\eqdef$ the set of $C(n,m)= R^{n \times m}$, i.e. all $n$ by $m$ matrices.
            %i $\circ \eqdef$ matrix multiplication
        To check this forms a category, note that:
        %item
            %i $\circ$ is associative because matrix multiplication is associative
            %i
            Every object has an identity, namely for any $n \in \Ob(C)$ there is the $n\times n$ identity matrix $I_n$, which has the property that
            for any morphism $f:m \to n$ (i.e. for every $n \times m$ matrix) we have $I_n \circ f = f \circ I_m = f$.
        
        
        Thus $C$ is a category. 
        
        Note that while technically $\Hom(C)$ consists of relations, (i.e. you have a relation for each $n\times m$ matrix)
        it is not productive to think of morphisms this way, so you should rather think of morphisms as some new object, i.e. an arrow.
        %i
        For any monoid $\mathcal M = (M,*)$, define the category $C=\cat{B}_M$:
        %item
            %i $\Ob(C)$ consists of some single object (could be anything, let's call it $o$)
            %i For every monoid element $m \in M$, define a morphism $f_{m}: o \to o$.
            %i Define $\circ$ as the binary operation $f_m \circ f_n \mapsto f_{m * n}$.
        
        Note that monoids have identity elements and associative binary operation.

%def(small_category)[category]
    A category is small if both $\Ob(C)$ and $\Hom(C)$ are sets."""
        # Parse the content
        parsed_tree = parser.parse(content)
        # Add assertions here to verify the parsed tree

if __name__ == '__main__':
    unittest.main()