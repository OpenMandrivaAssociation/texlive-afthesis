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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX thesis/dissertation class for US Air Force Institute Of
Technology.

