Summary:	Simple viewer of images (pbm-raw) and front end for GhostScript based on SVGAlib
Summary(pl.UTF-8):   Prosta przeglądarka plików graficznych (pbm-raw) oraz frontend do GhostScriptu bazujący na SVGAlib
Name:		bmv
Version:	1.2
Release:	3
Vendor:		Jan Kybic <kybic@earn.cvut.cz>
Group:		Applications/Publishing
License:	GPL
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/graphics/viewers/svga/%{name}-%{version}.tgz
# Source0-md5:	40c881800edac6b1d2ce75ea8da6e6b4
Patch0:		%{name}-glibc.patch
BuildRequires:	svgalib-devel
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BMV is a front end for GhostScript. Using BMV you can now preview
your PostScript files comfortably. It uses SVGAlib and it is intended
for Linux users who cannot run X. It is particularly suitable for
previewing PS files from dvips. It is small and fast.

%description -l pl.UTF-8
Przeglądarka BMV jest frontendem dla GhostScriptu. Korzystając z niej
możesz oglądać pliki PostScript poprzez bibliotekę svgalib - bez X.
Jest mała i szybka.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc} -DCOLOUR" \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bmv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc bmv.{CHANGES,README}
%attr(755,root,root) %{_bindir}/bmv
