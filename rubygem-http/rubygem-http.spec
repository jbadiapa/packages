# Generated from http-2.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name http

Name: rubygem-%{gem_name}
Version: 2.2.2
Release: 1%{?dist}
Summary: HTTP should be easy
Group: Development/Languages
License: MIT
URL: https://github.com/httprb/http
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0
BuildArch: noarch

%description
An easy-to-use client library for making requests from Ruby. It uses a simple
method chaining system for building requests, similar to Python's Requests.


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
%{gem_instdir}/.coveralls.yml
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%{gem_instdir}/.ruby-version
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%{gem_instdir}/CHANGES.md
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/http.gemspec
%{gem_libdir}
%{gem_instdir}/logo.png
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 2.2.2-1
- Initial package
