# revision 17667
# category Package
# catalog-ctan /macros/latex/contrib/imtekda
# catalog-date 2010-04-03 16:55:02 +0200
# catalog-license lppl
# catalog-version 1.7
Name:		texlive-imtekda
Version:	1.7
Release:	1
Summary:	IMTEK thesis class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/imtekda
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imtekda.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class permits typesetting of diploma, bachelor's and
master's theses for the Institute of Microsystem Technology
(IMTEK) at the University of Freiburg (Germany). The class is
based on the KOMA-Script class scrbook. Included in the
documentation is a large collection of useful tips for
typesetting theses and a list of recommended packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
