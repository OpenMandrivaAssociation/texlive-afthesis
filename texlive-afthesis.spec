Name:		texlive-afthesis
Version:	15878
Release:	1
Summary:	Air Force Institute of Technology thesis class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/afthesis
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afthesis.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
