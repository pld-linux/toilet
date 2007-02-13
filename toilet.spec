Summary:	TOIlet - free replacement for FIGlet utility
Summary(pl.UTF-8):	TOIlet - wolnodostępny zamiennik narzędzia FIGlet
Name:		toilet
Version:	0.1
Release:	2
License:	WTFPL
Group:		Applications/Graphics
Source0:	http://libcaca.zoy.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	7d26ca36c83eeca2f0c285872624c2c8
Patch0:		%{name}-make.patch
URL:		http://libcaca.zoy.org/toilet.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libcaca-devel >= 0.99-0.beta10
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	libcaca >= 0.99-0.beta10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The TOIlet project attempts to create a free replacement for the
FIGlet utility. TOIlet stands for "The Other Implementation's
letters", coined after FIGlet's "Frank, Ian and Glen's letters".
TOIlet is in its very early development phase. It uses the powerful
libcucul library to achieve various text-based effects. TOIlet
implements or plans to implement the following features:

 - The ability to load FIGlet fonts
 - Support for Unicode input and output
 - Support for colour output
 - Support for various output formats: HTML, IRC, ANSI...

%description -l pl.UTF-8
Projekt TOIlet ma na celu stworzenie wolnodostępnego zamiennika
narzędzia FIGlet. TOIlet jest skrótem od "The Other Implementation's
letters" (litery innej implementacji), na wzór FIGletowego "Frank,
Ian and Glen's letters" (litery Franka, Iana i Glena). TOIlet jest we
wczesnej fazie rozwoju. Do różnych efektów tekstowych wykorzystuje
potężną bibliotekę libcucul. TOIlet ma lub ma mieć następujące
możliwości:

 - wczytywanie fontów FIGleta
 - obsługę wejścia i wyjścia w Unicode
 - obsługę kolorowego wyjścia
 - obsługę różnych formatów wyjściowych: HTML, IRC, ANSI...

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/toilet
# XXX: shared with figlet?
%dir %{_datadir}/figlet
%{_datadir}/figlet/*.tlf
%{_mandir}/man1/toilet.1*
