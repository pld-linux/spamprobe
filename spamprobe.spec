Summary:	SpamProbe - fast bayesian spam filter
Name:		spamprobe
Version:	0.8b
Release:	1
License:	QPL
Group:		Applications
Source0:	http://dl.sourceforge.net/sourceforge/spamprobe/%{name}-%{version}.tar.gz
URL:		http://spamprobe.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast, intelligent, automatic spam detector using Paul Graham style
Bayesian analysis of word counts in spam and non-spam emails.
Filtering adapts to personal tastes automatically. No manual rule
creation required. Intended for use with procmail, maild

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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
