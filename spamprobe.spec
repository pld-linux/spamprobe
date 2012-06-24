Summary:	SpamProbe - fast bayesian spam filter
Summary(pl):	SpamProbe - szybki bayesowski filtr antyspamowy
Name:		spamprobe
Version:	1.1x7
Release:	1
License:	QPL
Group:		Applications
Source0:	http://dl.sourceforge.net/spamprobe/%{name}-%{version}.tar.gz
# Source0-md5:	e7e0d97c08fb96c4b1733aea4b2ddd85
URL:		http://spamprobe.sourceforge.net/
BuildRequires:	db-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast, intelligent, automatic spam detector using Paul Graham style
Bayesian analysis of word counts in spam and non-spam emails.
Filtering adapts to personal tastes automatically. No manual rule
creation required. Intended for use with procmail, maild.

%description -l pl
Szybki, inteligentny, automatyczny wykrywacz spamu u�ywaj�cy odmiany
Paula Grahama bayesowskiej analizy liczby s��w w listach b�d�cych i
nie b�d�cych spamem. Filtrowanie automatycznie dostosowuje si� do
osobistych gust�w. Nie jest wymagane r�czne tworzenie regu�. Program
mo�e by� u�ywany z procmailem lub maild.

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
