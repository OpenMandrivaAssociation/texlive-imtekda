Name:		texlive-imtekda
Version:	17667
Release:	2
Summary:	IMTEK thesis class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/imtekda
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class permits typesetting of diploma, bachelor's and
master's theses for the Institute of Microsystem Technology
(IMTEK) at the University of Freiburg (Germany). The class is
based on the KOMA-Script class scrbook. Included in the
documentation is a large collection of useful tips for
typesetting theses and a list of recommended packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/imtekda/IMTEKda.cls
%doc %{_texmfdistdir}/doc/latex/imtekda/IMTEKda.pdf
%doc %{_texmfdistdir}/doc/latex/imtekda/README
%doc %{_texmfdistdir}/doc/latex/imtekda/diplarb.bib
%doc %{_texmfdistdir}/doc/latex/imtekda/diplarb.tex
%doc %{_texmfdistdir}/doc/latex/imtekda/figures/bild.eps
%doc %{_texmfdistdir}/doc/latex/imtekda/figures/bild.pdf
#- source
%doc %{_texmfdistdir}/source/latex/imtekda/IMTEKda.dtx
%doc %{_texmfdistdir}/source/latex/imtekda/IMTEKda.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
