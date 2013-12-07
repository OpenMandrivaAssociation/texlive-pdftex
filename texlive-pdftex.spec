# revision 32132
# category TLCore
# catalog-ctan /systems/pdftex
# catalog-date 2011-11-09 15:33:34 +0100
# catalog-license gpl
# catalog-version 1.40.11
Name:		texlive-pdftex
Version:	1.40.11
Release:	19
Summary:	A TeX extension for direct creation of PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/pdftex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex.doc.tar.xz
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
%{_texmfdistdir}/fonts/map/pdftex/updmap/pdftex.map
%{_texmfdistdir}/fonts/map/pdftex/updmap/pdftex_dl14.map
%{_texmfdistdir}/fonts/map/pdftex/updmap/pdftex_ndl14.map
%{_texmfdistdir}/scripts/simpdftex/simpdftex
%{_texmfdistdir}/tex/generic/config/pdftex-dvi.tex
%{_texmfdistdir}/tex/generic/config/pdftexconfig.tex
%{_texmfdistdir}/tex/generic/pdftex/glyphtounicode.tex
%_texmf_fmtutil_d/pdftex
%doc %{_mandir}/man1/pdfetex.1*
%doc %{_texmfdistdir}/doc/man/man1/pdfetex.man1.pdf
%doc %{_mandir}/man1/pdftex.1*
%doc %{_texmfdistdir}/doc/man/man1/pdftex.man1.pdf
%doc %{_texmfdistdir}/doc/pdftex/Announcement-1.40.2
%doc %{_texmfdistdir}/doc/pdftex/NEWS
%doc %{_texmfdistdir}/doc/pdftex/README
%doc %{_texmfdistdir}/doc/pdftex/manual/ChangeLog
%doc %{_texmfdistdir}/doc/pdftex/manual/Makefile
%doc %{_texmfdistdir}/doc/pdftex/manual/README
%doc %{_texmfdistdir}/doc/pdftex/manual/makefiles.cmd
%doc %{_texmfdistdir}/doc/pdftex/manual/pdftex-a.pdf
%doc %{_texmfdistdir}/doc/pdftex/manual/pdftex-i.tex
%doc %{_texmfdistdir}/doc/pdftex/manual/pdftex-l.pdf
%doc %{_texmfdistdir}/doc/pdftex/manual/pdftex-s.pdf
%doc %{_texmfdistdir}/doc/pdftex/manual/pdftex-syntax.txt
%doc %{_texmfdistdir}/doc/pdftex/manual/pdftex-t.tex
%doc %{_texmfdistdir}/doc/pdftex/manual/pdftex-t.txt
%doc %{_texmfdistdir}/doc/pdftex/manual/pdftex-w.tex
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/cmr10.103
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/obj.dat
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/pdfcolor.tex
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/pic.eps
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/pic.jpg
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/pic.mps
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/pic.pdf
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/pic.png
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/pic16.png
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/rgb.icc
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/samplepdf.0
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/samplepdf.1
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/samplepdf.tex
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/supp-mis.tex
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/supp-pdf.tex
%doc %{_texmfdistdir}/doc/pdftex/manual/samplepdf/tmp.pdf
%doc %{_texmfdistdir}/doc/pdftex/manual/syntaxform.awk
%doc %{_texmfdistdir}/doc/pdftex/pdftex-pdfkeys/Makefile
%doc %{_texmfdistdir}/doc/pdftex/pdftex-pdfkeys/fdl.tex
%doc %{_texmfdistdir}/doc/pdftex/pdftex-pdfkeys/pdftex-pdfkeys.bbl
%doc %{_texmfdistdir}/doc/pdftex/pdftex-pdfkeys/pdftex-pdfkeys.pdf
%doc %{_texmfdistdir}/doc/pdftex/pdftex-pdfkeys/pdftex-pdfkeys.tex
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/abbr.tex
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/efcode.tex
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/il2.etx
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/il2.mtx
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/il2protcode.tex
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/mktextfm
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/mktextfm.ext
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/mktfm8z
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/protcode.tex
%doc %{_texmfdistdir}/doc/pdftex/thanh/ext/ufntinst.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

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
