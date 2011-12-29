# revision 20311
# category Package
# catalog-ctan /macros/latex/contrib/smartref
# catalog-date 2010-11-01 15:44:19 +0100
# catalog-license lppl
# catalog-version 1.9
Name:		texlive-smartref
Version:	1.9
Release:	1
Summary:	Extend LaTeX's \ref capability
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/smartref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smartref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smartref.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the LaTeX labelling system: whenever a
label is set, the values of counters (selected by the user) are
recorded, along with the label. The value of these counters can
be recalled with a command similar to \pageref. The package
also adds commands \s[name]ref (for each counter [name] that
the user has selected); these commands display something only
if the value of the [name] counter is changed from when the
label was set. Many commands are provided to serve as a macro
programming environment for using the extended labels.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/smartref/byname.sty
%{_texmfdistdir}/tex/latex/smartref/smartref.sty
%doc %{_texmfdistdir}/doc/latex/smartref/README
%doc %{_texmfdistdir}/doc/latex/smartref/smartref-doc.pdf
%doc %{_texmfdistdir}/doc/latex/smartref/smartref-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
