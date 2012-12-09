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


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.13-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.13-1
+ Revision: 783074
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.12-2
+ Revision: 755139
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.12-1
+ Revision: 719312
- texlive-protocol
- texlive-protocol
- texlive-protocol
- texlive-protocol

