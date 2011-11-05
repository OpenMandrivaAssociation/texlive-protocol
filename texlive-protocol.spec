# revision 24281
# category Package
# catalog-ctan /macros/latex/contrib/protocol
# catalog-date 2011-10-13 09:47:13 +0200
# catalog-license lppl1.3
# catalog-version 1.12
Name:		texlive-protocol
Version:	1.12
Release:	1
Summary:	A class for typesetting minutes of meetings
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The present version of the package is useful for German
documents; the author has ambitions to internationalise the
code, and would welcome support in the work.

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
%{_texmfdistdir}/tex/latex/protocol/protocol.cls
%doc %{_texmfdistdir}/doc/latex/protocol/README
%doc %{_texmfdistdir}/doc/latex/protocol/protest.tex
%doc %{_texmfdistdir}/doc/latex/protocol/protocol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/protocol/protocol.dtx
%doc %{_texmfdistdir}/source/latex/protocol/protocol.ins
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
