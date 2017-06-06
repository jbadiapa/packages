# Generated from fluent-plugin-typecast-0.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-typecast

Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 1%{?dist}
Summary: Fluentd plugin to typecast output
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/tarom/fluent-plugin-typecast
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(jeweler) >= 1.8.4
# BuildRequires: rubygem(jeweler) < 1.9
# BuildRequires: rubygem(test-unit) >= 3.0.9
# BuildRequires: rubygem(test-unit) < 3.1
BuildArch: noarch

%description
typecast output plugin for fluentd.


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
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/Rakefile.ci
%{gem_instdir}/VERSION
%exclude %{gem_instdir}/fluent-plugin-typecast.gemspec
%{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Sun Jun 04 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.2.0-1
- Initial package
