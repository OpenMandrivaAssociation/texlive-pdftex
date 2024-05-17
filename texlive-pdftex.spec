Name:		texlive-pdftex
Version:	70501
Release:	1
Summary:	A TeX extension for direct creation of PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/pdftex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex.doc.r%{version}.tar.xz
Source2:	https://raw.githubusercontent.com/latex3/tex-ini-files/main/pdftexconfig.tex
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-pdftex.bin

%description
An extension of TeX which can be configured to directly
generate PDF documents instead of DVI. All current free TeX
distributionsm including TeX live, MacTeX and MiKTeX include
pdfTeX (Plain TeX) and pdfLaTeX (LaTeX). ConTeXt was designed
around use of pdfTeX (though it is now migrating towards
LuaTeX).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	rm -fr %{_texmfvardir}/fonts/map/pdftex
	rm -fr %{_texmfvardir}/web2c/pdftex
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/dummy-space
%{_texmfdistdir}/fonts/tfm/public/pdftex
%{_texmfdistdir}/fonts/type1/public/pdftex
%{_texmfdistdir}/scripts/simpdftex
%{_texmfdistdir}/tex/generic/config/*
%{_texmfdistdir}/tex/generic/pdftex
%_texmf_fmtutil_d/pdftex
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/pdftex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/pdftex <<EOF
#
# from pdftex:
pdftex pdftex language.def -translate-file=cp227.tcx *pdfetex.ini
etex pdftex language.def -translate-file=cp227.tcx *etex.ini
pdfetex pdftex language.def -translate-file=cp227.tcx *pdfetex.ini
EOF
cp %{S:2} %{buildroot}%{_texmfdistdir}/tex/generic/config/
