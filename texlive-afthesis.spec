# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/afthesis
# catalog-date 2008-11-01 22:12:33 +0100
# catalog-license pd
# catalog-version 2.7
Name:		texlive-afthesis
Version:	2.7
Release:	9
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

%description
LaTeX thesis/dissertation class for US Air Force Institute Of
Technology.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.7-2
+ Revision: 749150
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.7-1
+ Revision: 717803
- texlive-afthesis
- texlive-afthesis
- texlive-afthesis
- texlive-afthesis
- texlive-afthesis

