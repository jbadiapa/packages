# Generated from oj-3.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name oj
%global debug_package %{nil}

Name: rubygem-%{gem_name}
Version: 3.1.0
Release: 1%{?dist}
Summary: A fast JSON parser and serializer
Group: Development/Languages
License: MIT
URL: http://www.ohler.com/oj
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-oj-0.patch 
Patch1: rubygem-oj-1.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem-minitest
BuildRequires: rubygem-bigdecimal
BuildRequires: rubygem-test-unit
#BuildRequires: rubygem-
# BuildRequires: rubygem(rake-compiler) >= 0.9
# BuildRequires: rubygem(rake-compiler) < 1
# BuildRequires: rubygem(minitest) >= 5
# BuildRequires: rubygem(minitest) < 6
# BuildRequires: rubygem(wwtd)
# BuildRequires: rubygem(wwtd) < 1

%description
The fastest JSON parser and object serializer.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%patch0 -p0
for FILE in `find %{gem_name}-%{version} -name '*.rb'`; 
do 
    sed -i -e 's/\/usr\/bin\/env ruby/\/usr\/bin\/ruby/g' ${FILE}
    BIN=`head -n 1 ${FILE} | grep "bin\/ruby" | wc -l`
    if [ ${BIN} -eq 1 ]; then    
      chmod 744 ${FILE}
    fi
done
chmod 644 %{gem_name}-%{version}/test/test_debian.rb

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%patch1 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

# Run the test suite
%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**/tests.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/pages
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/test

%changelog
* Wed Jun 07 2017 Juan Badia Payno <jbadiapa@redhat.com> - 3.1.0-1
- Initial package
