# Generated from rest-client-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rest-client

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: HTTP & REST client for ruby
Group: Development/Languages
License: MIT
URL: https://github.com/rest-client/rest-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
# BuildRequires: rubygem(webmock) >= 2.0
# BuildRequires: rubygem(webmock) < 3
# BuildRequires: rubygem(rspec) >= 3.0
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(pry) < 1
# BuildRequires: rubygem(pry-doc)
# BuildRequires: rubygem(pry-doc) < 1
# BuildRequires: rubygem(rubocop)
# BuildRequires: rubygem(rubocop) < 1
BuildArch: noarch

%description
A simple HTTP and REST client for Ruby, inspired by the Sinatra microframework
style of specifying actions: get, put, post, delete.


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/restclient
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.rubocop-disables.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/rest-client.gemspec
%exclude %{gem_instdir}/rest-client.windows.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/AUTHORS
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/history.md
%{gem_instdir}/spec

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 2.0.2-1
- Initial package
