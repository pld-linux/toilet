Summary:	TOIlet - free replacement for FIGlet utility
Summary(pl):	TOIlet - wolnodost�pny zamiennik narz�dzia FIGlet
Name:		toilet
Version:	0.1
Release:	1
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

%description -l pl
Projekt TOIlet ma na celu stworzenie wolnodost�pnego zamiennika
narz�dzia FIGlet. TOIlet jest skr�tem od "The Other Implementation's
letters" (litery innej implementacji), na wz�r FIGletowego "Frank,
Ian and Glen's letters" (litery Franka, Iana i Glena). TOIlet jest we
wczesnej fazie rozwoju. Do r�nych efekt�w tekstowych wykorzystuje
pot�n� bibliotek� libcucul. TOIlet ma lub ma mie� nast�puj�ce
mo�liwo�ci:

 - wczytywanie font�w FIGleta
 - obs�ug� wej�cia i wyj�cia w Unicode
 - obs�ug� kolorowego wyj�cia
 - obs�ug� r�nych format�w wyj�ciowych: HTML, IRC, ANSI...

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
