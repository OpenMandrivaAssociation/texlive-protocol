# revision 25562
# category Package
# catalog-ctan /macros/latex/contrib/protocol
# catalog-date 2012-03-03 18:35:38 +0100
# catalog-license lppl1.3
# catalog-version 1.13
Name:		texlive-protocol
Version:	1.13
Release:	2
Summary:	A class for minutes of meetings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/protocol
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/protocol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/protocol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/protocol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The present version of the class supports German meeting
minutes including vote results and action items. The author has
ambitions to internationalise the code, and would welcome
support in the work.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/protocol/protocol.cls
%doc %{_texmfdistdir}/doc/latex/protocol/README
%doc %{_texmfdistdir}/doc/latex/protocol/protest.tex
%doc %{_texmfdistdir}/doc/latex/protocol/protocol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/protocol/protocol.dtx
%doc %{_texmfdistdir}/source/latex/protocol/protocol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
