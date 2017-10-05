# Generated from public_suffix-2.0.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name public_suffix

# This will enable test on the future
# and also added it depdendencies
%global with_test 0 

Name: rubygem-%{gem_name}
Version: 2.0.5
Release: 3%{?dist}
Summary: Domain name parser based on the Public Suffix List
# MPLv2.0: %%{gem_instdir}/data/list.txt
License: MIT and MPLv2.0
URL: https://simonecarletti.com/code/publicsuffix-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if 0%{?with_test}
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
%endif

BuildArch: noarch

%if 0%{?rhel} > 0
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
PublicSuffix can parse and decompose a domain name into top level domain,
domain and subdomains.


%package doc
Summary: Documentation for %{name}
# Public Domain: %%{gem_instdir}/test/tests.txt
License: MIT and Public Domain
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



%check
pushd .%{gem_instdir}
%if 0%{?with_test}
# We don't have minitest-reporters in Fedora yet, but they are not needed
# very likely.
sed -i '/[Rr]eporters/ s/^/#/' test/test_helper.rb

LANG=C.utf-8 ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
%endif
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_instdir}/public_suffix.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/2.0-Upgrade.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Vít Ondruch <vondruch@redhat.com> - 2.0.5-2
- Fix license fields.

* Thu Apr 06 2017 Vít Ondruch <vondruch@redhat.com> - 2.0.5-1
- Initial package
