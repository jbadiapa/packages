# Generated from fluent-plugin-kubernetes_metadata_filter-0.27.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-kubernetes_metadata_filter

Name: rubygem-%{gem_name}
Version: 0.27.0
Release: 1%{?dist}
Summary: Filter plugin to add Kubernetes meta-data
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/fabric8io/fluent-plugin-kubernetes_metadata_filter
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
# BuildRequires: rubygem(minitest) >= 4.0
# BuildRequires: rubygem(minitest) < 5
# BuildRequires: rubygem(test-unit) >= 3.0.2
# BuildRequires: rubygem(test-unit) < 3.1
# BuildRequires: rubygem(test-unit-rr) >= 1.0.3
# BuildRequires: rubygem(test-unit-rr) < 1.1
# BuildRequires: rubygem(copyright-header)
# BuildRequires: rubygem(webmock)
# BuildRequires: rubygem(vcr)
# BuildRequires: rubygem(bump)
# BuildRequires: rubygem(yajl-ruby)
BuildArch: noarch

%description
Filter plugin to manage Kubernetes meta-data.


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
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/circle.yml
%exclude %{gem_instdir}/fluent-plugin-kubernetes_metadata_filter.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Sun Jun 04 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.27.0-1
- Initial package
