#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-curl
Version  : 4.3.1
Release  : 92
URL      : https://cran.r-project.org/src/contrib/curl_4.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/curl_4.3.1.tar.gz
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
%setup -q -c -n curl
cd %{_builddir}/curl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619792008

%install
export SOURCE_DATE_EPOCH=1619792008
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc curl || :


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
/usr/lib64/R/library/curl/tests/engine.R
/usr/lib64/R/library/curl/tests/engine.Rout.save
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
/usr/lib64/R/library/curl/tests/testthat/test-multi.R
/usr/lib64/R/library/curl/tests/testthat/test-nonblocking.R
/usr/lib64/R/library/curl/tests/testthat/test-path.R
/usr/lib64/R/library/curl/tests/testthat/test-post.R
/usr/lib64/R/library/curl/tests/testthat/test-progress.R
/usr/lib64/R/library/curl/tests/testthat/test-upload.R
/usr/lib64/R/library/curl/tests/testthat/test-writer.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/curl/libs/curl.so
