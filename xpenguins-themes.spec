Summary:	Some cartoon themes for xpenguins
Summary(pl):	Motywy do xpenguins
Name:		xpenguins-themes
Version:	1.0
Release:	1
License:	GPL (Lemmings), unknown (the rest)
Group:		X11/Amusements
Source0:	http://xpenguins.seul.org/xpenguins_themes-%{version}.tar.gz
# Source0-md5:	827445e56d6f6216c43303c12ec2bbc1
URL:		http://xpenguins.seul.org/
Requires:	xpenguins >= 1.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Themes for xpenguins: "The Simpsons", "Sonic the Hedgehog" and "Winnie
the Pooh". These are distributed separately from the basic xpenguins
package because they were created from animated gifs found on the web,
and the licensing/copyright situation is unclear.

%description -l pl
Motywy do xpenguins: "The Simpsons", "Sonic the Hedgehog" i "Winnie
the Pooh". Te zosta³y wydzielone z podstawowego pakietu xpenguins,
poniewa¿ zosta³y stworzone z animowanych gifów znalezionych w sieci i
sprawa licencji nie jest jasna.

%prep
%setup -q -n themes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpenguins/themes

cp -ar * $RPM_BUILD_ROOT%{_datadir}/xpenguins/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xpenguins/themes/*
