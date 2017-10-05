# Generated from bigdecimal-1.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bigdecimal

# This will enable test on the future
# and also added it depdendencies
%global with_test 0 

Name: rubygem-%{gem_name}
Version: 1.3.2
Release: 1%{?dist}
Summary: Arbitrary-precision decimal floating-point number library
Group: Development/Languages
License: BSD 
URL: https://github.com/ruby/bigdecimal
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
%if 0%{?with_test}
BuildRequires: rubygem(rake-compiler) >= 0.9
BuildRequires: rubygem(rake-compiler) < 1
BuildRequires: rubygem(minitest) >= 4.7.5
BuildRequires: rubygem(minitest) < 4.8
BuildRequires: rubygem(pry)
%endif

%if 0%{?rhel} > 0
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
This library provides arbitrary-precision decimal floating-point number class.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

sed -i -e "s/\/usr\/local\/bin\/ruby/\/usr\/bin\/ruby/g" %{gem_name}-%{version}/sample/nlsolve.rb
sed -i -e 's/\/usr\/local\/bin\/ruby/\/usr\/bin\/ruby/g' %{gem_name}-%{version}/sample/linear.rb
sed -i -e 's/\/usr\/local\/bin\/ruby/\/usr\/bin\/ruby/g' %{gem_name}-%{version}/sample/pi.rb
chmod 755 %{gem_name}-%{version}/sample/nlsolve.rb
chmod 755 %{gem_name}-%{version}/sample/linear.rb
chmod 755 %{gem_name}-%{version}/sample/pi.rb

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


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
cp -a .%{gem_extdir_mri}/*.so %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/bigdecimal.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/sample

%changelog
* Sat Sep 30 2017 vagrant - 1.3.2-1
- Initial package
