Summary:	Universal graphical front-end for command line programs
Summary(pl):	Uniwersalna graficzna nak�adka na programy dzia�aj�ce z linii polece�
Name:		kaptain
Version:	0.72
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/kaptain/%{name}-%{version}.tar.gz
# Source0-md5:	2a3a9d6acaa74a517a088a3aba1b9696
URL:		http://kaptain.sourceforge.net/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kaptain is a universal graphical front-end. It was originally
developed in order to provide a simple and efficient tool for creating
dialog-based interface for command line programs. Now, its
communication features allow it to serve the graphical user interface
of a program without directly using a graphical library, such as GTK
or Qt.

%description -l pl
Kaptain jest uniwersaln� nak�adk� graficzn�. Zosta� stwrzony jako
proste i efektywne narz�dzie do tworzenia interfejsu na programy
dzia�aj�ce z linii polece�. Teraz, jego mo�liwo�ci komunikacyjne
pozwalaj� zapewni� interfejs graficzny programu bez bezpo�redniego
korzystania z bibliotek graficznych.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_infodir}/*
