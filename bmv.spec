Summary:	Simple viewer of images (pbm-raw) and front end for GhostScript based on SVGAlib 
Summary(pl):	Prosta przegl±darka plików graficznych (pbm-raw) oraz frontend do GhostScriptu bazuj±cy na SVGAlib
Name:		bmv
Version:	1.2
Release:	2
Vendor:		Jan Kybic <kybic@earn.cvut.cz>
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
License:	GPL
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/graphics/viewers/svga/%{name}-%{version}.tgz
Patch0:		%{name}-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	svgalib-devel
Requires:	ghostscript

%description
BMV is a front end for GhostScript. Using BMV you can now preview your
PostScript files comfortably. It uses SVGAlib and it is intended for
Linux users who cannot run X. It is particulary suitable for
previewing PS files from dvips. It is small and fast.

%description -l pl
Przegl±darka BMV jest fontendem dla GhostScriptu. Korzystaj±c z niej
mo¿esz ogl±daæ pliki PostScript poprzez bibliotekê svgalib - bez X.
Jest ma³a i szybka.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	CC="%{__cc} -DCOLOUR" \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install bmv $RPM_BUILD_ROOT%{_bindir}
gzip -9nf bmv.{CHANGES,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/bmv
