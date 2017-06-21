# Generated from netrc-0.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name netrc

Name: rubygem-%{gem_name}
Version: 0.11.0
Release: 1%{?dist}
Summary: Library to read and write netrc files
Group: Development/Languages
License: MIT
URL: https://github.com/geemus/netrc
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
This library can read and update netrc files, preserving formatting including
comments and whitespace.


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
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Readme.md
%doc %{gem_instdir}/changelog.txt
%{gem_instdir}/test

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.11.0-1
- Initial package
