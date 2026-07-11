%global tl_name protocol
%global tl_revision 25562

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.13
Release:	%{tl_revision}.1
Summary:	A class for minutes of meetings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/protocol
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/protocol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/protocol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/protocol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The present version of the class supports German meeting minutes
including vote results and action items. The author has ambitions to
internationalise the code, and would welcome support in the work.

