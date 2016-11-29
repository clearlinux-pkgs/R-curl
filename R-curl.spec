#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-curl
Version  : 2.3
Release  : 31
URL      : http://cran.r-project.org/src/contrib/curl_2.3.tar.gz
Source0  : http://cran.r-project.org/src/contrib/curl_2.3.tar.gz
Summary  : A Modern and Flexible Web Client for R
Group    : Development/Tools
License  : MIT
Requires: R-curl-lib
BuildRequires : R-knitr
BuildRequires : R-magrittr
BuildRequires : R-markdown
BuildRequires : R-testthat
BuildRequires : clr-R-helpers
BuildRequires : curl-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-curl package.
Group: Libraries

%description lib
lib components for the R-curl package.


%prep
%setup -q -c -n curl

%build
export LANG=C

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library curl
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library curl || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/curl/DESCRIPTION
/usr/lib64/R/library/curl/INDEX
/usr/lib64/R/library/curl/LICENSE
/usr/lib64/R/library/curl/Meta/Rd.rds
/usr/lib64/R/library/curl/Meta/data.rds
/usr/lib64/R/library/curl/Meta/hsearch.rds
/usr/lib64/R/library/curl/Meta/links.rds
/usr/lib64/R/library/curl/Meta/nsInfo.rds
/usr/lib64/R/library/curl/Meta/package.rds
/usr/lib64/R/library/curl/Meta/vignette.rds
/usr/lib64/R/library/curl/NAMESPACE
/usr/lib64/R/library/curl/NEWS
/usr/lib64/R/library/curl/R/curl
/usr/lib64/R/library/curl/R/curl.rdb
/usr/lib64/R/library/curl/R/curl.rdx
/usr/lib64/R/library/curl/data/Rdata.rdb
/usr/lib64/R/library/curl/data/Rdata.rds
/usr/lib64/R/library/curl/data/Rdata.rdx
/usr/lib64/R/library/curl/doc/index.html
/usr/lib64/R/library/curl/doc/intro.R
/usr/lib64/R/library/curl/doc/intro.Rmd
/usr/lib64/R/library/curl/doc/intro.html
/usr/lib64/R/library/curl/help/AnIndex
/usr/lib64/R/library/curl/help/aliases.rds
/usr/lib64/R/library/curl/help/curl.rdb
/usr/lib64/R/library/curl/help/curl.rdx
/usr/lib64/R/library/curl/help/paths.rds
/usr/lib64/R/library/curl/html/00Index.html
/usr/lib64/R/library/curl/html/R.css
/usr/lib64/R/library/curl/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/curl/libs/curl.so
