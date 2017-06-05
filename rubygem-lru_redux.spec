# Generated from lru_redux-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name lru_redux

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: An efficient implementation of an lru cache
Group: Development/Languages
License: MIT
URL: https://github.com/SamSaffron/lru_redux
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
# BuildRequires: rubygem(minitest)
# BuildRequires: rubygem(guard-minitest)
# BuildRequires: rubygem(guard)
# BuildRequires: rubygem(rb-inotify)
# BuildRequires: rubygem(timecop) >= 0.7
# BuildRequires: rubygem(timecop) < 1
BuildArch: noarch

%description
A ruby efficient implementation of an lru cache.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

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




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bench
%{gem_libdir}
%exclude %{gem_instdir}/lru_redux.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Mon Jun 05 2017 Juan Badia Payno <jbadiapa@redhat.com> - 1.1.0-1
- Initial package
