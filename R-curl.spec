#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-curl
Version  : 3.2
Release  : 65
URL      : https://cran.r-project.org/src/contrib/curl_3.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/curl_3.2.tar.gz
Summary  : A Modern and Flexible Web Client for R
Group    : Development/Tools
License  : MIT
Requires: R-curl-lib
Requires: R-spelling
BuildRequires : R-httpuv
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-magrittr
BuildRequires : R-markdown
BuildRequires : R-spelling
BuildRequires : R-testthat
BuildRequires : clr-R-helpers
BuildRequires : curl-dev

%description
configurable drop-in replacements for base url() and download.file() with
    better performance, support for encryption (https, ftps), gzip compression,
    authentication, and other 'libcurl' goodies. The core of the package implements a
    framework for performing fully customized requests where data can be processed
    either in memory, on disk, or streaming via the callback or connection
    interfaces. Some knowledge of 'libcurl' is recommended; for a more-user-friendly
    web client see the 'httr' package which builds on this package with http
    specific tools and logic.

%package lib
Summary: lib components for the R-curl package.
Group: Libraries

%description lib
lib components for the R-curl package.


%prep
%setup -q -c -n curl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523746379

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523746379
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library curl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library curl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library curl
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library curl|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || : || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/curl/DESCRIPTION
/usr/lib64/R/library/curl/INDEX
/usr/lib64/R/library/curl/LICENSE
/usr/lib64/R/library/curl/Meta/Rd.rds
/usr/lib64/R/library/curl/Meta/data.rds
/usr/lib64/R/library/curl/Meta/features.rds
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
/usr/lib64/R/library/curl/WORDLIST
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
/usr/lib64/R/library/curl/libs/curl.so.avx2
/usr/lib64/R/library/curl/libs/curl.so.avx512
