#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-curl
Version  : 5.2.3
Release  : 123
URL      : https://cran.r-project.org/src/contrib/curl_5.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/curl_5.2.3.tar.gz
Summary  : A Modern and Flexible Web Client for R
Group    : Development/Tools
License  : MIT
Requires: R-curl-lib = %{version}-%{release}
BuildRequires : buildreq-R
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
%setup -q -n curl
pushd ..
cp -a curl buildavx2
popd
pushd ..
cp -a curl buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726842669

%install
export SOURCE_DATE_EPOCH=1726842669
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/curl/DESCRIPTION
/usr/lib64/R/library/curl/INDEX
/usr/lib64/R/library/curl/LICENSE
/usr/lib64/R/library/curl/Meta/Rd.rds
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
/usr/lib64/R/library/curl/R/sysdata.rdb
/usr/lib64/R/library/curl/R/sysdata.rdx
/usr/lib64/R/library/curl/WORDLIST
/usr/lib64/R/library/curl/doc/index.html
/usr/lib64/R/library/curl/doc/intro.R
/usr/lib64/R/library/curl/doc/intro.Rmd
/usr/lib64/R/library/curl/doc/intro.html
/usr/lib64/R/library/curl/doc/windows.R
/usr/lib64/R/library/curl/doc/windows.Rmd
/usr/lib64/R/library/curl/doc/windows.html
/usr/lib64/R/library/curl/help/AnIndex
/usr/lib64/R/library/curl/help/aliases.rds
/usr/lib64/R/library/curl/help/curl.rdb
/usr/lib64/R/library/curl/help/curl.rdx
/usr/lib64/R/library/curl/help/paths.rds
/usr/lib64/R/library/curl/html/00Index.html
/usr/lib64/R/library/curl/html/R.css
/usr/lib64/R/library/curl/tests/spelling.R
/usr/lib64/R/library/curl/tests/testthat.R
/usr/lib64/R/library/curl/tests/testthat/helper-version.R
/usr/lib64/R/library/curl/tests/testthat/test-auth.R
/usr/lib64/R/library/curl/tests/testthat/test-blockopen.R
/usr/lib64/R/library/curl/tests/testthat/test-certificates.R
/usr/lib64/R/library/curl/tests/testthat/test-connection.R
/usr/lib64/R/library/curl/tests/testthat/test-cookies.R
/usr/lib64/R/library/curl/tests/testthat/test-echo.R
/usr/lib64/R/library/curl/tests/testthat/test-escape.R
/usr/lib64/R/library/curl/tests/testthat/test-gc.R
/usr/lib64/R/library/curl/tests/testthat/test-handle.R
/usr/lib64/R/library/curl/tests/testthat/test-idn.R
/usr/lib64/R/library/curl/tests/testthat/test-multi-download.R
/usr/lib64/R/library/curl/tests/testthat/test-multi.R
/usr/lib64/R/library/curl/tests/testthat/test-nonblocking.R
/usr/lib64/R/library/curl/tests/testthat/test-path.R
/usr/lib64/R/library/curl/tests/testthat/test-post.R
/usr/lib64/R/library/curl/tests/testthat/test-progress.R
/usr/lib64/R/library/curl/tests/testthat/test-seek.R
/usr/lib64/R/library/curl/tests/testthat/test-upload.R
/usr/lib64/R/library/curl/tests/testthat/test-winssl.R
/usr/lib64/R/library/curl/tests/testthat/test-writer.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/curl/libs/curl.so
/V4/usr/lib64/R/library/curl/libs/curl.so
/usr/lib64/R/library/curl/libs/curl.so
