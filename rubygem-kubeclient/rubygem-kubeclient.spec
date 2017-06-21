# Generated from kubeclient-2.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name kubeclient

Name: rubygem-%{gem_name}
Version: 2.4.0
Release: 1%{?dist}
Summary: A client for Kubernetes REST api
Group: Development/Languages
License: MIT
URL: https://github.com/abonas/kubeclient
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
# BuildRequires: rubygem(minitest)
# BuildRequires: rubygem(webmock) >= 1.24.2
# BuildRequires: rubygem(webmock) < 1.25
# BuildRequires: rubygem(vcr)
# BuildRequires: rubygem(rubocop) = 0.30.0
BuildArch: noarch

%description
A client for Kubernetes REST api.


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
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/kubeclient.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile-rest-client-1.8.rb
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 2.4.0-1
- Initial package
