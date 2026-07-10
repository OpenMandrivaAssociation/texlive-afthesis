%global tl_name afthesis
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7
Release:	%{tl_revision}.1
Summary:	Air Force Institute of Technology thesis class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/afthesis
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/afthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/afthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX thesis/dissertation class for US Air Force Institute Of
Technology.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/afthesis
%dir %{_datadir}/texmf-dist/doc/latex/afthesis
%dir %{_datadir}/texmf-dist/tex/latex/afthesis
%{_datadir}/texmf-dist/bibtex/bst/afthesis/thesnumb.bst
%doc %{_datadir}/texmf-dist/doc/latex/afthesis/README
%doc %{_datadir}/texmf-dist/doc/latex/afthesis/thesnumb.doc
%doc %{_datadir}/texmf-dist/doc/latex/afthesis/usethesis.pdf
%doc %{_datadir}/texmf-dist/doc/latex/afthesis/usethesis.tex
%{_datadir}/texmf-dist/tex/latex/afthesis/afthes10.sty
%{_datadir}/texmf-dist/tex/latex/afthesis/afthes11.sty
%{_datadir}/texmf-dist/tex/latex/afthesis/afthes12.sty
%{_datadir}/texmf-dist/tex/latex/afthesis/afthesis.cls
%{_datadir}/texmf-dist/tex/latex/afthesis/afthesis.sty
