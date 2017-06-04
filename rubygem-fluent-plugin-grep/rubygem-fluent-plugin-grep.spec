# Generated from fluent-plugin-grep-0.3.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-grep

Name: rubygem-%{gem_name}
Version: 0.3.4
Release: 1%{?dist}
Summary: Fluentd Plugin to use grep on the messages
Group: Development/Languages
License: MIT
URL: https://github.com/sonots/fluent-plugin-grep
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(test-unit)
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(pry-nav)
BuildArch: noarch

%description
fluentd plugin to grep messages.


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
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/fluent-plugin-grep.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.fluentd.lt.0.12
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Sun Jun 04 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.3.4-1
- Initial package
