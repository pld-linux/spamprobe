Summary:	SpamProbe - fast bayesian spam filter
Summary(pl.UTF-8):   SpamProbe - szybki bayesowski filtr antyspamowy
Name:		spamprobe
Version:	1.4b
Release:	1
License:	QPL
Group:		Applications
Source0:	http://dl.sourceforge.net/spamprobe/%{name}-%{version}.tar.gz
# Source0-md5:	735a5ef084ca09a39fb88a0334fcc68e
URL:		http://spamprobe.sourceforge.net/
BuildRequires:	db-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast, intelligent, automatic spam detector using Paul Graham style
Bayesian analysis of word counts in spam and non-spam emails.
Filtering adapts to personal tastes automatically. No manual rule
creation required. Intended for use with procmail, maild.

%description -l pl.UTF-8
Szybki, inteligentny, automatyczny wykrywacz spamu używający odmiany
Paula Grahama bayesowskiej analizy liczby słów w listach będących i
nie będących spamem. Filtrowanie automatycznie dostosowuje się do
osobistych gustów. Nie jest wymagane ręczne tworzenie reguł. Program
może być używany z procmailem lub maild.

%prep
%setup -q

%build
%configure \
	--enable-default-8bit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
