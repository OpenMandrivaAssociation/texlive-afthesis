# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/afthesis
# catalog-date 2008-11-01 22:12:33 +0100
# catalog-license pd
# catalog-version 2.7
Name:		texlive-afthesis
Version:	2.7
Release:	1
Summary:	Air Force Institute of Technology thesis class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/afthesis
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afthesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
LaTeX thesis/dissertation class for US Air Force Institute Of
Technology.

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
%{_texmfdistdir}/bibtex/bst/afthesis/thesnumb.bst
%{_texmfdistdir}/tex/latex/afthesis/afthes10.sty
%{_texmfdistdir}/tex/latex/afthesis/afthes11.sty
%{_texmfdistdir}/tex/latex/afthesis/afthes12.sty
%{_texmfdistdir}/tex/latex/afthesis/afthesis.cls
%{_texmfdistdir}/tex/latex/afthesis/afthesis.sty
%doc %{_texmfdistdir}/doc/latex/afthesis/README
%doc %{_texmfdistdir}/doc/latex/afthesis/thesnumb.doc
%doc %{_texmfdistdir}/doc/latex/afthesis/usethesis.pdf
%doc %{_texmfdistdir}/doc/latex/afthesis/usethesis.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
