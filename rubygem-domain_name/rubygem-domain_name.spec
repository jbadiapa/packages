# Generated from domain_name-0.5.20170404.gem by gem2rpm -*- rpm-spec -*-
%global gem_name domain_name

Name: rubygem-%{gem_name}
Version: 0.5.20170404
Release: 1%{?dist}
Summary: Domain Name manipulation library for Ruby
Group: Development/Languages
License: BSD and MPLv2.0
URL: https://github.com/knu/ruby-domain_name
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(test-unit) >= 2.5.5
# BuildRequires: rubygem(test-unit) < 2.6
BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}

%description
This is a Domain Name manipulation library for Ruby.
It can also be used for cookie domain validation based on the Public
Suffix List.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

sed -i -e 's/\/usr\/bin\/env ruby/\/usr\/bin\/ruby/g' %{gem_name}-%{version}/tool/gen_etld_data.rb
chmod 744 %{gem_name}-%{version}/tool/gen_etld_data.rb

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
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/data
%exclude %{gem_instdir}/domain_name.gemspec
%{gem_libdir}
%{gem_instdir}/tool
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.5.20170404-1
- Initial package
