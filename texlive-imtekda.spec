%global tl_name imtekda
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	IMTEK thesis class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/imtekda
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class permits typesetting of diploma, bachelor's and master's theses
for the Institute of Microsystem Technology (IMTEK) at the University of
Freiburg (Germany). The class is based on the KOMA-Script class scrbook.
Included in the documentation is a large collection of useful tips for
typesetting theses and a list of recommended packages.

